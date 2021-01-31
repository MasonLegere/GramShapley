import argparse
import copy
from typing import Final
import pandas as pd
import yaml
from tabulate import tabulate

parser = argparse.ArgumentParser(description='Implementation of the Gale-Shapley algorithm')
parser.add_argument('scenario', metavar='S', type=str, nargs=1, help='The scenario to be ran as specified in '
                                                                     'config.yaml')
# TODO: add argument for configuration file location
# TODO: add command to run all tests


def print_matching(pairs):
    hospitals = set([pair[1][0] for pair in pairs.items()])
    df = {}
    for value in hospitals:
        df[value] = [k for k, v in pairs.items() if v[0] == value]

    print(tabulate(pd.DataFrame.from_dict(df, orient='index').T.fillna("-"), headers='keys', tablefmt='psql'))


class GaleShapley:
    PARAMETERS: Final = yaml.load(open('config.yaml'),
                                  Loader=yaml.FullLoader)

    def __init__(self, scenario):
        self._parameters = GaleShapley.PARAMETERS[scenario]
        self._hospitals = self._parameters['hospitals']
        self._residents = self._parameters['residents']

    def __call__(self, *args, **kwargs):
        return self.apply()

    def find_matching(self):

        pairs = {}
        hospitals_remaining = copy.deepcopy(self._hospitals)
        rankings = {name: {k: v for v, k in enumerate(resident)} for name, resident in self._residents.items()}

        while hospitals_remaining:
            hospital_name, values = next(iter(hospitals_remaining.items()))
            preferences = values['preferences']

            if preferences:
                resident = preferences.pop(0)

                if resident not in pairs:
                    pairs[resident] = hospital_name, values

                    values['open_positions'] -= 1
                    if values['open_positions'] == 0:
                        hospitals_remaining.pop(hospital_name)


                else:
                    previous_name, previous_values = pairs[resident]
                    if rankings[resident][hospital_name] < rankings[resident][previous_name]:

                        pairs[resident] = hospital_name, values
                        values['open_positions'] -= 1

                        if values['open_positions'] == 0:
                            hospitals_remaining[previous_name] = previous_values

                        if values['open_positions'] == 0:
                            hospitals_remaining.pop(hospital_name)

                        previous_values['open_positions'] += 1

        return pairs


if __name__ == '__main__':
    args = parser.parse_args()
    # TODO: refactor to include configuration test
    print_matching(GaleShapley('scenario_1').find_matching())

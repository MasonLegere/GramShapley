from collections import deque
import math

class HospitalMatcher:

    def __init__(self):
        settings = 


    def create_matching(self, scenario_name):
        pass


    def gale_shapley(self, hospitals, residents):






class Resident:

    def __init__(self, student_config):
        self._preferences = {k: v for v, k in enumerate(student_config['preferences_list'])}
        self._current_offer = math.inf

    def offer(self, hospital):
        if self._preferences[hospital.id] < self._current_offer:
            hospital.drop_offer()
            self._current_offer = self._preferences[hospital.id]
            return True
        return False



class Hospital:

    def __init__(self, hospital_config):
        self._preferences =  deque(hospital_config['preference_list'])
        self._positions_needed = hospital_config['positions_open']
        self.positions_open = self._positions_needed
        self.id = hospital_config['id']


    def next(self):
        return self._preferences.popleft()

    def offer_declined(self):
        self.positions_open += 1

    def make_offer(self, residents):
        offer_accepted = False

        while not offer_accepted:
            resident = residents[self.next()]
            if resident.offer(self):
                self.positions_open -= 1
                offer_accepted = True












# Gale-Shapley Algorithm 

Within this code we implement a slightly modified Gale-Shapley algorithm whereby one hospital H<sub>1</sub> can be assigned
several residents R<sub>1</sub>, R<sub>2</sub>, ..., R<sub>k</sub> where the hospital has ``k`` positions available. 


Scenarios to be run are included in `config.yaml` where you provide a scenario name followed by a dictionary of `hospitals` and `residents`. For both 
you must include the list of corresponding preferences, and with hospitals you must also specify  `open_positions` which is the number of open positions at a hospital. 

### Correctness: 
Pseudocode of the modified Gale-Shapley algorithm as well as proof of correctness and worst-case runtime performance is included 
in `/Gram-Shapley_Analysis.pdf`

### Assumptions: 
- Valid input is given in `config.yaml`. No pre-processing or validation is done. 
- As per the question, we assume that we have a surplus of residents. That is, all residents obtain a seat. 

### Run Guide:
All commands are to be ran from the project directory.    
To install dependencies: 
```console
foo@bar:~$ pip install -r requirements.txt
```
 To run a particular `scenario = example` that must be included in `config.yaml` run:
```console
foo@bar:~$ python main.py -s $scenario
```


### Output Examples:
Using the two included examples, `scenario1` and `scenario2` in `config.yaml` we get
```console
foo@bar:~$ python main.py -s scenario1
+----+-------------+-------------+-------------+
|    | hospital1   | hospital3   | hospital2   |
|----+-------------+-------------+-------------|
|  0 | resident6   | resident1   | resident4   |
|  1 | -           | resident2   | resident5   |
|  2 | -           | -           | resident3   |
+----+-------------+-------------+-------------+
```
```console
foo@bar:~$ python main.py -s scenario2
+----+-------------+-------------+-------------+
|    | hospital2   | hospital1   | hospital3   |
|----+-------------+-------------+-------------|
|  0 | resident6   | resident1   | resident2   |
|  1 | resident5   | -           | resident4   |
|  2 | resident3   | -           | -           |
|  3 | resident7   | -           | -           |
|  4 | resident8   | -           | -           |
|  5 | resident9   | -           | -           |
|  6 | resident10  | -           | -           |
+----+-------------+-------------+-------------+
```

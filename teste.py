import json
import test_function

#Load parameter values from json file and store in param dictionary
with open('ga_params.json', 'r') as f:
    param = json.load(f)

ranges = test_function.get_ranges()

print(ranges[0][1][0])
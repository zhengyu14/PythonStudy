# file path C:\Users\i323429\Documents\GitHub\PythonStudy\Learning Data Mining with Python\Code_REWRITE\Chapter 1\Test.py

import numpy as np

# read dataset with line features: bread, milk, cheese, apples, bananas
dataset_filename = "affinity_dataset.txt"
dataset = np.loadtxt(dataset_filename)
samples, features = dataset.shape
feature_name_set = ["bread", "milk", "cheese", "apples", "bananas"]
print ("This dataset conatins {0} and {1} features.".format(samples, features))
print ("------------------------------------------------------------------------")

# calculate the number of people who buy apples
apples_entries = 0
for entry in dataset:
    if entry[3] == 1:
        apples_entries += 1
print ("{0} people buy apples.".format(apples_entries))
print ("------------------------------------------------------------------------")

# validate rule: people buys apples also buys bananas
valid_entries = 0
invalid_entries = 0
for entry in dataset:
    if (entry[3] == 1) & (entry[4] == 1):
        valid_entries += 1
    elif (entry[3] == 1) & (entry[4] != 1):
        invalid_entries += 1
print ("Validate rule: people buys apples also buys bananas:")
print ("{0} entries are valid, while {1} entries are invalid.".format(valid_entries, invalid_entries))
support = valid_entries
confidence = valid_entries / apples_entries
print ("The support is {0} and the confidence is {1:.1f}%.".format(support, confidence * 100))
print ("------------------------------------------------------------------------")

# find the rules in all premise-conclusion combination: people buys what also buys what
from collections import defaultdict
valid_rules = defaultdict(int)
num_occurence = defaultdict(int)
for row in dataset:
    for premise in range(features):
        if row[premise] == 0:
            continue
        if row[premise] == 1:    # find the premise item and check other items
            num_occurence[premise] += 1
            for conclusion in range(features):
                if premise == conclusion: # ignore itself
                    continue
                if row[conclusion] == 1:
                    valid_rules[(premise, conclusion)] += 1
support = valid_rules
confidence = defaultdict(float)
for premise, conclusion in valid_rules.keys():
    confidence[(premise, conclusion)] = valid_rules[(premise, conclusion)] / num_occurence[premise]
for premise, conclusion in confidence.keys():
    premise_name = feature_name_set[premise]
    conclusion_name = feature_name_set[conclusion]
    print ("Rule: people buy {0} will also buy {1}: ".format(premise_name, conclusion_name))
    print (" support   : {0}".format(valid_rules[(premise, conclusion)]))
    print (" confidence: {0:.1f}%.".format(confidence[(premise, conclusion)] * 100))
print ("------------------------------------------------------------------------")

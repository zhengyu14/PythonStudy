# file path C:\Users\i323429\Documents\GitHub\PythonStudy\Learning Data Mining with Python\Code_REWRITE\Chapter 1\Test_Affinity_Analysis.py

import numpy as np

# 1: read dataset with line features: bread, milk, cheese, apples, bananas
print("1: ")
dataset_filename = "affinity_dataset.txt"
dataset = np.loadtxt(dataset_filename)
samples, features = dataset.shape
feature_name_set = ["bread", "milk", "cheese", "apples", "bananas"]
print ("This dataset conatins {0} and {1} features.".format(samples, features))
print ("------------------------------------------------------------------------")

# 2: calculate the number of people who buy apples
print("2: ")
apples_entries = 0
for entry in dataset:
    if entry[3] == 1:
        apples_entries += 1
print ("{0} people buy apples.".format(apples_entries))
print ("------------------------------------------------------------------------")

# 3: validate rule: people buys apples also buys bananas
# calculate support and confidence
print("3: ")
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

# 4: find the rules in all premise-conclusion (前提: 买了...-结论: 也会买...) combination: people buys what also buys what
# calculate support and confidence
print("4: ")
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
    print ("    support   : {0}".format(valid_rules[(premise, conclusion)]))
    print ("    confidence: {0:.1f}%.".format(confidence[(premise, conclusion)] * 100))
print ("------------------------------------------------------------------------")

# 5: sort the rules by support and display the top 3 rules
print("5: ")
from operator import itemgetter
sorted_support = sorted(support.items(), key=itemgetter(1), reverse=True)
print ("Top 3 rules with highest support:")
for index in range(3):
    premise, conclusion = sorted_support[index][0]
    print ("Rule #{0}: people buy {1} will also buy {2}: ".format(index + 1, feature_name_set[premise], feature_name_set[conclusion]))
    print ("    support   : {0}".format(valid_rules[(premise, conclusion)]))
    print ("    confidence: {0:.1f}%.".format(confidence[(premise, conclusion)] * 100))
print ("------------------------------------------------------------------------")

# 6: sort the rules by confidence and display the top 3 rules
print("6: ")
from operator import itemgetter
sorted_support = sorted(confidence.items(), key=itemgetter(1), reverse=True)
print ("Top 3 rules with highest confidence:")
for index in range(3):
    premise, conclusion = sorted_support[index][0]
    print ("Rule #{0}: people buy {1} will also buy {2}: ".format(index + 1, feature_name_set[premise], feature_name_set[conclusion]))
    print ("    support   : {0}".format(valid_rules[(premise, conclusion)]))
    print ("    confidence: {0:.1f}%.".format(confidence[(premise, conclusion)] * 100))
print ("------------------------------------------------------------------------")

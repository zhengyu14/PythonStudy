# file path C:\Users\i323429\Documents\GitHub\PythonStudy\Learning Data Mining with Python\Code_REWRITE\Chapter 1\Test.py

import numpy as np

# read dataset with line features: bread, milk, cheese, apples, bananas
dataset_filename = "affinity_dataset.txt"
dataset = np.loadtxt(dataset_filename)
samples, features = dataset.shape
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
print ("------------------------------------------------------------------------")

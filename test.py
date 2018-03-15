# Path (Mac): /Users/Zhengyu/Documents/Git/PythonStudy/test.py
# Path (Win): C:\Users\i323429\Documents\GitHub\PythonStudy\test.py
from sklearn.datasets import load_iris
import numpy as np
from collections import defaultdict
from operator import itemgetter
dataset = load_iris()
iris_data = dataset.data
iris_target = dataset.target
#print (iris_data.shape[1])

class_counts = defaultdict(int)
class_counts[0] = 2
class_counts[1] = 1
class_counts[2] = 0
print ([class_count for class_value, class_count in class_counts.items() if class_value != 0])
error = sum([class_count for class_value, class_count in class_counts.items() if class_value != 0])
print(error)

# file path C:\Users\i323429\Documents\GitHub\PythonStudy\Learning Data Mining with Python\Code_REWRITE\Chapter 1\Test_Classification.py
from sklearn.datasets import load_iris
import numpy as np

# 1: load load_iris dataset from scikit-learn library, display description and information
#   sepal: 萼片
#   petal: 花瓣
print ("1: ")
dataset = load_iris()
iris_data = dataset.data
iris_target = dataset.target
print (dataset.DESCR)
data_instances, data_attributes = iris_data.shape
print ("The data contains {0} instances, for each has {1} attributes.".format(data_instances, data_attributes))
print ("5 data samples in data: ")
for index in range(5):
    print (iris_data[index])
print ("In target: 0 - Iris Sentosa, 1 - Iris Cersicolour, 2 - Iris Virginica")
print ("5 data samples in target: ")
for index in range(5):
    print (iris_target[index])
print ("------------------------------------------------------------------------")

# 2: compute
attribute_means = iris_data.mean(axis=0)
print (attribute_means)
assert attribute_means.shape == (data_attributes,)
iris_data_d = np.array(iris_data >= attribute_means, dtype='int')
print (iris_data_d)

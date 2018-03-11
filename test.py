# Path: /Users/Zhengyu/Documents/Git/PythonStudy/test.py
data = [[1, 1], [1, 0], [3, 3]]

centroid = [0, 0]

cluster1 = data[0]

cluster2 = [data[1], data[2]]

def calDistance ( param1, param2 ):
    distanceSquare = (param1[0] - param2[0]) ** 2 + (param1[1] - param2[1]) ** 2
    distance = distanceSquare ** 0.5
    return distance;

distance = calDistance(data[0], centroid[0])

print distance;

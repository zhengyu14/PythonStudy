# file path: C:\Users\i323429\Documents\GitHub\PythonStudy\K_Means_Clustering.py
class coordinatePoint:
    xAxis = 0.0
    yAxis = 0.0

    def __init__(self, xAxis, yAxis):
        self.xAxis = xAxis
        self.yAxis = yAxis

class cluster:
    dataPoints = []

    def __init__(self, centroidXAxis, centroidYAxis): # Initialize a cluster with a centroid
        self.centroid = coordinatePoint(centroidXAxis, centroidYAxis)

    def addDataPoint(self, dataPoint):
        self.dataPoints.append(dataPoint)

    def updateCentroid(self):
        xAxisSum = 0.0
        yAxisSum = 0.0

        for index in range(len(self.dataPoints)):
            xAxisSum += self.dataPoints[index].xAxis
            yAxisSum += self.dataPoints[index].yAxis

        self.centroid.xAxis = xAxisSum / len(self.dataPoints)
        self.centroid.yAxis = yAxisSum / len(self.dataPoints)

    def clearCluster(self):
        del self.dataPoints[:]

def calDistance(data, centroid):
    distanceSquare = (data.xAxis - centroid.xAxis) ** 2 + (data.yAxis - centroid.yAxis) ** 2
    distance = distanceSquare ** 0.5
    return distance

def deriveCluster(data, cluster1, cluster2):
    distance1 = calDistance(data, cluster1.centroid)
    distance2 = calDistance(data, cluster2.centroid)

    if distance1 <= distance2:
        cluster1.addDataPoint(data)
    else:
        cluster2.addDataPoint(data)

# Create 5 data points into a data set and 2 clusters with random centoid
dataSet = [coordinatePoint(1, 1), coordinatePoint(1, 2), coordinatePoint(2, 2), coordinatePoint(5, 4), coordinatePoint(4, 5)]
cluster1 = cluster(0, 0)
cluster2 = cluster(3, 3)

# Objective function
flag = True
prevCentroid1 = []
prevCentroid2 = []

while flag:
    ## Assign data to cluster
    for index in range(len(dataSet)):
        deriveCluster(dataSet[index], cluster1, cluster2)

    if cluster1.centroid == prevCentroid1 & cluster2.centroid == prevCentroid2:
        flag = False
    else:
        prevCentroid1 = cluster1.centroid
        prevCentroid2 = cluster1.centroid
        cluster1,updateCentroid()
        cluster2,updateCentroid()
        cluster1.clearCluster()
        cluster2.clearCluster()

print "cluster1: ", cluster1.dataPoints, "cluster2: ", cluster2.dataPoints;

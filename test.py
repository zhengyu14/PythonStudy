# Path (Mac): /Users/Zhengyu/Documents/Git/PythonStudy/test.py
# Path (Win): C:\Users\i323429\Documents\GitHub\PythonStudy\test.py
class coordinatePoint:
    xAxis = 0.0
    yAxis = 0.0

    def __init__(self, xAxis, yAxis):
        self.xAxis = xAxis
        self.yAxis = yAxis

class cluster:
    dataPoints = []

    # Initialize a cluster with a centroid
    def __init__(self, centroidXAxis, centroidYAxis):
        self.centroid = coordinatePoint(centroidXAxis, centroidYAxis)

    def addToCluster(self, dataPoint):
        self.dataPoints.append(dataPoint)

    def clusterVol(self):
        return len(self.dataPoints)

    def clearCluster(self):
        del self.dataPoints[:]

    def updateCentroid(self):
        xAxisSum = 0.0
        yAxisSum = 0.0

        for index in range(len(self.dataPoints)):
            xAxisSum += self.dataPoints[index].xAxis
            yAxisSum += self.dataPoints[index].yAxis

        self.centroid.xAxis = xAxisSum / len(self.dataPoints)
        self.centroid.yAxis = yAxisSum / len(self.dataPoints)

testCluster = cluster(0, 0)
testCluster.addToCluster(coordinatePoint(1, 0))
testCluster.addToCluster(coordinatePoint(0, 2))
testCluster.addToCluster(coordinatePoint(6, 4))

print "Data in cluster: "

for index in range(len(testCluster.dataPoints)):
    print "x: ", testCluster.dataPoints[index].xAxis, "y: ", testCluster.dataPoints[index].yAxis

print "New centroid: "

testCluster.updateCentroid()

print "x: ", testCluster.centroid.xAxis, "y: ", testCluster.centroid.yAxis

print testCluster.clusterVol()

testCluster.clearCluster()
print len(testCluster.dataPoints)

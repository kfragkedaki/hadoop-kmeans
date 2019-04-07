__authors__ = "Vaggelis Malandrakis, KLeio Fragkedaki"

from mapper import getCentroids

#check if distance of centroids and centroids1 is less than 1
def checkCentroidsDistance(centroids, centroids1):
    f1x = abs(centroids[0][0] - centroids1[0][0])<1
    f1y = abs(centroids[0][1] - centroids1[0][1])<1
    f2x = abs(centroids[1][0] - centroids1[1][0])<1
    f2y = abs(centroids[1][1] - centroids1[1][1])<1
    f3x = abs(centroids[2][0] - centroids1[2][0])<1
    f3y = abs(centroids[2][1] - centroids1[2][1])<1

    if f1x and f1y and f2x and f2y and f3x and f3y:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    centroids1 = getCentroids('centroids1.txt')
    
    checkCentroidsDistance(centroids, centroids1)

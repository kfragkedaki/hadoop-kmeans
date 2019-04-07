#!/usr/bin/env python
"""mapper.py"""

__authors__ = "Vaggelis Malandrakis, KLeio Fragkedaki"

import sys
from math import sqrt

# get initial centroids from a txt file and add them in an array
def getCentroids(filepath):
    centroids = []

    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if line:
                try:
            	    line = line.strip()
            	    cord = line.split(', ')
                    # cord[0] is x and cord[1] is y point of a centroid
            	    centroids.append([float(cord[0]), float(cord[1])])
                except:
                    break
            else:
                break
            line = fp.readline()

    fp.close()
    return centroids

# create clusters based on initial centroids
def createClusters(centroids):
    # 
    for line in sys.stdin:
        line = line.strip()
        cord = line.split(',')
        min_dist = 100000000000000
        index = -1

        for centroid in centroids:
            try:
                cord[0] = float(cord[0])
                cord[1] = float(cord[1])
            except ValueError:
                # float was not a number, so silently
                # ignore/discard this line
                continue

            # euclidian distance from every point of dataset
            # to every centroid
            cur_dist = sqrt(pow(cord[0] - centroid[0], 2) + pow(cord[1] - centroid[1], 2))

            # find the centroid which is closer to the point
            if cur_dist <= min_dist:
                min_dist = cur_dist
                index = centroids.index(centroid)

        var = "%s\t%s\t%s" % (index, cord[0], cord[1])
        print(var)

if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    createClusters(centroids)

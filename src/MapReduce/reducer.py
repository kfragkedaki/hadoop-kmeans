#!/usr/bin/env python
"""reducer.py"""

__authors__ = "Vaggelis Malandrakis, KLeio Fragkedaki"

import sys

def calculateNewCentroids():
    current_centroid = None
    sum_x = 0
    sum_y = 0
    count = 0

    # input comes from STDIN
    for line in sys.stdin:

        # parse the input of mapper.py
        centroid_index, x, y = line.split('\t')

        # convert x and y (currently a string) to float
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            # float was not a number, so silently
            # ignore/discard this line
            continue

        # this IF-switch only works because Hadoop sorts map output
        # by key (here: word) before it is passed to the reducer
        if current_centroid == centroid_index:
            count += 1
            sum_x += x
            sum_y += y
        else:
            if count != 0:
                # print the average of every cluster to get new centroids
                print(str(sum_x / count) + ", " + str(sum_y / count))

            current_centroid = centroid_index
            sum_x = x
            sum_y = y
            count = 1
    
    # print last cluster's centroids
    if current_centroid == centroid_index and count != 0:
        print(str(sum_x / count) + ", " + str(sum_y / count))

if __name__ == "__main__":
    calculateNewCentroids()

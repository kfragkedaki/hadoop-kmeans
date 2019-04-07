from scipy.stats import skewnorm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import random, uniform
from math import sqrt, pow

# get random points that follows skew distribution and use them as distance
def skew():
    fig, ax = plt.subplots(1, 1) # This function creates a figure and a grid of subplots

    a = 5 # skewness parameter, when a = 0 the distribution is identical to a normal distribution

    # mean, variance, skew, kurt = skewnorm.stats ( a, moments='mvsk' )

    d = skewnorm.rvs(a, size=350000)

    ax.hist(d, density=True, histtype='stepfilled', alpha=0.2) # histogram of numbers generated
    plt.show()

    return d # return all the numbers generated with skew distribution

# get random point from a circle that has as center given centroid
# and as radius the distancew found in skew() function
def get_random_point(x, y, cluster):

    array = []
    distance = skew()

    for d in distance:
        while True:
            angle = random() * math.pi * 2
            x1 = x + math.cos (angle ) * d
            y1 = y + math.sin (angle ) * d
            # y1 = uniform(5, 30) # get a random float as y1
            # x1 = x - sqrt(abs(pow(d, 2) - pow(y - y1, 2))) # get x1 based on euclidean distance
            if [x1, y1, cluster] not in array:
                print('yeah')
                break # if the pair of (x1,y1) exist find another pair of (x1,y1)

        array.append([x1, y1, cluster])
        print(x1, y1, cluster, len(array))

    return array


if __name__ == '__main__':

    centers = [[10, 25], [2, -9], [-15, -35]] # pre-define three centers for clusters
    data = [] # array with all the final data

    for center in centers:
        # concat the results of these
       # three clusters in one array
        data = data + get_random_point ( center[0], center[1], centers.index(center)) print(len(data))
        print(data)

    plt.scatter([item[0] for item in data], [item[1] for item in data], c=[item[2] for item in data])
    plt.show()

    df = pd.DataFrame(data)
    df.drop(df.columns[[2]], axis=1, inplace=True)
    df.to_csv("dataset", header=False, index= False, sep="," )

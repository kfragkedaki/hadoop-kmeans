import matplotlib.pyplot as plt
from scipy.spatial import distance

centroids=[]

# initiliaze list for points
X=[[[],[]],[[],[]],[[],[]]]
# initiliaze list for centroids
M=[[],[]]

# import centroids.txt file
filepath = 'centroids.txt'
with open(filepath) as fp:
    # read line by line
    line = fp.readline()
    while line:
        if line:
            # delete blanks for each lines
            line = line.strip()
            # extract centroids coordinates
            cord = line.split(', ')
            centroids.append((float(cord[0]), float(cord[1])))
            M[0].append((float(cord[0])))
            M[1].append((float(cord[1])))
        else:
            break
        line = fp.readline()

fp.close()

# import dataset.txt file
filepath = 'dataset.txt'
with open(filepath) as fp:
    # read line by line
    line = fp.readline()
    while line:
        if line:
            # delete blanks for each lines
            line = line.strip()
            # extract points coordinates
            cord = line.split(',')
            x = (float(cord[0]), float(cord[1]))
            # implement k means loop
            # find the nearest centroid
            dist = 100000000000000
            selected_m = -1
            for m in centroids:
                test_distance = distance.euclidean(x, m)
                if test_distance < dist:
                    dist = test_distance
                    selected_m = centroids.index(m)

            X[selected_m][0].append(x[0])
            X[selected_m][1].append(x[1])
        else:
            break
        line = fp.readline()

fp.close()

# print cluster 0 with red color
plt.plot(X[0][0], X[0][1], 'ro')
# print cluster 1 with green color
plt.plot(X[1][0], X[1][1], 'go')
# print cluster 2 with blue color
plt.plot(X[2][0], X[2][1], 'bo')
# print centroids with yellow color
plt.plot(M[0], M[1], 'yo')
plt.axis([-22, 20, -50, 40])
plt.show()
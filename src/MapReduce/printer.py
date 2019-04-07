import random
import matplotlib.pyplot as plt
from scipy.spatial import distance

centroids=[]

x_dic={}
m_list=[[],[],[]]
X=[[[],[]],[[],[]],[[],[]]]
M=[[],[]]

print('Reading centroids...')

filepath = 'centroids.txt'
with open(filepath) as fp:
    line = fp.readline()
    while line:
        if line:
            line = line.strip()
            cord = line.split(', ')
            centroids.append((float(cord[0]), float(cord[1])))
            M[0].append((float(cord[0])))
            M[1].append((float(cord[1])))
        else:
            break
        line = fp.readline()

fp.close()

print('Reading centroids OK')
print('Reading dataset...')

#i = 0

filepath = 'dataset.txt'
with open(filepath) as fp:
    line = fp.readline()
    while line:
        if line:
            line = line.strip()
            cord = line.split(',')
            x = (float(cord[0]), float(cord[1]))
            dist = 100000000000000
            selected_m = -1
            for m in centroids:
                test_distance = distance.euclidean(x, m)
                if test_distance < dist:
                    dist = test_distance
                    selected_m = centroids.index(m)

            x_dic[x] = [selected_m, dist]
            m_list[selected_m].append(x)
            X[selected_m][0].append(x[0])
            X[selected_m][1].append(x[1])
        else:
            break
        line = fp.readline()
        i += 1
        #if i % 50000 == 0:
        #    print(i)

fp.close()

plt.plot(X[0][0], X[0][1], 'ro')
plt.plot(X[1][0], X[1][1], 'go')
plt.plot(X[2][0], X[2][1], 'bo')
plt.plot(M[0], M[1], 'yo')
plt.axis([-22, 20, -50, 40])
plt.show()

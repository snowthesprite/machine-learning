import sys
sys.path.append('src')
from k_means_clustering import *

'''
columns = ['Portion Eggs',
            'Portion Butter',
            'Portion Sugar',
            'Portion Flour']

data = [[0.14, 0.14, 0.28, 0.44],
        [0.22, 0.1, 0.45, 0.33],
        [0.1, 0.19, 0.25, 0.4],
        [0.02, 0.08, 0.43, 0.45],
        [0.16, 0.08, 0.35, 0.3],
        [0.14, 0.17, 0.31, 0.38],
        [0.05, 0.14, 0.35, 0.5],
        [0.1, 0.21, 0.28, 0.44],
        [0.04, 0.08, 0.35, 0.47],
        [0.11, 0.13, 0.28, 0.45],
        [0.0, 0.07, 0.34, 0.65],
        [0.2, 0.05, 0.4, 0.37],
        [0.12, 0.15, 0.33, 0.45],
        [0.25, 0.1, 0.3, 0.35],
        [0.0, 0.1, 0.4, 0.5],
        [0.15, 0.2, 0.3, 0.37],
        [0.0, 0.13, 0.4, 0.49],
        [0.22, 0.07, 0.4, 0.38],
        [0.2, 0.18, 0.3, 0.4]]

# we usually don't know the classes, of the 
# data we're trying to cluster, but I'm providing
# them here so that you can actually see that the
# k-means algorithm succeeds.

classes = ['Shortbread',
            'Fortune',
            'Shortbread',
            'Sugar',
            'Fortune',
            'Shortbread',
            'Sugar',
            'Shortbread',
            'Sugar',
            'Shortbread',
            'Sugar',
            'Fortune',
            'Shortbread',
            'Fortune',
            'Sugar',
            'Shortbread',
            'Sugar',
            'Fortune',
            'Shortbread']

initial_clusters = {
    1: [0,3,6,9,12,15,18],
    2: [1,4,7,10,13,16],
    3: [2,5,8,11,14,17]
    }

kmeans = KMeans(initial_clusters, data)

kmeans.run()

print('Does KMeans Clustering work?')
assert kmeans.clusters == {
    1: [0, 2, 5, 7, 9, 12, 15, 18],
    2: [3, 6, 8, 10, 14, 16],
    3: [1, 4, 11, 13, 17]
}
print('Yosh\n')
#'''
## May 24th
#'''

columns = ['Portion Eggs',
            'Portion Butter',
            'Portion Sugar',
            'Portion Flour']

data = [[0.14, 0.14, 0.28, 0.44],
        [0.22, 0.1, 0.45, 0.33],
        [0.1, 0.19, 0.25, 0.4],
        [0.02, 0.08, 0.43, 0.45],
        [0.16, 0.08, 0.35, 0.3],
        [0.14, 0.17, 0.31, 0.38],
        [0.05, 0.14, 0.35, 0.5],
        [0.1, 0.21, 0.28, 0.44],
        [0.04, 0.08, 0.35, 0.47],
        [0.11, 0.13, 0.28, 0.45],
        [0.0, 0.07, 0.34, 0.65],
        [0.2, 0.05, 0.4, 0.37],
        [0.12, 0.15, 0.33, 0.45],
        [0.25, 0.1, 0.3, 0.35],
        [0.0, 0.1, 0.4, 0.5],
        [0.15, 0.2, 0.3, 0.37],
        [0.0, 0.13, 0.4, 0.49],
        [0.22, 0.07, 0.4, 0.38],
        [0.2, 0.18, 0.3, 0.4]]

all_errors = []

for num_k in range(1, 6) :
    initial_clusters = {k : [] for k in range(1,num_k + 1)}
    current_cluster = 0
    for id in range(len(data)) :
        initial_clusters[current_cluster + 1].append(id)
        current_cluster = (current_cluster + 1) % num_k
    kmeans = KMeans(initial_clusters, data)
    kmeans.run()
    all_errors.append(kmeans.compute_square_error())

import matplotlib.pyplot as plt
#plt.style.use('bmh')

k_val = range(1, 6)

plt.plot(k_val, all_errors)
#plt.xlim((1,6))
plt.xticks(range(6))
plt.xlabel("k")
plt.ylabel("Sum Squared Error")

plt.savefig('tests/KNN_elbow.png')
#'''
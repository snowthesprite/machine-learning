import pandas as pd
import numpy as np
import sys
sys.path.append('src')
from k_nearest_neighbors_classifier import *

df = pd.DataFrame(
    [['A', 0],
     ['A', 1],
     ['B', 2],
     ['B', 3]],
     columns = ['letter', 'number']
)

knn = KNearestNeighborsClassifier(k=4)
knn.fit(df, dependent_variable = 'letter')
observation = {
    'number': 1.6
}

print('Testing K Nearest Neighbor Classifier...')

assert knn.classify(observation) == 'B'

print('Test succsessful')


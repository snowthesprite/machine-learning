import random
import math
import sys
sys.path.append('src')
from rand_forest import *


## Semi Random points
#''''
#random.seed(10)
centers = {1 : [(1,1), (4,4)], 2: [(1,4), (4,1)]}
points = []

for kind in range(1,3) :
    for num in range(100) :
        center = centers[kind][round(random.random())]
        point = []
        for axis in range(2) :
            sign = [1,-1][round(random.random())]
            point.append(center[axis] + random.random()*sign* num/25)
        points.append({'coord': point, 'type': kind})

point_num = len(points)
folds = 2

rand_folds = [[] for _ in range(folds)]
for fold in range(folds) :
    for __ in range(int(point_num/folds)) :
        id = math.floor(random.random() * len(points))
        rand_folds[fold].append(points[id])
        points.pop(id)

assert points == []

def find_accuracy(predictions, test) :
    correct = 0
    for index in range(len(test)) :
        if predictions[index] == test[index]['type'] :
            correct+=1
    return correct/len(test)

tree_num = [1,10,20,50,100,500,1000]
all_acc = {_ : [] for _ in tree_num}


for fold_id in range(folds) :
    print(fold_id)
    test_fold = rand_folds[fold_id]
    train_fold = []
    for new_id in range(folds) :
        if new_id != fold_id :
            train_fold.extend(rand_folds[new_id])
    for num_trees in tree_num :
        print(num_trees)
        predictions = []
        #rand 75% of training data
        train_data = []
        while len(train_data) < int(len(train_fold) * 3/4) :
            id = math.floor(random.random() * len(train_fold))
            train_data.append(train_fold[id])
        forest = RandForest(train_data, num_trees, 10)
        forest.make_forest_2()
        for point in test_fold :
            #print(point['coord'])
            predictions.append(forest.predict(point['coord']))
        all_acc[num_trees].append(find_accuracy(predictions, test_fold))
    print()

avg_acc = []
for acc in all_acc.values() :
    avg_acc.append(sum(acc)/len(acc))

#'''

#'''
import matplotlib.pyplot as plt
plt.style.use('bmh')

plt.plot(tree_num, avg_acc)

plt.savefig('Pred_Rand_Forest_Acc.png')
#'''
import random
import math
import sys
sys.path.append('src')
from decision_tree import DecisionTree

#random.seed(1)
'''
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



import matplotlib.pyplot as plt
plt.style.use('bmh')

kind = ['b+', 'r+']
plt.plot(1,1, 'mo')
plt.plot(4,4, 'mo')
plt.plot(1,4, 'mo')
plt.plot(4,1, 'mo')
for point_info in points :
    plt.plot(point_info['coord'][0], point_info['coord'][1], kind[point_info['type']-1])


plt.savefig('datasets/test_set.png')
#'''

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

rand_folds = [[] for _ in range(5)]
for fold in range(5) :
    for __ in range(int(point_num/5)) :
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

min_split_val = [1,2,5,10,15,20,30,50,100]
all_acc = {_ : [] for _ in min_split_val}

for fold_id in range(5) :
    print(fold_id)
    test_fold = rand_folds[fold_id]
    train_fold = []
    for new_id in range(5) :
        if new_id != fold_id :
            train_fold.extend(rand_folds[new_id])
    for min_split in min_split_val :
        predictions = []
        tree = DecisionTree(train_fold, min_split)
        tree.make_tree()
        for point in test_fold :
            #print(point['coord'])
            predictions.append(tree.predict(point['coord']))
        all_acc[min_split].append(find_accuracy(predictions, test_fold))

avg_acc = []
for acc in all_acc.values() :
    avg_acc.append(sum(acc)/len(acc))

#'''
import matplotlib.pyplot as plt
plt.style.use('bmh')

plt.plot(min_split_val, avg_acc)

plt.savefig('Fold_Acc.png')
#'''
import random
import math
import sys
sys.path.append('src')
from decision_tree import DecisionTree

points = [{'coord': (5,2), 'type' : 2},
        {'coord': (7,4), 'type' : 1},
        {'coord': (1,8), 'type' : 2},
        {'coord': (3,4), 'type' : 1},
        {'coord': (9,2), 'type' : 2}]

tree = DecisionTree(points)
tree.make_tree()
#print(tree.start.points)

assert tree.predict((5,4)) == 1
#print(tree.find_splits())
#print(tree.find_best_split())
#print(tree.entropy())
print('\n\nnew tree\n\n')
points = [{'coord': (2,4), 'type': 1},
        {'coord': (2,3), 'type': 1},
        {'coord': (2,2), 'type': 2},
        {'coord': (2,1), 'type': 2},
        {'coord': (3,4), 'type': 1},
        {'coord': (3,3), 'type': 2},
        {'coord': (3,2), 'type': 2}]

tree = DecisionTree(points)
tree.make_tree()

##Impure non_tie
points = [{'coord': (1,7), 'type': 1},
        {'coord': (2,7), 'type': 1},
        {'coord': (3,7), 'type': 1},
        {'coord': (3,8), 'type': 1},
        {'coord': (3,9), 'type': 1},
        {'coord': (7,1), 'type': 1},
        {'coord': (1,9), 'type': 2},
        {'coord': (5,1), 'type': 2},
        {'coord': (5,2), 'type': 2},
        {'coord': (5,3), 'type': 2},
        {'coord': (6,3), 'type': 2},
        {'coord': (7,3), 'type': 2}]

tree = DecisionTree(points,7)
tree.make_tree()

assert tree.start.best_split == (0,4)

##Impure tie 
points = [{'coord': (1,5), 'type': 1},
        {'coord': (1,4), 'type': 2},
        {'coord': (1,3), 'type': 1},
        {'coord': (2,5), 'type': 1},
        {'coord': (2,4), 'type': 1},
        {'coord': (2,3), 'type': 2}]

tree = DecisionTree(points,5,1)
tree.make_tree()

assert tree.start.best_split == (1,4.5)

points = [{'coord': (0,1), 'type': 1},
        {'coord': (0,1), 'type': 1},
        {'coord': (0,2), 'type': 1},
        {'coord': (0,2), 'type': 1},
        {'coord': (1,1), 'type': 1},
        {'coord': (1,1), 'type': 1},
        {'coord': (1,1), 'type': 2},
        {'coord': (1,2), 'type': 2},
        {'coord': (1,2), 'type': 2},
        {'coord': (1,2), 'type': 2}]

tree = DecisionTree(points, 1, 1)
tree.make_tree()

print(tree.start.children[0].kind)

## Semi Random points
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

rand_folds = [[] for _ in range(10)]
for fold in range(10) :
    for __ in range(int(point_num/10)) :
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

all_acc = [[] for _ in range(int(point_num/2))]

for fold_id in range(10) :
    print(fold_id)
    test_fold = rand_folds[fold_id]
    train_fold = []
    for new_id in range(10) :
        if new_id != fold_id :
            train_fold.extend(rand_folds[new_id])
    for min_split in range(1, int(point_num/2)+1) :
        predictions = []
        tree = DecisionTree(train_fold, min_split)
        tree.make_tree()
        for point in test_fold :
            #print(point['coord'])
            predictions.append(tree.predict(point['coord']))
        all_acc[min_split-1].append(find_accuracy(predictions, test_fold))

avg_acc = []
for acc in all_acc :
    avg_acc.append(sum(acc)/len(acc))

#'''
import matplotlib.pyplot as plt
plt.style.use('bmh')

min_split_val = range(1, int(point_num/2)+1)

plt.plot(min_split_val, avg_acc)

plt.savefig('Fold_Acc.png')
#'''
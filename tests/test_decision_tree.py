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
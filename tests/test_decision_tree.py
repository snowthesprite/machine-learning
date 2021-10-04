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
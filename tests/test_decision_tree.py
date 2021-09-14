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
print(tree.start.points)

print(tree.predict((5,4)))
#print(tree.find_splits())
#print(tree.find_best_split())
#print(tree.entropy())


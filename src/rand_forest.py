from decision_tree import *
import math
import random

class RandForest () :
    def __init__(self, point, num_trees = 1, min_split = 1) : 
        self.points = point
        self.num_trees = num_trees
        self.min_split = min_split
        self.trees = []
        self.types = [1,2]

    def make_forest_1(self) :
        for _ in range(self.num_trees) :
            tree = RandDecisionTree(self.points, self.min_split)
            tree.make_tree()
            self.trees.append(tree)
    
    def make_forest_2(self) :
        for _ in range(self.num_trees) :
            tree = DecisionTree(self.points, self.min_split)
            tree.make_tree()
            self.trees.append(tree)

    def predict(self, point) : 
        count = {kind: [] for kind in self.types} 
        for tree in self.trees : 
            count[tree.predict(point)].append(1)
        max = 0
        best_kind = None
        for kind in self.types :
            amount = sum(count[kind])
            if amount > max :
                max = amount
                best_kind = kind
            elif amount == max :
                choice = math.floor(random.random()*2)
                if choice == 1 :
                    best_kind = kind
        return best_kind
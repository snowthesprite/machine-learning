import math
import random

class SplitNode () :
    def __init__ (self, points, kind=None) :
        self.points = points
        self.children = None
        self.best_split = None
        self.entropy = None
        self.kind = kind
        self.type = None 

class DecisionTree () :
    def __init__(self, all_points, min_size_to_split = 1) :
        self.dim = 2
        self.start = SplitNode(all_points)
        self.min_to_split = min_size_to_split

    def make_tree(self) :
        queue = [self.start]
        while queue != [] :
            node = queue[0]
            queue.pop(0)
            node.entropy = self.find_entropy(node.points)
            if node.entropy == 0 or len(node.points) < self.min_to_split :
                node.type = self.find_node_type(node)
                continue
            split = self.find_best_split(node.points)
            node.best_split = split['split']
            great_node = SplitNode(split['greater'], 'grt' + str(node.best_split))
            less_node = SplitNode(split['lesser'],'less' + str(node.best_split))
            node.children = [great_node, less_node]
            queue.extend([great_node, less_node])

    def find_node_type(self, node) :
        len_1 = sum([1 for point in node.points if point['type'] == 1])
        len_2 = sum([1 for point in node.points if point['type'] == 2])
        if len_1 > len_2 :
            node_type = 1
        elif len_2 > len_1 :
            node_type = 2
        else : 
            node_type = random.randint(1,2)
        return node_type

    def find_entropy(self, points) :
        len_1 = sum([1 for point in points if point['type'] == 1])
        len_2 = sum([1 for point in points if point['type'] == 2])
        p_1 = len_1/(len_1 + len_2)
        p_2 = len_2/(len_1 + len_2)
        if p_1 == 0 or p_2 == 0 :
            return 0
        return -p_1 * math.log(p_1) - p_2 * math.log(p_2)
        

    def find_splits(self, points) :
        splits = [set([]) for _ in range(self.dim)]
        for index_1 in range(len(points)) :
            point_1 = points[index_1]['coord']
            for index_2 in range(len(points)) : 
                point_2 = points[index_2]['coord']
                for axis in range(self.dim) :
                    if point_1[axis] == point_2[axis] :
                        continue
                    splits[axis].add((point_1[axis]+point_2[axis])/2)
        return splits
    
    def find_best_split(self, points) :
        splits = self.find_splits(points)
        best_split = {}
        best_avg_entropy = 1
        for axis in range(self.dim) :
            for split in splits[axis] :
                greater = [point for point in points if point['coord'][axis] >= split]
                lesser = [point for point in points if point['coord'][axis] < split]
                g_entropy = self.find_entropy(greater)
                l_entropy = self.find_entropy(lesser)
                avg_entropy = len(greater)/len(points) * g_entropy + len(lesser)/len(points) *l_entropy
                if avg_entropy < best_avg_entropy :
                    best_avg_entropy = avg_entropy
                    best_split['split'] = (axis, split)
                    best_split['greater'] = greater
                    best_split['lesser'] = lesser
        return best_split

    def predict(self, coord) :
        current_node = self.start
        while True :
            if current_node.type != None :
                return current_node.type
            axis,split = current_node.best_split
            if coord[axis] >= split : 
                current_node = current_node.children[0]
            else :
                current_node = current_node.children[1]

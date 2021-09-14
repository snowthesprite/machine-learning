import math
class SplitNode () :
    def __init__ (self, points, parent = None, kind=None) :
        self.points = points
        self.parent = parent
        self.children = []
        self.best_split = None
        self.entropy = None
        self.kind = kind

class DecisionTree () :
    def __init__(self, all_points) :
        self.dim = 2
        self.start = SplitNode(all_points)

    def make_tree(self) :
        queue = [self.start]
        while queue != [] :
            node = queue[0]
            node.entropy = self.entropy(node.points)
            print(node.kind)
            print(node.entropy)
            print(node.points)
            if node.entropy == 0 :
                queue.pop(0)
                continue
            split = self.find_best_split(node.points)
            node.best_split = split['split']
            print(split)
            great_node = SplitNode(split['greater'], node, 'grt' + str(node.best_split))
            less_node = SplitNode(split['lesser'], node,'less' + str(node.best_split))
            node.children.extend([great_node, less_node])
            queue.extend([great_node, less_node])
            queue.pop(0)
            print('next node\n')

    def entropy(self, points) :
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
        print('\nbest split\n')
        splits = self.find_splits(points)
        print(splits)
        best_split = {'split' : 0, 'greater' : None, 'lesser' : None}
        best_avg_entropy = 1
        for axis in range(self.dim) :
            for split in splits[axis] :
                greater = [point for point in points if point['coord'][axis] >= split]
                lesser = [point for point in points if point['coord'][axis] < split]
                g_entropy = self.entropy(greater)
                l_entropy = self.entropy(lesser)
                avg_entropy = len(greater)/len(points) * g_entropy + len(lesser)/len(points) *l_entropy
                print(split)
                print(g_entropy)
                print(l_entropy)
                print(avg_entropy)
                print()
                if avg_entropy < best_avg_entropy :
                    best_avg_entropy = avg_entropy
                    best_split['split'] = (axis, split)
                    best_split['greater'] = greater
                    best_split['lesser'] = lesser
        return best_split

    def predict(self, coord) :
        point_type = None
        current_node = self.start
        while point_type == None :
            if current_node.entropy == 0 :
                point_type = current_node.points[0]['type']
                break
            axis,split = current_node.best_split
            if coord[axis] >= split : 
                current_node = current_node.children[0]
            else :
                current_node = current_node.children[1]
        return point_type

class Node (): 
    def __init__(self, id, act_funct) :
        self.id = id
        self.parents = []
        self.act_funct = act_funct
        self.value = None
    
    def output(self, input = None, funct = None) :
        if funct == None :
            funct = self.act_funct
        if input == None :
            return (lambda x : funct(self.value(x)))
        return funct(self.value(input))

    def set_value(self, value) : 
        self.value = lambda x : sum(value(self.parents, self.id, x))

'''
class NeuralNet (): 
    def __init__(self, layers, weights, act_funct, data = None, mutation_rate = 0, premade = False) :
        self.nodes = layers
        self.weights = weights
        self.data = data
        self.mut_rate = mutation_rate
        if not premade :
            self.nodes = {}
            self.weights = {}
            self.create_net(layers, weights, act_funct)

    def create_net(self, layers, weights, act_funct) :
        id = 0
        for layer in range(len(layers)) :
            node_order = 0
            self.nodes[layer] = []
            for node in layers[layer] :
                #print(layer, node)
                id += 1
                new_node = Node(id, act_funct)
                if node == 'bias' : 
                    new_node.value = lambda x : 1
                    self.nodes[layer].append(new_node)
                    #print()
                    continue
                if layer == 0 :
                    new_node.value = lambda x : x
                    self.nodes[layer].append(new_node)
                    #print()
                    continue
                #print(id)
                new_node.parents = self.make_node_specifics(layer, weights, node_order, id)
                new_node.set_value(lambda parents, id, x : [self.weights[(parent.id, id)] * parent.output()(x) for parent in parents])
                self.nodes[layer].append(new_node)
                
    def make_node_specifics(self, layer, weights, node_order, id) :
        from_node = []
        for prev_node_order in range(len(self.nodes[layer-1])) :
            prev_node = self.nodes[layer-1][prev_node_order]
            from_node.append(prev_node)
            self.weights[(prev_node.id, id)] = weights[layer-1][prev_node_order][node_order] 
        return from_node
    
    def calc_ans(self, input) :
        culmunate = self.nodes[len(self.nodes)-1][0]
        return culmunate.output(input)

    ## RSS is a thing that exists and is, in fact, what you are taking the derivative of. 
    ## Not... whatever you were thinking

    def calc_rss(self) :
        rss = 0
        for point in self.data :
            rss += (point[1] - self.calc_ans(point[0])) ** 2
        return rss
'''

class NeuralNet (): 
    def __init__(self, nodes, weights, act_funct, data, mutation_rate = 0, premade = False) :
        self.nodes = nodes
        self.data = data
        self.mut_rate = mutation_rate
        if not premade :
            self.weights = self.create_weights(weights)
        else :
            self.weights = weights
    
    def calc_ans(self, input) :
        culmunate = self.nodes[len(self.nodes)-1][0]
        return culmunate.output(input)

    ## RSS is a thing that exists and is, in fact, what you are taking the derivative of. 
    ## Not... whatever you were thinking

    def calc_rss(self) :
        rss = 0
        for point in self.data :
            rss += (point[1] - self.calc_ans(point[0])) ** 2
        return rss

    def make_weights() :
        weights = {}
        for layer in range(1, len(self.nodes)) :
            for node in self.nodes[layer] :

            cur_amnt = node_num[layer_num] + 1
            if layer_num == len(node_num) - 1 :
                cur_amnt -= 1
            prev_amnt = node_num[layer_num -1 ] + 1
            weights[layer_num-1] = [[rand.uniform(-2, 2)/10 for _ in range(cur_amnt)] for __ in range(prev_amnt)]
        return weights


class NeuralNetField (): 
    def __init__(self, layers, act_funct, data, amount) :
        self.nodes = {}
        self.data = self.normalize_data(data)
        self.create_nodes(layers, act_funct)
        self.nets = {}

    def create_nodes(self, node_layers, weights, act_funct) :
        layers = self.create_layers(node_layers)
        id = 0
        for layer in range(len(layers)) :
            node_order = 0
            self.nodes[layer] = []
            for node in layers[layer] :
                #print(layer, node)
                id += 1
                new_node = Node(id, act_funct)
                if node == 'bias' : 
                    new_node.value = lambda x : 1
                    self.nodes[layer].append(new_node)
                    #print()
                    continue
                if layer == 0 :
                    new_node.value = lambda x : x
                    self.nodes[layer].append(new_node)
                    #print()
                    continue
                #print(id)
                new_node.parents = self.make_node_specifics(layer, node_order, id)
                new_node.set_value(lambda parents, id, x : [self.weights[(parent.id, id)] * parent.output()(x) for parent in parents])
                self.nodes[layer].append(new_node)
                
    def make_node_specifics(self, layer, weights, node_order, id) :
        from_node = []
        for prev_node_order in range(len(self.nodes[layer-1])) :
            prev_node = self.nodes[layer-1][prev_node_order]
            from_node.append(prev_node)
        return from_node

    def normalize_data(data) : 
        x_data = [x for (x,y) in data]
        y_data = [y for (x,y) in data]

        x_min_max = (min(x_data), max(x_data))
        y_min_max = (min(y_data), max(y_data))

        normalized = []

        for (x,y) in data :
            norm_x = (x-x_min_max[0])/(x_min_max[1] - x_min_max[0])
            norm_y = (y-y_min_max[0])/(y_min_max[1] - y_min_max[0])
            normalized.append((norm_x, 2*norm_y-1))
        return normalized
    
    def create_layers(node_layers) :
        net_set = []
        for layer_num in range(len(node_num)) :
            if layer_num != 0 :
                net_set[layer_num - 1].append('bias')
            net_set.append([node for node in range(node_num[layer_num])])
        return net_set

    def make_weights() :
        weights = {}
        for layer_num in range(1, len(node_num)) :
            cur_amnt = node_num[layer_num] + 1
            if layer_num == len(node_num) - 1 :
                cur_amnt -= 1
            prev_amnt = node_num[layer_num -1 ] + 1
            weights[layer_num-1] = [[rand.uniform(-2, 2)/10 for _ in range(cur_amnt)] for __ in range(prev_amnt)]
        return weights
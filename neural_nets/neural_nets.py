from numpy.random import normal
import random as rand
import math

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
    def __init__(self, nodes, weights, data, mutation_rate = 0, premade = False) :
        self.nodes = nodes
        self.data = data
        self.mut_rate = mutation_rate
        if not premade :
            self.weights = self.create_weights()
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

    def make_weights(self) :
        weights = {}
        for layer in range(len(self.nodes)-1) :
            for node_from in self.nodes[layer] :
                for node_to in self.nodes[layer+1] :
                    weights[(node_from.id, node_to.id)] = rand.uniform(-2, 2)/10
        return weights


class NeuralNetField (): 
    def __init__(self, layers, act_funct, data, amount) :
        self.nodes = {}
        self.data = self.normalize_data(data)

        self.create_nodes(layers, act_funct)

        self.num_weights = 111
        self.first_gen = []
        self.curr_gen = []

        self.create_gen(amount)

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

    def normalize_data(self, data) : 
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
    
    def create_layers(self, node_layers) :
        net_set = []
        for layer_num in range(len(node_num)) :
            if layer_num != 0 :
                net_set[layer_num - 1].append('bias')
            net_set.append([node for node in range(node_num[layer_num])])
        return net_set

    def find_lowest_rss(self, amount, field) :
        rss_count = []
        for net_id in range(len(field)) :
            rss_count.append((net_id, field[net_id].calc_rss()))
        rss_count.sort(key=(lambda x: x[1]))
        return rss_count[:amount]

    def reproduce(self, parent, amount=1) :
        children_data = [{'weights': {}, 'mutate': 0} for num in range(amount)]
        for child_id in range(amount) :
            child = children_data[child_id]
            for (connect, weight) in parent.weights.items() :
                child['weights'][connect] = weight * parent.mut_rate * normal(0,1)
            child['mutate'] = parent.mut_rate ** (normal(0,1) / (2**(1/2) * weight_amount ** (1/4)))
        return children_data

    def evolve(self, gens) :
        rss_gen_avg = {}
        for gen in range(gens) :
            gen_avg = [net.calc_rss() for net in self.curr_gen]
            rss_gen_avg[gen] = sum(gen_avg) / len(gen_avg)
            next_gen = [self.curr_gen[net_id] for (net_id, rss) in self.find_lowest_rss(15, self.curr_gen)]
            children = []
            for parent in next_gen :
                child = self.reproduce(parent)
                #print(child)
                child = [NeuralNet(self.nodes, kid['weights'], self.data, kid['mutate'], True) for kid in child]
                children.extend(child)
            next_gen.extend(children)
            self.curr_gen = next_gen
        return rss_gen_avg

    def create_gen(self, amount) :
        for _ in range(amount) :
            net = NeuralNet(self.nodes, None, self.data, 0.5)
            self.curr_gen.append(net)
            self.first_gen.append(net)
    
'''def make_weights() :
        weights = {}
        for layer_num in range(1, len(node_num)) :
            cur_amnt = node_num[layer_num] + 1
            if layer_num == len(node_num) - 1 :
                cur_amnt -= 1
            prev_amnt = node_num[layer_num -1 ] + 1
            weights[(node_from)] = [[rand.uniform(-2, 2)/10 for _ in range(cur_amnt)] for __ in range(prev_amnt)]
        return weights
'''
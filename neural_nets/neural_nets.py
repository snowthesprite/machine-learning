from numpy.random import normal, uniform
import math

'''
class Node (): 
    def __init__(self, id, act_funct) :
        self.id = id
        self.parents = []
        self.act_funct = act_funct
        #self.parts = lambda net, parents, id, x : [net.weights[(parent.id, self.id)] * parent.output(net,x) for parent in self.parents]
        #self.value = lambda net, x : sum(self.parts(net, self.parents, self.id, x))
        self.value = None
    
    def output(self, input = None) :
        #if input == None :
            #return lambda x : self.act_funct(self.value(net, x))
            #return (lambda x : self.value(x))
        return self.act_funct(self.value(input))
        
    def set_value(self, value) : 
        self.value = (lambda x : sum(value(self.parents, self.id, x)))

class NeuralNet (): 
    def __init__(self, layers, weights, act_funct, data, mutation_rate = 0, premade = False) :
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
                new_node.set_value(lambda parents, id, x : [self.weights[(parent.id, id)] * parent.output(x) for parent in parents])
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
#'''

#'''
class Node (): 
    def __init__(self, id, act_funct) :
        self.id = id
        self.parents = []
        self.act_funct = act_funct
        self.value = lambda weights, x : sum([weights[(parent.id, self.id)] * parent.output(weights,x) for parent in self.parents])
    
    def output(self, weights, input) :
        return self.act_funct(self.value(weights, input))

class NeuralNet (): 
    def __init__(self, nodes, weights, data, mutation_rate = 0, premade = False) :
        self.nodes = nodes
        self.data = data
        self.mut_rate = mutation_rate
        if not premade :
            self.weights = self.make_weights()
        else :
            self.weights = weights
    
    def calc_ans(self, input) :
        culmunate = self.nodes[len(self.nodes)-1][0]
        return culmunate.output(self.weights, input)

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
                    weights[(node_from.id, node_to.id)] = uniform(-0.2, 0.2)
        return weights

class NeuralNetField (): 
    def __init__(self, layers, act_funct, data, amount) :
        self.nodes = {}
        self.data = self.normalize_data(data)

        self.create_nodes(layers, act_funct)

        self.num_weights = 111
        self.curr_gen = []

        self.create_gen(amount)

    def create_nodes(self, node_layers, act_funct) :
        layers = self.create_layers(node_layers)
        id = 0
        for layer in range(len(layers)) :
            node_order = 0
            self.nodes[layer] = []
            for node in layers[layer] :
                id += 1
                new_node = Node(id, act_funct)
                if node == 'bias' : 
                    new_node.value = lambda weights, x : 1
                    self.nodes[layer].append(new_node)
                    continue
                if layer == 0 :
                    new_node.value = lambda weights, x : x
                    self.nodes[layer].append(new_node)
                    continue
                new_node.parents = self.make_node_specifics(layer, node_order, id)
                self.nodes[layer].append(new_node)
                
    def make_node_specifics(self, layer, node_order, id) :
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
        for layer_num in range(len(node_layers)) :
            if layer_num != 0 :
                net_set[layer_num - 1].append('bias')
            net_set.append([node for node in range(node_layers[layer_num])])
        return net_set

    def find_lowest_rss(self, amount, field) :
        rss_count = []
        for net_id in range(len(field)) :
            rss_count.append((net_id, field[net_id].calc_rss()))
        rss_count.sort(key=(lambda x: x[1]))
        return rss_count[:amount]

    def reproduce(self, parent, amount=1) :
        child = {'weights': {}, 'mutate': 0}
        for (connect, weight) in parent.weights.items() :
            child['weights'][connect] = weight + parent.mut_rate * normal()
        child['mutate'] = parent.mut_rate * math.exp(normal() / (2**(1/2) * self.num_weights ** (1/4)))

        return child

    def evolve(self, gens) :
        rss_gen_avg = {}
        for gen in range(gens) :
            if gen % 100 == 0 :
                print(gen)
            gen_avg = [net.calc_rss() for net in self.curr_gen]
            rss_gen_avg[gen] = sum(gen_avg) / len(gen_avg)

            self.curr_gen.sort(key=(lambda x: x.calc_rss()))
            for id in range(0, 15) :
                child = self.reproduce(self.curr_gen[id])
                self.curr_gen[id+15].weights = child['weights']
                self.curr_gen[id+15].mut_rate = child['mutate']
        return rss_gen_avg
        
    def calc_ans(self, input) :
        return [net.calc_ans(input) for net in self.curr_gen]

    def create_gen(self, amount) :
        for _ in range(amount) :
            net = NeuralNet(self.nodes, None, self.data, 0.05)
            self.curr_gen.append(net)
#'''
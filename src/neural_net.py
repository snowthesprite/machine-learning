def funct_sum (functions, input) :
    sum = 0
    for funct in functions :
        sum += funct(input)
    return sum

class Node (): 
    def __init__(self, id, act_funct) :
        self.id = id
        self.parents = None
        self.act_funct = act_funct
        self.value = None
    
    def output(self, input = None) :
        if input == None :
            return (lambda x : self.act_funct(self.value(x)))
        return self.act_funct(self.value(input))

class NeuralNet (): 
    def __init__(self, neural_net, act_funct) :
        self.nodes = {}
        self.weights = {}
        self.create_net(neural_net, act_funct)

    def create_net(self, neural_net, act_funct) :
        id = 0
        for layer in range(len(neural_net)) :
            node_order = 0
            self.nodes[layer] = []
            for node in neural_net[layer]['nodes'] :
                print(layer, node)
                id += 1
                new_node = Node(id, act_funct)
                if node == 'bias' : 
                    new_node.value = lambda x : 1
                    self.nodes[layer].append(new_node)
                    continue
                if layer == 0 :
                    new_node.value = lambda x : x
                    self.nodes[layer].append(new_node)
                    continue
                new_node.value = self.make_node_value(neural_net, layer, node_order, id)
                self.nodes[layer].append(new_node)
                
    def make_node_value(self, neural_net, layer, node_order, id) :
        node_elements = []
        for prev_node_order in range(len(self.nodes[layer-1])) :
            prev_node = self.nodes[layer-1][prev_node_order]
            self.weights[(prev_node.id, id)] = neural_net[layer-1]['weights'][prev_node_order][node_order] 
            node_elements.append((lambda x : self.weights[(prev_node.id, id)] * prev_node.output()(x)))
        return (lambda x : funct_sum(node_elements, x))
    
    def calc_answer(self, input) :
        culmunate = self.nodes[len(self.nodes)-1][0]
        return culmunate.output(input)
                
                
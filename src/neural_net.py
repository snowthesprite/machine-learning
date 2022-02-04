def funct_sum (functions, input) :
    sum = 0
    print('run')
    for funct in functions :
        #print(funct(input))
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
                    print()
                    continue
                if layer == 0 :
                    new_node.value = lambda x : x
                    self.nodes[layer].append(new_node)
                    print()
                    continue
                print(id)
                new_node.value = self.make_node_value(neural_net, layer, node_order, id)
                self.nodes[layer].append(new_node)
                
    def make_node_value(self, neural_net, layer, node_order, id) :
        node_elements = []
        from_node = []
        print('layer', layer-1, len(self.nodes[layer-1]))
        for prev_node_order in range(len(self.nodes[layer-1])) :
            prev_node = self.nodes[layer-1][prev_node_order]
            from_node.append(prev_node)
            print('id', prev_node.id, prev_node.output()(2))
            self.weights[(prev_node.id, id)] = neural_net[layer-1]['weights'][prev_node_order][node_order] 
            #node_elements.append((lambda x : self.weights[(prev_node.id, id)] * prev_node.output()(x)))
            print('_',(lambda x : prev_node.output()(x))(2))
            node_elements.append(lambda x : prev_node.output()(x))

        print([node_element(2) for node_element in node_elements])
        #print([node_element(1) for node_element in node_elements])
        print()
        return (lambda x : funct_sum(node_elements, x))
    
    def calc_answer(self, input) :
        culmunate = self.nodes[len(self.nodes)-1][0]
        return culmunate.output(input)
                
                
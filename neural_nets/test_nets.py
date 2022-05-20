from neural_nets import *
from numpy.random import normal
import random as rand
import math

data = [(0.0, 7), (0.2, 5.6), (0.4, 3.56), (0.6, 1.23), (0.8, -1.03),
        (1.0, -2.89), (1.2, -4.06), (1.4, -4.39), (1.6, -3.88), (1.8, -2.64),
        (2.0, -0.92), (2.2, 0.95), (2.4, 2.63), (2.6, 3.79), (2.8, 4.22),
        (3.0, 3.8), (3.2, 2.56), (3.4, 0.68), (3.6, -1.58), (3.8, -3.84),
        (4.0, -5.76), (4.2, -7.01), (4.4, -7.38), (4.6, -6.76), (4.8, -5.22)]

#'''
x_data = [x for (x,y) in data]
y_data = [y for (x,y) in data]

x_min_max = (min(x_data), max(x_data))
y_min_max = (min(y_data), max(y_data))

normalized = []

for (x,y) in data :
    norm_x = (x-x_min_max[0])/(x_min_max[1] - x_min_max[0])
    norm_y = (y-y_min_max[0])/(y_min_max[1] - y_min_max[0])
    normalized.append((norm_x, 2*norm_y-1))
#'''
node_num = [1, 10, 6, 3, 1]
#'''
net_set = []

for layer_num in range(len(node_num)) :
    if layer_num != 0 :
        net_set[layer_num - 1].append('bias')
    net_set.append([node for node in range(node_num[layer_num])])

def make_weights() :
    weights = {}
    for layer_num in range(1, len(node_num)) :
        cur_amnt = node_num[layer_num] + 1
        if layer_num == len(node_num) - 1 :
            cur_amnt -= 1
        prev_amnt = node_num[layer_num -1 ] + 1
        weights[layer_num-1] = [[rand.uniform(-2, 2)/10 for _ in range(cur_amnt)] for __ in range(prev_amnt)]
    return weights
#'''
act_funct = (lambda x: (math.e**x - math.e ** (-x)) / (math.e**x + math.e ** (-x)))
#act_funct = lambda x : x

net_field = [NeuralNet(net_set, make_weights(), act_funct, normalized.copy(), 0.05) for _ in range(30)]
#net_field = NeuralNetField(node_num, act_funct, data, 30)

#'''
def find_lowest_rss(amount, field) :
    rss_count = []
    for net_id in range(len(field)) :
        rss_count.append((net_id, field[net_id].calc_rss()))
    rss_count.sort(key=(lambda x: x[1]))
    return rss_count[:amount]

weight_amount = 111

def reproduce(parent, amount=1) :
    children_data = [{'nodes': parent.nodes, 'weights': {}, 'mutate': 0} for num in range(amount)]
    for child_id in range(amount) :
        child = children_data[child_id]
        for (connect, weight) in parent.weights.items() :
            child['weights'][connect] = weight * parent.mut_rate * normal(0,1)
        child['mutate'] = parent.mut_rate ** (normal(0,1) / (2**(1/2) * weight_amount ** (1/4)))
    return children_data
    


rss_gen_avg = {}

current_generation = net_field.copy()

for gen in range (100) :
    print(gen)
    gen_avg = [net.calc_rss() for net in current_generation]
    rss_gen_avg[gen] = sum(gen_avg) / len(gen_avg)
    next_gen = [current_generation[net_id] for (net_id, rss) in find_lowest_rss(15, current_generation)]
    children = []
    for parent in next_gen :
        child = reproduce(parent)
        #print(child)
        child = [NeuralNet(kid['nodes'], kid['weights'], act_funct, normalized.copy(), kid['mutate'], True) for kid in child]
        children.extend(child)
    next_gen.extend(children)
    current_generation = next_gen
'''
rss_gen_avg = net_field.evolve(100)

#'''
import matplotlib.pyplot as plt
plt.style.use('bmh')
x_axis = []
y_axis = []

for (gen, rss) in rss_gen_avg.items() :
    x_axis.append(gen)
    y_axis.append(rss)

plt.plot(x_axis, y_axis)

plt.savefig('neural_nets/evolving.png')
#'''
import sys
sys.path.append('src')
from neural_net import *

neural_net_set = [
    {'nodes' : [1],
    'weights' : [[1,1],[1,1]]},
    {'nodes' : [3, 4, 'bias'],
    'weights' : [[1],[1], [1]]},
    {'nodes' : [5, 'bias'],
    'weights' : [[1],[1]]},
    {'nodes' : [7],
    'weights' : []}]
''''
neural_net_set = [
    {'nodes' : [1, 'bias'],
    'weights' : [[1,1],[1,1]]},
    {'nodes' : [3, 4, 'bias'],
    'weights' : [[1],[1],[1]]},
    {'nodes' : [6],
    'weights' : [[1]]},
    {'nodes' : [7],
    'weights' : []}]
'''

finished_net = NeuralNet(neural_net_set, (lambda x: x))

print()
print(finished_net.nodes[2][0].output(1))
print()

print(finished_net.calc_answer(2))

finished_net.weights[(6,7)] = 2

#print(finished_net.calc_answer(1))
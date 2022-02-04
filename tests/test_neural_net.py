import sys
sys.path.append('src')
from neural_net import *

neural_net_set = [
    {'nodes' : [1, 'bias'],
    'weights' : [[1,1],[1,1]]},
    {'nodes' : [3, 4],
    'weights' : [[1],[1]]},
    {'nodes' : [5],
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

finished_net = NeuralNet(neural_net_set, (lambda x: 2*x))

print(finished_net.nodes[1][0].output(1))

print(finished_net.calc_answer(1))

finished_net.weights[(6,7)] = 2

print(finished_net.calc_answer(1))
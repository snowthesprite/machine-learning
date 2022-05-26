from neural_nets import *
import matplotlib.pyplot as plt
plt.style.use('bmh')

data = [(0.0, 7), (0.2, 5.6), (0.4, 3.56), (0.6, 1.23), (0.8, -1.03),
        (1.0, -2.89), (1.2, -4.06), (1.4, -4.39), (1.6, -3.88), (1.8, -2.64),
        (2.0, -0.92), (2.2, 0.95), (2.4, 2.63), (2.6, 3.79), (2.8, 4.22),
        (3.0, 3.8), (3.2, 2.56), (3.4, 0.68), (3.6, -1.58), (3.8, -3.84),
        (4.0, -5.76), (4.2, -7.01), (4.4, -7.38), (4.6, -6.76), (4.8, -5.22)]

#'''
node_num = [1, 10, 6, 3, 1]

##act_funct = (lambda x: ((math.e**x) - (math.e ** (-x))) / ((math.e**x) + (math.e ** (-x))))
act_funct = lambda x: math.tanh(x)

net_field = NeuralNetField(node_num, act_funct, data, 30)

x_axis = [point[0] for point in net_field.data]
y_axis = [point[1] for point in net_field.data]

plt.scatter(x_axis, y_axis)

for net in net_field.curr_gen :
    plt.plot(x_axis, [net.calc_ans(x) for x in x_axis], 'g-')


rss_gen_avg = net_field.evolve(2000)
#print(rss_gen_avg)
#'''
#'''

for net in net_field.curr_gen : 
    plt.plot(x_axis, [net.calc_ans(x) for x in x_axis], 'r-')

plt.savefig('neural_nets/change.png')
#'''

plt.clf()


x_axis = []
y_axis = []

for (gen, rss) in rss_gen_avg.items() :
    x_axis.append(gen)
    y_axis.append(rss)

plt.plot(x_axis, y_axis)

plt.savefig('neural_nets/evolving.png')

#'''

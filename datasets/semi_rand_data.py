import random

#random.seed(1)
centers = {1 : [(1,1), (4,4)], 2: [(1,4), (4,1)]}
points = []

for kind in range(1,3) :
    for num in range(100) :
        center = centers[kind][round(random.random())]
        point = []
        for axis in range(2) :
            sign = [1,-1][round(random.random())]
            point.append(center[axis] + random.random()*sign* num/25)
        points.append({'coord': point, 'type': kind})



import matplotlib.pyplot as plt
plt.style.use('bmh')

kind = ['b+', 'r+']
plt.plot(1,1, 'mo')
plt.plot(4,4, 'mo')
plt.plot(1,4, 'mo')
plt.plot(4,1, 'mo')
for point_info in points :
    plt.plot(point_info['coord'][0], point_info['coord'][1], kind[point_info['type']-1])


plt.savefig('datasets/test_set.png')
#'''
import sys
sys.path.append('src')
from dataframe import DataFrame
from logistic_regressor import LogisticRegressor
''''
df = DataFrame.from_array(
    [[1,0],
    [2,0],
    [3,0],
    [2,1],
    [3,1],
    [4,1]],
    columns = ['x', 'y'])

alpha = 0.01
delta = 0.01
num_steps = 20000

reg = LogisticRegressor(df, dependent_variable='y', premade = True)

reg.set_coefficients({'constant': 0.5, 'x': 0.5})

print(reg.calc_rss())
print(reg.calc_gradient(delta))
reg.gradient_descent(alpha, delta, num_steps)
print(reg.coefficients)
'''
df = DataFrame.from_array(
    [[2,1],
    [3,0]],
    columns = ['x', 'y'])

alpha = 0.2
delta = 0.1
num_steps = 20000

reg = LogisticRegressor(df, dependent_variable='y', premade = True)

reg.set_coefficients({'constant': 1, 'x': 1})

print(reg.calc_rss())
print(reg.calc_gradient(delta))
#reg.gradient_descent(alpha, delta, num_steps)
#print(reg.coefficients)

''''
import matplotlib.pyplot as plt
plt.style.use('bmh')

points = {'x': [], 'y': []}

x = -5

while x <= 10 :
    points['x'].append(x)

    points['y'].append(reg.predict({'x': x}))
    x+=0.1


plt.plot(points['x'],points['y'])

plt.plot([1, 2, 3, 2, 3, 4], [0, 0, 0, 1, 1, 1], 'ro')

plt.legend(['0.1','data'])

plt.xlabel('x')
plt.ylabel('Prediction')
plt.title('Gradient Descent')
plt.savefig('new_log_regress.png')
#'''
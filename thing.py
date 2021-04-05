import sys
sys.path.append('src')
from dataframe import DataFrame
from log_regress import LogisticRegressor

df = DataFrame.from_array(
    [[1,0],
    [2,0],
    [3,0],
    [2,1],
    [3,1],
    [4,1]],
    columns = ['x', 'y'])

log_reg1 = LogisticRegressor(df,dependent_variable = 'y', change = 0.1)

log_reg2 = LogisticRegressor(df,dependent_variable = 'y', change = 0.01)

#''''
log_reg3 = LogisticRegressor(df,dependent_variable = 'y', change = 0.001)

log_reg4 = LogisticRegressor(df,dependent_variable = 'y', change = 0.0001)

import matplotlib.pyplot as plt
plt.style.use('bmh')

points = {'x': [], 'y1': [], 'y2': [], 'y3': [], 'y4': []}

x = -5

while x <= 10 :
    points['x'].append(x)

    points['y1'].append(log_reg1.predict({'x': x}))

    points['y2'].append(log_reg2.predict({'x': x}))

    points['y3'].append(log_reg3.predict({'x': x}))

    points['y4'].append(log_reg4.predict({'x': x}))
    x+=0.1

plt.plot(points['x'],points['y1'])
plt.plot(points['x'],points['y2'])
plt.plot(points['x'],points['y3'])
plt.plot(points['x'],points['y4'])

plt.plot([1, 2, 3, 2, 3, 4], [0, 0, 0, 1, 1, 1], 'ro')

plt.legend(['0.1','0.01','0.001', '0.0001', 'data'])

plt.xlabel('x')
plt.ylabel('Prediction')
plt.title('Differences between Logistic Regressors')
plt.savefig('plot.png')


#'''
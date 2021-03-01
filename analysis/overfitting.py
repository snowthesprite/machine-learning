import sys
sys.path.append('src')
from poly_regressor import PolynomialRegressor
from dataframe import DataFrame

data = [(-4, 11.0),
 (-2, 5.0),
 (0, 3.0),
 (2, 5.0),
 (4, 11.1),
 (6, 21.1),
 (8, 35.1),
 (10, 52.8),
 (12, 74.8),
 (14, 101.2)]
 
training_data = [data[index] for index in range(len(data)) if index % 2 == 0]
testing_data = [data[index] for index in range(len(data)) if index % 2 == 1]

#testing_data = [data[index] for index in range(len(data)) if index % 2 == 0]
#training_data = [data[index] for index in range(len(data)) if index % 2 == 1]

df = DataFrame.from_array(training_data, ['x', 'y'])

linear = PolynomialRegressor(1)
linear.fit(df, 'y')

quad = PolynomialRegressor(2)
quad.fit(df, 'y')

cube = PolynomialRegressor(3)
cube.fit(df, 'y')

quart = PolynomialRegressor(4)
quart.fit(df, 'y')

def find_RSS(given_data, regressor) :
    sum = 0
    for (x, y) in given_data :
        predicted_y = regressor.predict({'x' : x})
        #print(predicted_y, y)
        #print(sum, y - predicted_y, (y - predicted_y) ** 2, "\n")
        sum += (y - predicted_y) ** 2
    return sum
#''''
print('Linear')
print('Training RSS:', find_RSS(training_data, linear))
print('Testing RSS:', find_RSS(testing_data, linear), "\n")

print('Quadratic')
print('Training RSS:', find_RSS(training_data, quad))
print('Testing RSS:', find_RSS(testing_data, quad), "\n")

print('Cubic')
print('Training RSS:', find_RSS(training_data, cube))
print('Testing RSS:', find_RSS(testing_data, cube), "\n")

print('Quartic')
print('Training RSS:', find_RSS(training_data, quart))
print('Testing RSS:', find_RSS(testing_data, quart), "\n")

'''
import matplotlib.pyplot as plt
plt.style.use('bmh')

x_points = []
linear_points = []
quad_points = []
cube_points = []
quart_points = []

for x in range(-4,15) :
    data_dict = {'x' : x}
    x_points.append(x)
    linear_points.append(linear.predict(data_dict))
    quad_points.append(quad.predict(data_dict))
    cube_points.append(cube.predict(data_dict))
    quart_points.append(quart.predict(data_dict))

plt.plot(x_points, linear_points)
plt.plot(x_points, quad_points)
plt.plot(x_points, cube_points)
plt.plot(x_points, quart_points)
plt.scatter([x for (x,y) in data], [y for (x,y) in data], color = 'black')

plt.legend(['Linear', 'Quadratic', 'Cubic', 'Quartic', 'Orign Data'])
plt.savefig('analysis/overfitting.png')
#'''
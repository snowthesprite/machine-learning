import sys
sys.path.append('src')
from poly_regressor import PolynomialRegressor
from dataframe import DataFrame

data = [(1, 3.1), (2, 10.17), (3, 20.93), (4, 38.71), (5, 60.91), (6, 98.87), (7, 113.92), (8, 146.95), (9, 190.09), (10, 232.65)]

df = DataFrame.from_array(data, ['time', 'distance'])

quad_regressor = PolynomialRegressor(2)

cube_regressor = PolynomialRegressor(3)

quad_regressor.fit(df, 'distance')

cube_regressor.fit(df, 'distance')

print('Quad Regressor')
print(quad_regressor.coefficients)
print('5 seconds:', quad_regressor.predict({'time' : 5}))
print('10 seconds:', quad_regressor.predict({'time' : 10}))
print('200 seconds:', quad_regressor.predict({'time' : 200}), "\n")

print('Cube Regressor')
print(cube_regressor.coefficients)
print('5 seconds:', cube_regressor.predict({'time' : 5}))
print('10 seconds:', cube_regressor.predict({'time' : 10}))
print('200 seconds:', cube_regressor.predict({'time' : 200}), "\n")
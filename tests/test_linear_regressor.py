import sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor

''''
Eh I'll fix this stuff later, it'll throw up errors right now

df = DataFrame.from_array([[1,0.2], [2,0.25], [3,0.5]], columns = ['hours worked', 'progress'])

regressor = LinearRegressor(df, dependent_variable='progress')

print('Does all the linear_regressor stuff work')

assert regressor.coefficients == [0.01667, 0.15], 'No, coefficients does not work'

assert regressor.predict({'hours worked': 4}) == 0.61667, 'No, predict does not work'

print('Yes they do', "\n")
'''

df = DataFrame.from_array([[0, 0, 0.1], [1, 0, 0.2], [0, 2, 0.5], [4,5,0.6]], columns = ['scoops of chocolate', 'scoops of vanilla', 'taste rating'])

regressor = LinearRegressor(df, dependent_variable = 'taste rating')

print('Does all the linear_regressor stuff work')

reg_coeff = regressor.coefficients.copy()
for (key, value) in reg_coeff.items() :
    reg_coeff[key] = round(value,8)

assert reg_coeff == {'constant': 0.19252336, 'scoops of chocolate': -0.05981308, 'scoops of vanilla': 0.13271028}, 'No, coefficients does not work'

assert round(regressor.predict({'scoops of chocolate': 2, 'scoops of vanilla': 3}), 8) == 0.47102804, 'No, predict does not work'

print('Yes they do', "\n")

df = DataFrame.from_array(
    [[0, 0, 1], 
    [1, 0, 2], 
    [2, 0, 4], 
    [4, 0, 8], 
    [6, 0, 9], 
    [0, 2, 2], 
    [0, 4, 5], 
    [0, 6, 7], 
    [0, 8, 6],
    [2, 2, 0],
    [3, 4, 0]],
    columns = ['beef', 'pb', 'rating']
)

df = df.create_interaction_terms('beef', 'pb')

assert df.columns == ['beef', 'pb', 'rating', 'beef * pb']
assert df.to_array() == [[0, 0, 1, 0],  [1, 0, 2, 0],  [2, 0, 4, 0],  [4, 0, 8, 0],  [6, 0, 9, 0],  [0, 2, 2, 0],  [0, 4, 5, 0],  [0, 6, 7, 0],  [0, 8, 6, 0], [2, 2, 0, 4], [3, 4, 0, 12]]

regressor = LinearRegressor(df, 'rating')
print(regressor.coefficients)
print(regressor.predict({'beef' : 5, 'pb' : 5, 'beef * pb' : 25}))
print(regressor.predict({'beef' : 5, 'pb' : 0}))

print()
import sys
sys.path.append('src')
from dataframe import DataFrame
from logistic_regressor import LogisticRegressor

df = DataFrame.from_array(
    [[1,0.2],
     [2,0.25],
     [3,0.5]],
    columns = ['x','y']
)

log_reg = LogisticRegressor(df, dependent_variable = 'y', upper_bound = 1)

print('Does our new Logistic Regressor work?')
assert round(log_reg.predict({'x': 5}), 3) == 0.777, 'No, it doesnt'
print('Yes, it does', "\n")

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

regressor = LogisticRegressor(df, 'rating', 10)
print('Coefficients:', regressor.coefficients)
print('Beef: 5, Pb: 0, Rating:', regressor.predict({'beef' : 5, 'pb' : 0}))
print('Beef: 12, Pb: 0, Rating:', regressor.predict({'beef' : 12, 'pb' : 0}))
print('Beef: 5, Pb: 5, Rating:', regressor.predict({'beef' : 5, 'pb' : 5, 'beef * pb' : 25}), "\n")

df = DataFrame.from_array(
    [[10, 0.05],
    [100, 0.35],
    [1000, 0.95]], ['# of hours', 'prob of winning']
)

regressor = LogisticRegressor(df, 'prob of winning')

print('Game Coefficents:', regressor.coefficients)

print('Hours Played: 500, Chance of winning:', regressor.predict({'# of hours' : 500}), "\n")

b_0 = regressor.coefficients['constant']
b_1 = regressor.coefficients['# of hours']

print('avg players practice hours:', -b_0/b_1)
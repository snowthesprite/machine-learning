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
print('Yes, it does')
print()

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
print(regressor.coefficients)
print(regressor.predict({'beef' : 5, 'pb' : 0}))
print(regressor.predict({'beef' : 12, 'pb' : 0}))
print(regressor.predict({'beef' : 5, 'pb' : 5, 'beef * pb' : 25}))

import sys
sys.path.append('src')
from dataframe import DataFrame
from logistic_regressor import LogisticRegressor

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
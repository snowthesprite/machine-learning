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

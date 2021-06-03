import sys
sys.path.append('src')
from dataframe import DataFrame
from logistic_regressor import LogisticRegressor

df = DataFrame.from_array(
    [[0.5, 2],
     [0.9,0.9],
     [1,0.3]],
    columns = ['x','y']
)
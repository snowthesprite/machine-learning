import sys
sys.path.append('src')
from linear_regressor import LinearRegressor
from dataframe import DataFrame
import math

class LogisticRegressor (LinearRegressor):
    def __init__(self, data_frame, dependent_variable, change, upper_bound = 1) :
        self.depend_var = dependent_variable
        self.change = change
        self.up_bound = upper_bound
        self.data_frame = self.transform(data_frame)
        self.coefficients = self.calculate_coefficient()
        self.funct = lambda a : self.up_bound / (1 + math.exp(a))
    
    def transform(self, df) :
        dict_data = df.data_dict.copy()
        transformed_df = {'x' : [1,2,3,2,3,4], 'y': [0,0,0,1,1,1]}
        for index in range(len(dict_data[self.depend_var])) :
            element = dict_data[self.depend_var][index]
            if element == 0 :
                element = self.change
            if element == 1 :
                element = 1 - self.change
            transformed_df[self.depend_var][index] = math.log((self.up_bound/element) - 1)
        return DataFrame(transformed_df, df.columns.copy())

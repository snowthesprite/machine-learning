from linear_regressor import LinearRegressor
from dataframe import DataFrame
import math

class LogisticRegressor (LinearRegressor):
    def __init__(self, data_frame, dependent_variable) :
        self.depend_var = dependent_variable
        self.data_frame = self.transform(data_frame)
        self.coefficients = self.calculate_coefficient()
        self.funct = lambda a : 1 / (1 + math.exp(a))
    
    def transform(self, df) :
        dict_data = df.data_dict
        transformed_df = dict_data.copy()
        for index in range(len(dict_data[self.depend_var])) :
            element = dict_data[self.depend_var][index]
            transformed_df[self.depend_var][index] = math.log((1/element) - 1)
        return DataFrame(transformed_df, df.columns)


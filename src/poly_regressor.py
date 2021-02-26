import sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor

class PolynomialRegressor (LinearRegressor) :
    def __init__(self, degree) :
        self.degree = degree
        self.data_frame = None
        self.depend_var = None
        self.coefficients = None
        self.funct = lambda a : a

    def fit (self, dataframe, dependent_variable) :
        self.data_frame = dataframe
        dict_data = self.data_frame.data_dict
        self.depend_var = dependent_variable
        independ_var = [var for var in dict_data if var != self.depend_var][0]
        if self.degree == 0 :
            self.data_frame = DataFrame({self.depend_var : dict_data[self.depend_var]}, [self.depend_var])
        for degree in range(1, self.degree) :
            col = independ_var + '^' + str(degree + 1)
            col_val = [dict_data[independ_var][index] ** (degree + 1) for index in range(len(dict_data[independ_var]))]
            self.data_frame = self.data_frame.add_data(col, col_val)
        self.coefficients = self.calculate_coefficient()

df = DataFrame.from_array(
    [(0,1), (1,2), (2,5), (3,10), (4,20), (5,30)],
    columns = ['x', 'y']
)

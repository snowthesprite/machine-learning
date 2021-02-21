import sys
sys.path.append('src')
from dataframe import DataFrame
from matrix import Matrix
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
        self.depend_var = dependent_variable
        if self.degree == 0 :
            self.data_frame = DataFrame({self.depend_var : self.data_frame.data_dict[self.depend_var]}, [self.depend_var])
        for degree in range(1, self.degree) :
            col_1 = 'x'
            col_2 = 'x'
            for _ in range(1, degree) :
                col_1 = col_1 + ' * x'
            self.data_frame = self.data_frame.create_interaction_terms(col_1, col_2)
        self.coefficients = self.calculate_coefficient()

df = DataFrame.from_array(
    [(0,1), (1,2), (2,5), (3,10), (4,20), (5,30)],
    columns = ['x', 'y']
)

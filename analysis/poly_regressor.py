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

print('Does the PolynomialRegressor work?')

constant_regressor = PolynomialRegressor(degree = 0)
constant_regressor.fit(df, dependent_variable = 'y')
coeff_vals = []
for element in list(constant_regressor.coefficients.values()) :
    coeff_vals.append(round(element, 4))
assert coeff_vals ==  [11.3333]
assert round(constant_regressor.predict({'x': 2}), 4) ==  11.3333

linear_regressor = PolynomialRegressor(degree = 1)
linear_regressor.fit(df, dependent_variable = 'y')
coeff_vals = []
for element in list(linear_regressor.coefficients.values()) :
    coeff_vals.append(round(element, 4))
assert coeff_vals ==  [-3.2381, 5.8286]
assert round(linear_regressor.predict({'x': 2}), 4) ==  8.4190

quadratic_regressor = PolynomialRegressor(degree = 2)
quadratic_regressor.fit(df, dependent_variable = 'y')
coeff_vals = []
for element in list(quadratic_regressor.coefficients.values()) :
    coeff_vals.append(round(element, 4))
assert coeff_vals ==  [1.1071, -0.6893, 1.3036]
assert round(quadratic_regressor.predict({'x': 2}), 4) ==  4.9429

cubic_regressor = PolynomialRegressor(degree = 3)
cubic_regressor.fit(df, dependent_variable = 'y')
#cubic_regressor.solve_coefficients()
coeff_vals = []
for element in list(cubic_regressor.coefficients.values()) :
    coeff_vals.append(round(element, 4))
assert coeff_vals ==  [1.1349, -0.8161, 1.3730, -0.0093]
assert round(cubic_regressor.predict({'x': 2}), 4) ==  4.9206

quintic_regressor = PolynomialRegressor(degree = 5)
quintic_regressor.fit(df, dependent_variable = 'y')
#quintic_regressor.solve_coefficients()
coeff_vals = []
for element in list(quintic_regressor.coefficients.values()) :
    coeff_vals.append(round(element, 4))
assert coeff_vals ==  [1.0000, -2.9500, 6.9583, -3.9583, 1.0417, -0.0917]
assert round(quintic_regressor.predict({'x': 2}), 4) ==  5.0000

print('Yes it does!')

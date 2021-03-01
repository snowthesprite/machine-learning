import sys
sys.path.append('src')
from poly_regressor import *

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

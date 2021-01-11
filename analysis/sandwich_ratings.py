import sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor

def rating(coeff_1, coeff_2, coeff_3, beef_slices, peanut_butter) :
    return coeff_1 + coeff_2 * beef_slices + coeff_3 * peanut_butter

df = DataFrame.from_array([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6]], columns = ['Slices of Beef', 'Tbsp of Peanut Butter', 'Taste Rating'])

regressor = LinearRegressor(df, dependent_variable = 'Taste Rating')

print(regressor.predict({'Slices of Beef': 5, 'Tbsp of Peanut Butter': 0}))
print()
print(regressor.predict({'Slices of Beef': 5, 'Tbsp of Peanut Butter': 5}))
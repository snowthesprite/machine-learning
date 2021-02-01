import sys
sys.path.append('src')
from dataframe import DataFrame
from logistic_regressor import LogisticRegressor
''''
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

df = DataFrame.from_array(
    [[0, 0, 1], 
    [1, 0, 2], 
    [2, 0, 4], 
    [4, 0, 8], 
    [6, 0, 9], 
    [0, 2, 2], 
    [0, 4, 5], 
    [0, 6, 7], 
    [0, 8, 6],
    [2, 2, 0],
    [3, 4, 0]],
    columns = ['beef', 'pb', 'rating']
)

df = df.create_interaction_terms('beef', 'pb')

regressor = LogisticRegressor(df, 'rating', 10)
print(regressor.coefficients)
print(regressor.predict({'beef' : 5, 'pb' : 0}))
print(regressor.predict({'beef' : 12, 'pb' : 0}))
print(regressor.predict({'beef' : 5, 'pb' : 5, 'beef * pb' : 25}))
'''
print()

df = DataFrame.from_array(
    [[0, 0, [],               1],
    [0, 0, ['mayo'],          1],
    [0, 0, ['jelly'],         4],
    [0, 0, ['mayo', 'jelly'], 0],
    [5, 0, [],                4],
    [5, 0, ['mayo'],          8],
    [5, 0, ['jelly'],         1],
    [5, 0, ['mayo', 'jelly'], 0],
    [0, 5, [],                5],
    [0, 5, ['mayo'],          0],
    [0, 5, ['jelly'],         9],
    [0, 5, ['mayo', 'jelly'], 0],
    [5, 5, [],                0],
    [5, 5, ['mayo'],          0],
    [5, 5, ['jelly'],         0],
    [5, 5, ['mayo', 'jelly'], 0]],
    columns = ['beef', 'pb', 'condiments', 'rating']
)

df = df.create_dummy_variables('condiments')


terms = df.columns.copy()

#creating interaction terms
for index_1 in range(len(terms) - 1) :
    interaction_1 = terms[index_1]
    for index_2 in range(1,len(terms) - 1) :
        interaction_2 = terms[index_2]
        if interaction_1 + " * " + interaction_2 not in df.columns and interaction_2 + " * " + interaction_1 not in df.columns and interaction_1 != interaction_2 :
            df = df.create_interaction_terms(interaction_1, interaction_2)

logistic = LogisticRegressor(df, 'rating', 10)

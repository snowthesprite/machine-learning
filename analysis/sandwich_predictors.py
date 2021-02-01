import sys
sys.path.append('src')
from dataframe import DataFrame
from logistic_regressor import LogisticRegressor
from linear_regressor import LinearRegressor

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

linear = LinearRegressor(df, 'rating')
logistic = LogisticRegressor(df, 'rating', 10)

print(linear.coefficients)
print()
print(logistic.coefficients)
print()

print(linear.predict({'beef' : 8, 'mayo' : 1, 'beef * mayo' : 8}))
print(logistic.predict({'beef' : 8, 'mayo' : 1, 'beef * mayo' : 8}))
print()

print(linear.predict({'pb' : 4, 'jelly' : 1}))
print(logistic.predict({'pb' : 4, 'jelly' : 1}))
print()

print(linear.predict({'pb' : 4, 'mayo' : 1}))
print(logistic.predict({'pb' : 4, 'mayo' : 1}))
print()

print(linear.predict({'beef' : 8, 'pb' : 4, 'mayo' : 1}))
print(logistic.predict({'beef' : 8, 'pb' : 4, 'mayo' : 1}))
print()

print(linear.predict({'beef' : 8, 'mayo' : 1, 'jelly' : 1}))
print(logistic.predict({'beef' : 8, 'mayo' : 1, 'jelly' : 1}))

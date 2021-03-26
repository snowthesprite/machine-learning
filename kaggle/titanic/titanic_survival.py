import sys
sys.path.append('src')
from dataframe import DataFrame
from linear_regressor import LinearRegressor
from parse_line import *

data_types = {
    "PassengerId": int,
    "Survived": int,
    "Pclass": int,
    "Name": str,
    "Sex": str,
    "Age": float,
    "SibSp": int,
    "Parch": int,
    "Ticket": str,
    "Fare": float,
    "Cabin": str,
    "Embarked": str
}

df = DataFrame.from_csv("kaggle/titanic/data/dataset_of_knowns.csv", data_types=data_types, parser=parse_line)

#df = DataFrame.from_csv("kaggle/titanic/data/smaller.csv", data_types=data_types, parser=parse_line)


get_surname = (lambda a : a.split(',')[0][1:])
df = df.apply('Name', get_surname, 'Surname')

get_first_cabin = (lambda a : a if (a == None or ' ' not in a) else a.split(' ')[0])
df = df.apply('Cabin', get_first_cabin)

cabin_type = (lambda a : a[0] if (a != None) else None)
ct_arr = df.apply('Cabin', cabin_type).select_columns(['Cabin']).data_dict['Cabin']

cabin_number = (lambda a : int(a[1:]) if (a != None and a[1:] != '') else a)
df = df.apply('Cabin', cabin_number, 'CabinNumber')

df = df.add_data('CabinType', ct_arr, 10)

ticket_type = (lambda a : a.split(' ')[0] if (' ' in a) else (None if a.isnumeric() else a))
tt_arr = df.apply('Ticket', ticket_type).select_columns(['Ticket']).data_dict['Ticket']

ticket_number = (lambda a : int(a.split(' ')[-1]) if (' ' in a) else (None if not a.isnumeric()  else int(a)))
df = df.apply('Ticket', ticket_number, 'TicketNumber')

df = df.add_data('TicketType', tt_arr, 8)




df = df.select_columns(["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "CabinType", "Embarked"])




df = df.create_dummy_variables('Sex', True, {'male' : 1, 'female' : 0})

def_age = df.select_rows_where((lambda a : a['Age'] != None))
avg_age = sum(def_age.data_dict['Age'])/len(def_age.data_dict['Age'])
replace_none = (lambda element : avg_age if (element == None) else element )
df = df.apply('Age', replace_none)

sibsp_0 = df.apply('SibSp',(lambda element : 1 if (element == 0) else 0)).data_dict['SibSp']
df = df.add_data('SibSp=0',sibsp_0,df.columns.index('SibSp')+1)

df = df.apply('Parch',(lambda element : 1 if (element == 0) else 0), 'Parch=0')

df = df.create_dummy_variables(initial_key = 'CabinType', add_on = 'CabinType=')

df = df.create_dummy_variables(initial_key = 'Embarked', add_on = 'Embarked=')

df_1 = df.select_columns(['Sex'])

titanic_reg_1 = LinearRegressor(df_1,'Survived')

''''
df_1 = df.select_columns(['Sex'])

titanic_reg_1 = LinearRegressor(df_1,'Survived')

df_1 = df.select_columns(['Sex'])

titanic_reg_1 = LinearRegressor(df_1,'Survived')

df_1 = df.select_columns(['Sex'])

titanic_reg_1 = LinearRegressor(df_1,'Survived')

df_1 = df.select_columns(['Sex'])

titanic_reg_1 = LinearRegressor(df_1,'Survived')

df_1 = df.select_columns(['Sex'])

titanic_reg_1 = LinearRegressor(df_1,'Survived')

'''

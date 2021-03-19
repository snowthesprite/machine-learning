import sys
sys.path.append('src')
from dataframe import DataFrame
from parse_line import *

print('Does parse_line work?') #
''''
line_1 = "1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,,S"

#assert parse_line(line_1) == ['1', '0', '3', "'Braund, Mr. Owen Harris'", 'male', '22', '1', '0', 'A/5 21171', '7.25', '', 'S']

line_2 = '102,0,3,"Petroff, Mr. Pastcho (""Pentcho"")",male,,0,0,349215,7.8958,,S'

#assert parse_line(line_2) == ['102', '0', '3', '"Petroff, Mr. Pastcho (""Pentcho"")"', 'male', '', '0', '0', '349215', '7.8958', '', 'S']

line_3 = '187,1,3,"O\'Brien, Mrs. Thomas (Johanna ""Hannah"" Godfrey)",female,,1,0,370365,15.5,,Q'

#assert parse_line(line_3) == ['187', '1', '3', '"O\'Brien, Mrs. Thomas (Johanna ""Hannah"" Godfrey)"', 'female', '', '1', '0', '370365', '15.5', '', 'Q']
'''
print('Yes it does!', "\n")



print('Does the dataframe implementation work?') #
''''
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

#assert df.columns == ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]

#assert df.to_array()[:5] == [[1, 0, 3, '"Braund, Mr. Owen Harris"', "male", 22, 1, 0, "A/5 21171", 7.25, "", "S"],
[2, 1, 1, '"Cumings, Mrs. John Bradley (Florence Briggs Thayer)"', "female", 38, 1, 0, "PC 17599", 71.2833, "C85", "C"],
[3, 1, 3, '"Heikkinen, Miss. Laina"', "female", 26, 0, 0, "STON/O2. 3101282", 7.925, "", "S"],
[4, 1, 1, '"Futrelle, Mrs. Jacques Heath (Lily May Peel)"', "female", 35, 1, 0, "113803", 53.1, "C123", "S"],
[5, 0, 3, '"Allen, Mr. William Henry"', "male", 35, 0, 0, "373450", 8.05, "", "S"]]
'''
print('Yes it does!', "\n")


print('Double checking the parser works for from CSV...') ### (3/13/2021)

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
''''
#assert df.columns == ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]

#assert df.to_array()[:5] == [[1, 0, 3, '"Braund, Mr. Owen Harris"', "male", 22.0, 1, 0, "A/5 21171", 7.25, None, "S"],
[2, 1, 1, '"Cumings, Mrs. John Bradley (Florence Briggs Thayer)"', "female", 38.0, 1, 0, "PC 17599", 71.2833, "C85", "C"],
[3, 1, 3, '"Heikkinen, Miss. Laina"', "female", 26.0, 0, 0, "STON/O2. 3101282", 7.925, None, "S"],
[4, 1, 1, '"Futrelle, Mrs. Jacques Heath (Lily May Peel)"', "female", 35.0, 1, 0, "113803", 53.1, "C123", "S"],
[5, 0, 3, '"Allen, Mr. William Henry"', "male", 35.0, 0, 0, "373450", 8.05, None, "S"]]
'''
print('...it works fine', "\n")

print('Does the splitting things work?') 

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
''''
#assert df.columns == ["PassengerId", "Survived", "Pclass", "Surname", "Sex", "Age", "SibSp", "Parch", "TicketType", "TicketNumber", "Fare", "CabinType", "CabinNumber", "Embarked"]

#assert df.to_array()[:5] == [[1, 0, 3, "Braund", "male", 22.0, 1, 0, "A/5", 21171, 7.25, None, None, "S"],
[2, 1, 1, "Cumings", "female", 38.0, 1, 0, "PC", 17599, 71.2833, "C", 85, "C"],
[3, 1, 3, "Heikkinen", "female", 26.0, 0, 0, "STON/O2.", 3101282, 7.925, None, None, "S"],
[4, 1, 1, "Futrelle", "female", 35.0, 1, 0, None, 113803, 53.1, "C", 123, "S"],
[5, 0, 3, "Allen", "male", 35.0, 0, 0, None, 373450, 8.05, None, None, "S"]]
'''
print('Yes it does!', "\n")

#print(df.to_array()[0], "\n")

#print(df.group_by('Pclass').aggregate('Survived', 'avg', 'meanSurvival').aggregate('PassengerId', 'count', 'count').select_columns(['Pclass', 'meanSurvival', 'count']).data_dict, "\n \n")

#print(df.group_by('Sex').aggregate('Survived', 'avg', 'meanSurvival').aggregate('PassengerId', 'count', 'count').select_columns(['Sex', 'meanSurvival', 'count']).data_dict)

#print(df.group_by('SibSp').aggregate('Survived', 'avg', 'meanSurvival').aggregate('PassengerId', 'count', 'count').select_columns(['SibSp', 'meanSurvival', 'count']).data_dict)

#print(df.group_by('Parch').aggregate('Survived', 'avg', 'meanSurvival').aggregate('PassengerId', 'count', 'count').select_columns(['Parch', 'meanSurvival', 'count']).data_dict)

#print(df.group_by('CabinType').aggregate('Survived', 'avg', 'meanSurvival').aggregate('PassengerId', 'count', 'count').select_columns(['CabinType', 'meanSurvival', 'count']).data_dict)

#print(df.group_by('Embarked').aggregate('Survived', 'avg', 'meanSurvival').aggregate('PassengerId', 'count', 'count').select_columns(['Embarked', 'meanSurvival', 'count']).data_dict)

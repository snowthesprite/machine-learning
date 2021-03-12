import sys
sys.path.append('src')
from dataframe import DataFrame
from parse_line import *

print('Does parse_line work?')

line_1 = "1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,,S"

assert parse_line(line_1) == ['1', '0', '3', "'Braund, Mr. Owen Harris'", 'male', '22', '1', '0', 'A/5 21171', '7.25', '', 'S']

line_2 = '102,0,3,"Petroff, Mr. Pastcho (""Pentcho"")",male,,0,0,349215,7.8958,,S'

assert parse_line(line_2) == ['102', '0', '3', '"Petroff, Mr. Pastcho (""Pentcho"")"', 'male', '', '0', '0', '349215', '7.8958', '', 'S']

line_3 = '187,1,3,"O\'Brien, Mrs. Thomas (Johanna ""Hannah"" Godfrey)",female,,1,0,370365,15.5,,Q'

assert parse_line(line_3) == ['187', '1', '3', '"O\'Brien, Mrs. Thomas (Johanna ""Hannah"" Godfrey)"', 'female', '', '1', '0', '370365', '15.5', '', 'Q']

print('Yes it does!', "\n")

print('Does the dataframe implementation work?')

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

assert df.columns == ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"]

assert df.to_array()[:5] == [[1, 0, 3, '"Braund, Mr. Owen Harris"', "male", 22, 1, 0, "A/5 21171", 7.25, "", "S"],
[2, 1, 1, '"Cumings, Mrs. John Bradley (Florence Briggs Thayer)"', "female", 38, 1, 0, "PC 17599", 71.2833, "C85", "C"],
[3, 1, 3, '"Heikkinen, Miss. Laina"', "female", 26, 0, 0, "STON/O2. 3101282", 7.925, "", "S"],
[4, 1, 1, '"Futrelle, Mrs. Jacques Heath (Lily May Peel)"', "female", 35, 1, 0, "113803", 53.1, "C123", "S"],
[5, 0, 3, '"Allen, Mr. William Henry"', "male", 35, 0, 0, "373450", 8.05, "", "S"]]

print('Yes it does!')
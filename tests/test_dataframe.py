import sys
sys.path.append('src')
from dataframe import DataFrame
''''
data_dict = {'Pete': [1, 0, 1, 0],'John': [2, 1, 0, 2],'Sarah': [3, 1, 4, 0]}

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sarah'])

print('Did DataFrame correctly take data_dict?')
assert df1.data_dict == {'Pete': [1, 0, 1, 0],'John': [2, 1, 0, 2],'Sarah': [3, 1, 4, 0]}, 'No, it did not'
print('Yes, it did')
print()

print('Is DataFrames column order in order?')
assert df1.columns == ['Pete', 'John', 'Sarah']

print('Does DataFrames to_array put the given data in the correct array?')
assert df1.to_array() == [[1, 2, 3], [0, 1, 1], [1, 0, 4], [0, 2, 0]], 'No, it did not'
print('Yes, it did')
print()

df2 = df1.select_columns(['Sarah', 'Pete'])

print('Did DataFrames select_columns chose the correct columns?')
assert df2.to_array() == [[3, 1], [1, 0], [4, 1], [0, 0]], 'df2s to_array is not correct'

assert df2.columns == ['Sarah', 'Pete'], 'df2s columns is not correct'
print('Yes it did')
print()

df3 = df1.select_rows([1,3])

print('Did DataFrames select_rows take the correct rows?')
assert df3.to_array() == [[0, 1, 1], [0, 2, 0]], 'No, it did not'
print('Yes, it did')
print()

data_dict = {'Pete': [1, 0, 1, 0],'John': [2, 1, 0, 2],'Sarah': [3, 1, 4, 0]}

df1 = DataFrame(data_dict, column_order = ['Pete', 'John', 'Sarah'])
df2 = df1.apply('John', lambda x: 7 * x)

print("Does DataFrames apply method work correctly?")

assert df2.data_dict == {'Pete': [1, 0, 1, 0],'John': [14, 7, 0, 14],'Sarah': [3, 1, 4, 0]}, 'No, it does not'
print('Yes it did!')
print()

columns = ['firstname', 'lastname', 'age']
arr = [['Kevin', 'Fray', 5], ['Charles', 'Trapp', 17], ['Anna', 'Smith', 13], ['Sylvia', 'Mendez', 9]]
df = DataFrame.from_array(arr, columns)

print('Does select_rows_where work?')
assert df.select_rows_where(lambda row: len(row['firstname']) >= len(row['lastname'])and row['age'] > 10).to_array() == [['Charles', 'Trapp', 17]], 'No, select_rows_where does not work'
print('Yes, it does')
print()

print('Does order_by work?')
assert df.order_by('age', ascending=True).to_array() == [['Kevin', 'Fray', 5], ['Sylvia', 'Mendez', 9], ['Anna', 'Smith', 13], ['Charles', 'Trapp', 17]], 'No, order_by does not work for "age" and ascending = True'

assert df.order_by('firstname', ascending=False).to_array() == [['Sylvia', 'Mendez', 9], ['Kevin', 'Fray', 5], ['Charles', 'Trapp', 17], ['Anna', 'Smith', 13]], 'No, order_by does not work for "firstname" and ascending = False'
print('Yes it does!')
print()
'''
import csv

test = []

path_to_datasets = '/home/runner/machine-learning/datasets/'
filename = 'airtravel.csv' 
with open(path_to_datasets + filename, "r") as file:
    data = csv.reader(file, quotechar='|', skipinitialspace = True)
    for row in data :
        #print(row)
        test.append(row)
test.pop(len(test) - 1)
print()

filepath = path_to_datasets + filename
df = DataFrame.from_csv(filepath, header=True)

print(df.to_array())

#assert df.to_array() == [['"Month"', '"1958"', '"1959"', '"1960"'], ['"JAN"',  '340',  '360',  '417'], ['"FEB"',  '318',  '342',  '391'], ['"MAR"',  '362',  '406',  '419'], ['"APR"',  '348',  '396',  '461'], ['"MAY"',  '363',  '420',  '472'], ['"JUN"',  '435',  '472',  '535'], ['"JUL"',  '491',  '548',  '622'], ['"AUG"',  '505',  '559',  '606'], ['"SEP"',  '404',  '463',  '508'], ['"OCT"',  '359',  '407',  '461'], ['"NOV"',  '310',  '362',  '390'], ['"DEC"',  '337',  '405',  '432']]
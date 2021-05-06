import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from timeit import default_timer as timer
start_time = timer()

df = pd.read_csv('/home/runner/machine-learning/analysis/KNN/book_type.csv')

def change_type_to_int (book_type) :
    if book_type == "children's book" :
        return 0
    elif book_type == "adult book" :
        return 1

df['book type'] = df['book type'].apply(change_type_to_int)

book_type = df['book type']

def find_accuracy (predict, actual) :
    num_correct = 0
    num_incorrect = 0
    for i in range(len(predict)) :
        if predict[i] == actual[i] :
            num_correct += 1
        else :
            num_incorrect+=1 
    return num_correct/(num_correct + num_incorrect)

##Unscaled
#'''
acc_un = []
predict_un = {k : [] for k in range(1,100)}

for row_id in range(book_type.size) :
    mod_df = df.drop(row_id)
    mod_book_type = book_type.drop(row_id)
    for k in range(1,100) :
        KNN = KNeighborsClassifier(n_neighbors=k)
        KNN.fit(mod_df, mod_book_type)
        predict_un[k].append(KNN.predict([df.iloc[row_id]]))

#'''
print('un')
##Simple scaling
#'''
df_simple = df.copy()
df_simple['num pages'] = df['num pages']/df['num pages'].max()
df_simple['num unique words'] = df['num unique words']/df['num unique words'].max()
df_simple['avg sentence length'] = df['avg sentence length']/df['avg sentence length'].max()
df_simple['avg word size'] = df['avg word size']/df['avg word size'].max()

acc_simp = []
predict_simp = {k : [] for k in range(1,100)}

for row_id in range(book_type.size) :
    mod_df = df_simple.drop(row_id)
    mod_book_type = book_type.drop(row_id)
    for k in range(1,100) :
        KNN = KNeighborsClassifier(n_neighbors=k)
        KNN.fit(mod_df, mod_book_type)
        predict_simp[k].append(KNN.predict([df_simple.iloc[row_id]]))

#'''
print('simp')
##Min-max
#'''
df_min_max = df.copy()
df_min_max['num pages'] = (df['num pages']-df['num pages'].min())/(df['num pages'].max() - df['num pages'].min())
df_min_max['num unique words'] = (df['num unique words']-df['num unique words'].min())/(df['num unique words'].max() - df['num unique words'].min())
df_min_max['avg sentence length'] = (df['avg sentence length']-df['avg sentence length'].min())/(df['avg sentence length'].max() - df['avg sentence length'].min())
df_min_max['avg word size'] = (df['avg word size']-df['avg word size'].min())/(df['avg word size'].max() - df['avg word size'].min())

acc_min_max = []
predict_min_max = {k : [] for k in range(1,100)}

for row_id in range(book_type.size) :
    mod_df = df_min_max.drop(row_id)
    mod_book_type = book_type.drop(row_id)
    for k in range(1,100) :
        KNN = KNeighborsClassifier(n_neighbors=k)
        KNN.fit(mod_df, mod_book_type)
        predict_min_max[k].append(KNN.predict([df_min_max.iloc[row_id]]))

#'''
print('min max')
##z-score
#'''
df_z = df.copy()
df_z['num pages'] = (df['num pages']-df['num pages'].mean())/(df['num pages'].std())
df_z['num unique words'] = (df['num unique words']-df['num unique words'].mean())/(df['num unique words'].std())
df_z['avg sentence length'] = (df['avg sentence length']-df['avg sentence length'].mean())/(df['avg sentence length'].std())
df_z['avg word size'] = (df['avg word size']-df['avg word size'].mean())/(df['avg word size'].std())

acc_z = []
predict_z = {k : [] for k in range(1,100)}

for row_id in range(book_type.size) :
    mod_df = df_z.drop(row_id)
    mod_book_type = book_type.drop(row_id)
    for k in range(1,100) :
        KNN = KNeighborsClassifier(n_neighbors=k)
        KNN.fit(mod_df, mod_book_type)
        predict_z[k].append(KNN.predict([df_z.iloc[row_id]]))

#'''
print('z')

for k in range(1,100) :
    acc_un.append(find_accuracy(predict_un[k],book_type))
    acc_simp.append(find_accuracy(predict_simp[k],book_type))
    acc_min_max.append(find_accuracy(predict_min_max[k],book_type))
    acc_z.append(find_accuracy(predict_z[k],book_type))

#'''
import matplotlib.pyplot as plt
#plt.style.use('bmh')

plt.plot(range(1,100), acc_un)
plt.plot(range(1,100), acc_simp)
plt.plot(range(1,100), acc_min_max)
plt.plot(range(1,100), acc_z)
#plt.xlim((1,19))
plt.legend(['Unaltered', 'Simple', 'Min-Max', 'Z'])

plt.savefig('analysis/KNN/KNN_model.png')

print('\n\n', timer() - start_time, 'sec \n\n\n')
#'''
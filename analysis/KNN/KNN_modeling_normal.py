import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('/home/runner/machine-learning/analysis/KNN/book_type.csv')

def change_type_to_int (book_type) :
    if book_type == "children's book" :
        return 0
    elif book_type == "adult book" :
        return 1

df['book type'] = df['book type'].apply(change_type_to_int)
book_type = df['book type']
del df['book type']

columns = list(df.columns)

def find_accuracy (predict, actual) :
    num_correct = 0
    for i in range(len(predict)) :
        if predict[i] == actual[i] :
            num_correct += 1
    return num_correct/len(predict)

k_vals = range(1,100,2)

df_simp = df.copy()
df_min_max = df.copy()
df_z = df.copy()

for column in columns :
    df_simp[column] = df[column]/df[column].max()

    df_min_max[column] = (df[column]-df[column].min())/(df[column].max() - df[column].min())

    df_z[column] = (df[column]-df[column].mean())/(df[column].std())

acc_un = []
predict_un = {k : [] for k in k_vals}

acc_simp = []
predict_simp = {k : [] for k in k_vals}

acc_min_max = []
predict_min_max = {k : [] for k in k_vals}

acc_z = []
predict_z = {k : [] for k in k_vals}

for row_id in range(book_type.size) :
    mod_df = df.drop(row_id)
    mod_df_simp = df_simp.drop(row_id)
    mod_df_min = df_min_max.drop(row_id)
    mod_df_z = df_z.drop(row_id)

    mod_book_type = book_type.drop(row_id)
    for k in k_vals :
        KNN = KNeighborsClassifier(n_neighbors=k)

        KNN.fit(mod_df, mod_book_type)
        predict_un[k].append(KNN.predict([df.iloc[row_id]]))

        KNN.fit(mod_df_simp, mod_book_type)
        predict_simp[k].append(KNN.predict([df_simp.iloc[row_id]]))

        KNN.fit(mod_df_min, mod_book_type)
        predict_min_max[k].append(KNN.predict([df_min_max.iloc[row_id]]))

        KNN.fit(mod_df_z, mod_book_type)
        predict_z[k].append(KNN.predict([df_z.iloc[row_id]]))

for k in k_vals :
    acc_un.append(find_accuracy(predict_un[k],book_type))
    acc_simp.append(find_accuracy(predict_simp[k],book_type))
    acc_min_max.append(find_accuracy(predict_min_max[k],book_type))
    acc_z.append(find_accuracy(predict_z[k],book_type))

import matplotlib.pyplot as plt

plt.plot(k_vals, acc_un)
plt.plot(k_vals, acc_simp)
plt.plot(k_vals, acc_min_max)
plt.plot(k_vals, acc_z)
plt.xlable('k')
plt.ylable('Accuracy')
plt.legend(['Unaltered', 'Simple', 'Min-Max', 'Z'])

plt.savefig('analysis/KNN/KNN_model.png')
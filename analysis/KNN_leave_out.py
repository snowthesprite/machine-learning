import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

df = pd.DataFrame([['Shortbread', 0.14, 0.14, 0.28, 0.44],
                    ['Shortbread', 0.10, 0.18, 0.28, 0.44],
                    ['Shortbread', 0.12, 0.10, 0.33, 0.45],
                    ['Shortbread', 0.10, 0.25, 0.25, 0.40],
                    ['Sugar', 0.00, 0.10, 0.40, 0.50],
                    ['Sugar', 0.00, 0.20, 0.40, 0.40],
                    ['Sugar', 0.02, 0.08, 0.45, 0.45],
                    ['Sugar', 0.10, 0.15, 0.35, 0.40],
                    ['Sugar', 0.10, 0.08, 0.35, 0.47],
                    ['Sugar', 0.00, 0.05, 0.30, 0.65],
                    ['Fortune', 0.20, 0.00, 0.40, 0.40],
                    ['Fortune', 0.25, 0.10, 0.30, 0.35],
                    ['Fortune', 0.22, 0.15, 0.50, 0.13],
                    ['Fortune', 0.15, 0.20, 0.35, 0.30],
                    ['Fortune', 0.22, 0.00, 0.40, 0.38],
                    ['Shortbread', 0.05, 0.12, 0.28, 0.55],
                    ['Shortbread', 0.14, 0.27, 0.31, 0.28],
                    ['Shortbread', 0.15, 0.23, 0.30, 0.32],
                    ['Shortbread', 0.20, 0.10, 0.30, 0.40]],
                     columns = ['Cookie Type' ,'Portion Eggs','Portion Butter','Portion Sugar','Portion Flour']
                    )

cookie_type = df['Cookie Type']
del df['Cookie Type']

def find_accuracy(predictions) :
    correct = 0
    for index in range(cookie_type.size) :
        print(index, predictions[index], cookie_type[index])
        if predictions[index] == cookie_type[index] :
            correct+=1
    return correct/cookie_type.size

all_acc = []

for neigh_numb in range(1, cookie_type.size) :
    predictions = []
    for row_id in range(cookie_type.size) :
        mod_df = df.drop(row_id)
        mod_cookies = cookie_type.drop(row_id)
        KNN = KNeighborsClassifier(n_neighbors=neigh_numb)
        KNN.fit(mod_df, mod_cookies)
        predictions.append(KNN.predict([df.iloc[row_id]]))
    print('k={}'.format(neigh_numb))
    all_acc.append(find_accuracy(predictions))
    print()
    print()

'''
import matplotlib.pyplot as plt
plt.style.use('bmh')

k_val = range(1, cookie_type.size)

plt.plot(k_val, all_acc)
plt.xlim((1,19))
plt.xticks(range(19))

plt.savefig('analysis/KNN_Acc.png')
#'''
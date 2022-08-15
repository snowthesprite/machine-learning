import sys
sys.path.append('src')
from naive_bayes import NaiveBayes

data = {'class': ['not','scam','scam','not','not','scam','not','not','scam','not'],
        'errors': [0,1,1,0,0,1,1,0,1,0],
        'links': [0,1,1,0,1,1,0,1,0,1]}

bayes = NaiveBayes(data)

imput = {'errors': 0,
        'links': 0}

print(bayes.find_class(imput))

imput = {'errors': 1,
        'links': 1}

print(bayes.find_class(imput))

imput = {'errors': 1,
        'links': 0}

print(bayes.find_class(imput))

imput = {'errors': 0,
        'links': 1}

print(bayes.find_class(imput))
import sys
sys.path.append('src')
from naive_bayes import NaiveBayes

data = {'class': [0,1,1,0,0,1,0,0,1,0],
        'errors': [0,1,1,0,0,1,1,0,1,0],
        'links': [0,1,1,0,1,1,0,1,0,1]}

imput = {'errors': [0,1,1,0],
        'links': [0,1,0,1]}
import sys
sys.path.append('src')
from matrix import Matrix

random_matrix = Matrix([[8, 5, 6, 9, 5, 4, 1, 4, 4, 9], [3, 0, 3, 4, 4, 9, 4, 4, 3, 7], [3, 3, 3, 0, 3, 0, 3, 9, 1, 1], [2, 7, 3, 1, 4, 1, 1, 8, 3, 5], [3, 1, 9, 7, 6, 6, 0, 8, 2, 7], [3, 3, 7, 7, 8, 8, 6, 1, 9, 7], [0, 3, 2, 3, 8, 6, 3, 2, 9, 0], [6, 2, 5, 4, 7, 9, 1, 2, 3, 6], [6, 3, 9, 2, 2, 0, 3, 3, 5, 0], [3, 0, 2, 0, 1, 7, 7, 9, 2, 3]])


#det = random_matrix.cofactor_method_determinant()

#det = random_matrix.determinant()

#The original determinant method is MUCH FASTER. I'm assuming that the reason Cofactor is so much slower is because of all the layers of recursiveness it goes through. (is recursiveness a word? it is now)
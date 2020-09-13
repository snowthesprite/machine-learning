import sys
sys.path.append('src')
from matrix import Matrix

print('For the 2x2 Matrices')
print('')

A = Matrix([[1,3],[2,4]])

print('Is {} the correct elements in A?'.format(A.elements))
assert A.elements == [[1,3],[2,4]], 'No, they are not the right elements'
print('Yes, they are the right elements')
print('')

B = A.copy() 

A = 'resetting A to a string'

print('Did B properly copy A?')
assert B.elements == [[1,3],[2,4]], 'No it did not'
print('Yes, B did properly copy A')
print('')

C = Matrix([[1,0],[2,-1]])

D = B.add(C)

print('Is D the addition of B and C?')
assert D.elements == [[2,3],[4,3]], 'No it is not'
print('Yes, D is the addition of B and C')
print('')

E = B.subtract(C)

print('Is E the subtraction of B and C?')
assert E.elements == [[0,3],[0,5]], 'No it is not'
print('Yes, E is the subtraction of B and C')
print('')

F = B.scalar_multiply(2)

print('Is F B multiplied by 2?')
assert F.elements == [[2,6],[4,8]], 'No it is not'
print('Yes, F is B multiplied by 2')
print('')

G = B.matrix_multiply(C)

print('Is G B multiplied by C?')
assert G.elements == [[7,-3],[10,-4]], 'No it is not'
print('Yes, G is B multiplied by C')
print('')

print('For the MxN Matrices')
print('')

A = Matrix([[1,0,2,0,3],[0,4,0,5,0],[6,0,7,0,8],[-1,-2,-3,-4,-5]])

print('Is the num_rows and num_cols correct for the matrix A?')
assert (A.num_rows, A.num_cols) == (4, 5), 'No they are not'
print('Yes, they are')
print('')

A_t = A.transpose()

print('Did A properly transpose?')
assert A_t.elements == [[ 1,  0,  6, -1],[ 0,  4,  0, -2],[ 2,  0,  7, -3],[ 0,  5,  0, -4],[ 3,  0,  8, -5]], 'No, it did not'
print('Yes, it did')
print('')

B = A_t.matrix_multiply(A)

print('Is the matrix B the product of A and A transpose?')
assert B.elements == [[38,  2, 47,  4, 56],[ 2, 20,  6, 28, 10],[47,  6, 62, 12, 77],[ 4, 28, 12, 41, 20],[56, 10, 77, 20, 98]], 'No it is not'
print('Yes it is')
print('')

C = B.scalar_multiply(0.1)

print('Is the matrix C the matrix B multiplied by 0.1?')
assert C.elements == [[3.8,  .2, 4.7,  .4, 5.6],[ .2, 2.0,  .6, 2.8, 1.0],[4.7,  .6, 6.2, 1.2, 7.7],[ .4, 2.8, 1.2, 4.1, 2.0],[5.6, 1.0, 7.7, 2.0, 9.8]], 'No it is not'
print('Yes, it is')
print('')

D = B.subtract(C)

print('Is the matrix D the matrix B subtracted by the matrix C?')
assert D.elements == [[34.2,  1.8, 42.3,  3.6, 50.4],[ 1.8, 18. ,  5.4, 25.2,  9. ],[42.3,  5.4, 55.8, 10.8, 69.3],[ 3.6, 25.2, 10.8, 36.9, 18. ],[50.4,  9. , 69.3, 18. , 88.2]], 'No it is not'
print('Yes, it is')
print('')

E = D.add(C)

print('Is the matrix E the matrix D subtracted by the matrix C?')
assert E.elements == [[38,  2, 47,  4, 56],[ 2, 20,  6, 28, 10],[47,  6, 62, 12, 77],[ 4, 28, 12, 41, 20],[56, 10, 77, 20, 98]], 'No it is not'
print('Yes, it is')
print('')

print('Is the matrix E equal to the matrix B, but not equal to the matrix C?')
assert (E.is_equal(B), E.is_equal(C)) == (True, False), 'No it is not'
print('Yes, it is')

A = Matrix([[0, 1, 2],[3, 6, 9],[2, 6, 8]])

assert A.get_pivot_row(0) == 1

A.swap_rows(0,1)

assert A.elements == [[3, 6, 9], [0, 1, 2], [2, 6, 8]]

A.normalize_row(0)

assert A.elements == [[1, 2, 3], [0, 1, 2], [2, 6, 8]]

A.clear_below(0)

assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 2, 2]]

assert A.get_pivot_row(1) == 1

A.normalize_row(1)

assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 2, 2]]

A.clear_below(1)

assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 0, -2]]

A.normalize_row(2)

assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 0, 1]]

A.clear_above(2)

assert A.elements == [[1, 2, 0], [0, 1, 0], [0, 0, 1]]

A.clear_above(1)

assert A.elements == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

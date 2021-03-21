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
print('')

A = Matrix([[0, 1, 2],[3, 6, 9],[2, 6, 8]])

print('Does get_pivot_row get the correct row?')
assert A.get_pivot_row(0) == 1, 'No, it did not'
print('Yes, it did')
print('')

A = A.swap_rows(0,1)

print('Did swap_rows swap the correct rows')
assert A.elements == [[3, 6, 9], [0, 1, 2], [2, 6, 8]], 'No, it did not'
print('Yes, it did')
print('')

A = A.normalize_row(0)

print('Did normalize_row normalize the right row?')
assert A.elements == [[1, 2, 3], [0, 1, 2], [2, 6, 8]], 'No, it did not'
print('Yes, it did')
print('')
print(A.elements)
A = A.clear_below(0)

print('Did clear_below correctly clear the rows below the pivot?')
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 2, 2]], 'No, it did not'
print('Yes, it did')
print('')

print('Is the pivot correct?')
assert A.get_pivot_row(1) == 1, 'No, it did not'
print('Yes, it did')
print('')

A = A.normalize_row(1)

print('Did normalize_row normalize the right row?')
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 2, 2]], 'No, it did not'
print('Yes, it did')
print('')

A = A.clear_below(1)

print('Did clear_below correctly clear the rows below the pivot?')
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 0, -2]], 'No, it did not'
print('Yes, it did')
print('')

A = A.normalize_row(2)

print('Did normalize_row normalize the right row?')
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 0, 1]], 'No, it did not'
print('Yes, it did')
print('')

A = A.clear_above(2)

print('Did clear_above correctly clear the rows above the pivot?')
assert A.elements == [[1, 2, 0], [0, 1, 0], [0, 0, 1]], 'No, it did not'
print('Yes, it did')
print('')

A = A.clear_above(1)

print('Did clear_above correctly clear the rows above the pivot?')
assert A.elements == [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 'No, it did not'
print('Yes, it did')
print()

A = Matrix([[0, 1, 2], [3, 6, 9], [2, 6, 8]])

print('Did rref() correctly put the matrix A in esholon form?')
assert A.rref().elements == [[1, 0, 0], [0, 1, 0], [0, 0, 1]], 'No it did not'
print('Yes it did')
print()

B = Matrix([[0, 0, -4, 0], [0, 0, 0.3, 0], [0, 2, 1, 0]])

print('Did rref() correctly put the matrix B in esholon form?')
assert B.rref().elements == [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]], 'No it did not'
print('Yes it did')
print()

A = Matrix([[1, 2,   3,  4], [5, 6,   7,  8], [9, 10, 11, 12]])

B = Matrix([[13, 14], [15, 16], [17, 18]])

A_augmented = A.augment(B)

print('Did the augment function properly augment the Matrices A and B?')
assert A_augmented.elements == [[1, 2,   3,  4, 13, 14], [5, 6,   7,  8, 15, 16], [9, 10, 11, 12, 17, 18]], 'No, it did not'
print('Yes it did')
print()

rows_02 = A_augmented.get_rows([0, 2])

print('Did the get_rows function correctly get rows 0 and 2 from the augmented matrix A?')
assert rows_02.elements == [[1, 2,   3,  4, 13, 14],[9, 10, 11, 12, 17, 18]], 'No it did not'
print('Yes it did')
print()

cols_0123 = A_augmented.get_columns([0, 1, 2, 3])

print('Did get_columns corretly get the columns 0, 1, 2 and 3 from the augmented matrix A?')
assert cols_0123.elements == [[1, 2,   3,  4], [5, 6,   7,  8], [9, 10, 11, 12]], 'No it did not'
print('Yes it did')
print()

cols_45 = A_augmented.get_columns([4, 5])

print('Did get_columns corretly get the columns 4 and 5 from the augmented matrix A?')
assert cols_45.elements == [[13, 14], [15, 16], [17, 18]], 'No it did not'
print('Yes it did')
print()

print('Does inverse properly inverse the various definitions of A?')
print()
A = Matrix([[1, 2],[3, 4]])
A_inv = A.inverse()
print('A - 1')

assert A_inv.elements == [[-2,   1], [1.5, -0.5]], 'Does not work for A = [[1, 2],[3, 4]]'
print('Works on A - 1')
print()

A = Matrix([[1,   2,  3],[1,   0, -1],[0.5, 0,  0]])
A_inv = A.inverse()
print('A - 2')

assert A_inv.elements == [[0,   0,    2],[0.5, 1.5, -4],[0,  -1,    2]], 'Does not work for A = [[1,   2,  3],[1,   0, -1],[0.5, 0,  0]]'
print('Works on A - 2')
print()

print('A - 3')
A = Matrix([[1, 2, 3, 0], [1, 0, 1, 0], [0, 1, 0, 0]])
A_inv = A.inverse()
print()

print('A - 4')
A = Matrix([[1, 2, 3], [3, 2, 1], [1, 1, 1]])
A_inv = A.inverse()
print()

A = Matrix([[1,2], [3,4]])
ans = A.determinant()

print('Does the determinant work for a 2x2 matrix?')
assert round(ans,6) == -2, 'No it does not'
print('Yes, it does')
print()

A = Matrix([[1,2,0.5], [3,4,-1], [8,7,-2]])
ans = A.determinant()

print('Does the determinant work for a 3x3 matrix?')
assert round(ans,6) == -10.5, 'No it does not'
print('Yes, it does')
print()

A = Matrix([[1,2,0.5,0,1,0], [3,4,-1,1,0,1], [8,7,-2,1,1,1],[-1,1,0,1,0,1], [0,0.35,0,-5,1,1], [1,1,1,1,1,0]])
ans = A.determinant()

print('Does the determinant work for a 6x6 matrix?')
assert round(ans,6) == -37.3, 'No it does not'
print('Yes, it does')
print()

print('Does the determinant work for a 6x7 matrix?')
A = Matrix([[1,2,0.5,0,1,0], [3,4,-1,1,0,1], [8,7,-2,1,1,1], [-1,1,0,1,0,1], [0,0.35,0,-5,1,1], [1,1,1,1,1,0], [2,3,1.5,1,2,0]])
ans = A.determinant()
print()

A = Matrix([[1,2,0.5,0,1,0,1], [3,4,-1,1,0,1,0], [8,7,-2,1,1,1,0], [-1,1,0,1,0,1,0], [0,0.35,0,-5,1,1,0], [1,1,1,1,1,0,0], [2,3,1.5,1,2,0,1]])
ans = A.determinant()

print('Is 0 right for a matrix that doesnt work out to rref?')
assert round(ans,6) == 0, 'No it is not'
print('Yes, it is')
print()

A = Matrix([[1, 1, 0], [2, -1, 0], [0, 0, 3]])

print('Does the exponent function work properly?')
assert A.exponent(3).elements == [[3, 3, 0], [6, -3, 0], [0, 0, 27]], 'No it does not'
print('Yes it does')
print()

A = Matrix([[1,0,2,0,3],[0,4,0,5,0],[6,0,7,0,8],[-1,-2,-3,-4,-5]])

A_t = A.transpose()

print('Does the transpose work properly?')
assert A_t.elements == [[ 1,  0,  6, -1], [ 0,  4,  0, -2], [ 2,  0,  7, -3], [ 0,  5,  0, -4], [ 3,  0,  8, -5]], 'No it does not'
print('Yes, it does')
print()

print('Do all the overloads work properly?')
B = A_t @ A
assert B.elements == [[38,  2, 47,  4, 56], [ 2, 20,  6, 28, 10], [47,  6, 62, 12, 77], [ 4, 28, 12, 41, 20], [56, 10, 77, 20, 98]], '@ (Matrix Multi) does not work'

C = B * 0.1
assert C.elements == [[3.8,  .2, 4.7,  .4, 5.6], [ .2, 2.0,  .6, 2.8, 1.0], [4.7,  .6, 6.2, 1.2, 7.7], [ .4, 2.8, 1.2, 4.1, 2.0], [5.6, 1.0, 7.7, 2.0, 9.8]], '* (scalar multi) does not work'

D = B - C

assert D.elements == [[34.2,  1.8, 42.3, 3.6, 50.4], [1.8, 18.0, 5.4, 25.2, 9.0], [42.3, 5.4, 55.8, 10.8, 69.3], [3.6, 25.2, 10.8, 36.9, 18.0], [50.4, 9.0, 69.3, 18.0, 88.2]], '- (matrix subtract) does not work'

E = D + C 

assert E.elements == [[38,  2, 47,  4, 56], [ 2, 20,  6, 28, 10], [47, 6, 62, 12, 77], [ 4, 28, 12, 41, 20], [56, 10, 77, 20, 98]],'+ (matrix add) does not work'

assert (E == B) == True, '== (equality) does not work'

assert (E == C) == False, '== (equality) does not work'

print('Yes they all work!')
print()

print('Does the cofactor method in replacement of the original det function?')

A = Matrix([[1,2], [3,4]])
ans = A.cofactor_method_determinant()
assert round(ans,6) == -2, 'Does not work for 2x2 matrix'

A = Matrix([[1,2,0.5], [3,4,-1], [8,7,-2]])
ans = A.cofactor_method_determinant()
assert round(ans,6) == -10.5, 'Does not work for 3x3 matrix'

A = Matrix([[1,2,0.5,0,1,0], [3,4,-1,1,0,1], [8,7,-2,1,1,1],[-1,1,0,1,0,1], [0,0.35,0,-5,1,1], [1,1,1,1,1,0]])
ans = A.cofactor_method_determinant()
assert round(ans,6) == -37.3, 'Does not work for 6x6 matrix'

A = Matrix([[1,2,0.5,0,1,0], [3,4,-1,1,0,1], [8,7,-2,1,1,1], [-1,1,0,1,0,1], [0,0.35,0,-5,1,1], [1,1,1,1,1,0], [2,3,1.5,1,2,0]])
ans = A.determinant()

A = Matrix([[1,2,0.5,0,1,0,1], [3,4,-1,1,0,1,0], [8,7,-2,1,1,1,0], [-1,1,0,1,0,1,0], [0,0.35,0,-5,1,1,0], [1,1,1,1,1,0,0], [2,3,1.5,1,2,0,1]])
ans = A.cofactor_method_determinant()
assert round(ans,6) == 0, 'Does not work for the non rref matrix'
print('Yes it does!')
print()

print('Do the new overloads work?')
A = Matrix([[1, 1, 0], [2, -1, 0], [0, 0, 3]])

B = 0.1 * A

assert B.elements == [[0.1, 0.1, 0], [0.2, -0.1, 0], [0, 0, 0.3]], 'No they do not'

C = A**3

assert C.elements == [[3, 3, 0], [6, -3, 0], [0, 0, 27]], 'No they do not'
print('Yes, they do')
print()

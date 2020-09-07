import sys
sys.path.append('src')
from matrix import Matrix

A = Matrix([[1,3],[2,4]])

B = A.copy()

A = 'resetting A to a string'

C = Matrix([[1,0],[2,-1]])

D = B.add(C)

E = B.subtract(C)

F = B.scalar_multiply(2)

G = B.matrix_multiply(C)

#print(B.elements)

#print(C.elements)

print(G.elements)
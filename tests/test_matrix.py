import sys
sys.path.append('src')
from matrix import Matrix

A = Matrix([[0, 1, 2],[3, 6, 9],[2, 6, 8]])

print(A.get_pivot_row(0))

A.swap_rows(0,1)

print(A.elements)

A.normalize_row(0)

print(A.elements)

#print(A.elements)

#print(A.elements)

#print(A.elements)

#print(A.elements)
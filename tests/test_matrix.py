import sys
sys.path.append('src')
from matrix import Matrix

A = Matrix([[0, 1, 2],[3, 6, 9],[2, 6, 8]])

print(A.get_pivot_row(0))

A.swap_rows(0,1)

print(A.elements)

A.normalize_row(0)

print(A.elements)

A.clear_below(0)

assert A.elements == [[1, 2, 3],[0, 1, 2],[0, 2, 2]]

#assert A.get_pivot_row(1) == 1

A.normalize_row(1)

assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 2, 2]]

A.clear_below(1)
print( A.elements)
assert A.elements == [[1, 2, 3], [0, 1, 2], [0, 0, -2]]

#assert
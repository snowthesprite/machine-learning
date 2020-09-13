import sys
sys.path.append('src')
from matrix import Matrix

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

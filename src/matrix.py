class Matrix :
    def __init__(self,element) :
        self.elements = element
        self.num_rows = len(element)
        self.num_cols = len(element[0])

    def copy(self) :
        copied_elemenets = [[entry for entry in row] for row in self.elements]
        return Matrix(copied_elemenets)

    def add(self, matrix) :
        new_elements = [[] for blank in range(self.num_rows)]
        for rows in range(self.num_rows)  :
            for column in range(self.num_cols) : 
                new_elements[rows].append(self.elements[rows][column] + matrix.elements[rows][column])
        return Matrix(new_elements)

    def subtract(self, matrix) :
        new_elements = [[] for blank in range(self.num_rows)]
        for rows in range(self.num_rows) :
            for column in range(self.num_cols) : 
                new_elements[rows].append(self.elements[rows][column] - matrix.elements[rows][column])
        return Matrix(new_elements)

    def matrix_multiply(self, matrix) :
        new_elements = [[] for blank in range(self.num_rows)]
        for rows in range(self.num_rows) :
            for matrix_column in range(matrix.num_cols) :
                end_number = 0
                for column in range(self.num_cols) :
                    end_number += self.elements[rows][column] * matrix.elements[column][matrix_column]
                new_elements[rows].append(end_number)
        return Matrix(new_elements)
        
    def scalar_multiply(self, scalar) :
        new_elements = [[] for blank in range(self.num_rows)]
        for rows in range(self.num_rows) :
            for num in self.elements[rows] :
                new_elements[rows].append(round(num * scalar,1))
        return Matrix(new_elements)

    def transpose(self) :
        new_elements = [[] for blank in range(self.num_cols)]
        for column in range(self.num_cols) :
            for rows in range(self.num_rows) :
                new_elements[column].append(self.elements[rows][column])
        return Matrix(new_elements)

    def is_equal(self, matrix) : 
        for rows in range(self.num_rows)  :
            for column in range(self.num_cols) : 
                if self.elements[rows][column] != matrix.elements[rows][column] :
                    return False
        return True

    def get_pivot_row(self, column_index) :
        for rows in range(self.num_rows) :
            ran = False
            for column in range(0,column_index) :
                if self.elements[rows][column] != 0 :
                    ran = True
            if self.elements[rows][column_index] != 0 and not ran :
                return rows

    def swap_rows(self, row_index1, row_index2) :
        copy = self.copy()
        copy.elements[row_index1], copy.elements[row_index2] = copy.elements[row_index2], copy.elements[row_index1]
        return Matrix(copy.elements)

    def normalize_row(self, row_index) :
        copy = self.copy()
        run = False
        for column in range(copy.num_cols) :
            if copy.elements[row_index][column] != 0 and not run:
                normalizer = copy.elements[row_index][column]
                run = True
        if run :
            for column in range(copy.num_cols) :
                copy.elements[row_index][column] = copy.elements[row_index][column] / normalizer
        return Matrix(copy.elements)

    def clear_below(self, row_index) :
        copy = self.copy()
        run = False
        for column in range(copy.num_cols) :
            if copy.elements[row_index][column] != 0 and not run:
                non_zero = copy.elements[row_index][column]
                col_index = column
                run = True
        if run :
            if non_zero < 0 :
                sign = -1
            elif non_zero > 0 :
                sign = 1
            for rows in range(row_index, copy.num_rows) :
                while copy.elements[rows][col_index] != 0 and rows != row_index :
                    cancleator = copy.elements[rows][col_index] / copy.elements[row_index][col_index]
                    if copy.elements[rows][col_index] < 0 and sign * cancleator <= 0 :
                        sign = sign * -1
                    elif copy.elements[rows][col_index] > 0 and sign * cancleator >= 0 :
                        sign = sign * -1
                    for column in range(copy.num_cols) :
                        copy.elements[rows][column] = copy.elements[rows][column] + (copy.elements[row_index][column] * sign * cancleator)
        return Matrix(copy.elements)

    def clear_above(self, row_index) :
        copy = self.copy()
        run = False
        for column in range(copy.num_cols) :
            if copy.elements[row_index][column] != 0 and not run:
                non_zero = copy.elements[row_index][column]
                col_index = column
                run = True
        if run :
            if non_zero < 0 :
                sign = -1
            elif non_zero > 0 :
                sign = 1
            for rows in range(0, row_index) :
                cancleator = copy.elements[rows][col_index] / copy.elements[row_index][col_index]
                while copy.elements[rows][col_index] != 0 and rows != row_index :
                    if copy.elements[rows][col_index] < 0 and sign * cancleator <= 0 :
                        sign = sign * -1
                    elif copy.elements[rows][col_index] > 0 and sign * cancleator >= 0 :
                        sign = sign * -1
                    for column in range(copy.num_cols) :
                        copy.elements[rows][column] = copy.elements[rows][column] + (copy.elements[row_index][column] * sign * cancleator)
        return Matrix(copy.elements)

    def rref(self) :
        copy = self.copy()
        row_index = 0
        for column in range(copy.num_cols) :
            ran = False
            if copy.get_pivot_row(column) != None and copy.get_pivot_row(column) != row_index :
                copy = copy.swap_rows(copy.get_pivot_row(column), row_index)
            if copy.get_pivot_row(column) != None : 
                ran = True
            copy = copy.normalize_row(row_index)
            copy = copy.clear_below(row_index)
            copy = copy.clear_above(row_index)
            if ran :
                row_index += 1 
            if row_index >= copy.num_rows :
                row_index = 0
        return Matrix(copy.elements)
    
    def augment(self, other_matrix) :
        copy = self.copy()
        for rows in range(copy.num_rows) :
            for nums in other_matrix.elements[rows] :
                copy.elements[rows].append(nums)
        return Matrix(copy.elements)
    
    def get_rows(self, row_nums) :
        given_rows = [self.elements[rows] for rows in row_nums]
        return Matrix(given_rows)

    def get_columns(self, col_nums) :
        given_cols = [[self.elements[rows][column] for column in col_nums] for rows in range(self.num_rows)]
        return Matrix(given_cols)

    def inverse(self) :
        if self.num_cols != self.num_rows :
            print('Error: cannot invert a non-square matrix')
            return
        identity = [[(1 if col == row else 0)  for col in range(0,self.num_cols)] for row in range(0,self.num_rows)]
        self_and_id = self.augment(Matrix(identity))
        self_rref = self_and_id.rref()
        for rows in range(self.num_rows) :
            for column in range(self.num_cols) : 
                if rows == column and self_rref.elements[rows][column] != 1 :
                    print('Error: cannot invert a singular matrix')
                    return
        for rows in range(self.num_rows) :
            for column in range(self.num_cols) : 
                self_rref.elements[rows].pop(0)
        return Matrix(self_rref.elements)
                
    def determinant(self) :
        if self.num_cols != self.num_rows :
            print('Error: cannot calculate determinant of a non-square matrix')
            return
        copy = self.copy()
        row_index = 0
        number_of_swaps = 0
        product_of_scalars = 1
        for column in range(copy.num_cols) :
            ran = False
            if copy.get_pivot_row(column) != None and copy.get_pivot_row(column) != row_index :
                copy = copy.swap_rows(copy.get_pivot_row(column), row_index)
            if copy.get_pivot_row(column) != None : 
                ran = True
            #to find normalizer
            run = False
            for column in range(copy.num_cols) :
                if copy.elements[row_index][column] != 0 and not run:
                    normalizer = copy.elements[row_index][column]
                    run = True
            product_of_scalars = product_of_scalars * normalizer
            copy = copy.normalize_row(row_index)
            copy = copy.clear_below(row_index)
            copy = copy.clear_above(row_index)
            if ran :
                row_index += 1 
            if row_index >= copy.num_rows :
                row_index = 0
        for rows in range(copy.num_rows) :
            for column in range(copy.num_cols) : 
                if rows == column and copy.elements[rows][column] != 1 :
                    ran = False
                    for rows2 in range(copy.num_rows) :
                        if copy.elements[rows2][column] == 1 :
                            number_of_swaps += 1
                            copy = copy.swap_rows(rows,rows2)
                            ran = True
                        elif not ran :
                            return 0
                elif rows != column and copy.elements[rows][column] != 0 :
                    return 0
        return ((-1) ** number_of_swaps) * product_of_scalars

    def exponent(self, expo) :
        copy = self.copy()
        current_expo = 1
        while current_expo < expo :
            copy = self.matrix_multiply(copy)
            current_expo += 1
        return copy

    def __add__(self, other) :
        return self.add(other)

    def __sub__(self, other) :
        return self.subtract(other)

    def __mul__(self, other) :
        return self.scalar_multiply(other)

    def __matmul__(self, other) :
        return self.matrix_multiply(other)

    def __eq__(self, other) :
        return self.is_equal(other)
    
    def split_matrix(self, row, column) :
        new_elements = [[] for _ in range(self.num_rows - 1)]
        for row_index in range(self.num_rows) :
            for col_index in range(self.num_cols) :
                if row_index != row and col_index != column :
                    new_elements[row_index - 1].append(self.elements[row_index][col_index])
        return Matrix(new_elements)

    def cofactor_method_determinant(self) :
        if self.num_cols != self.num_rows :
            print('Error: cannot calculate determinant of a non-square matrix')
            return
        determinant = 0
        if self.num_cols > 1 :
            for test in range(self.num_cols) :
                new_matrix = self.split_matrix(0, test)
                det = new_matrix.cofactor_method_determinant()
                if type(det) != int and type(det) != float :
                    determinant += self.elements[0][test] * det.elements[0][0] * ((-1) ** test)
                else :
                    determinant += self.elements[0][test] * det * ((-1) ** test)
            return determinant
        else : 
            return self
        
    def __rmul__ (self, other) :
        return self.scalar_multiply(other)

    def __pow__ (self, other) :
        return self.exponent(other)

    

#This is just clear above AND below, but keep it just in case
'''def clear_below(self, row_index) :
        run = False
        for column in range(self.num_cols) :
            if self.elements[row_index][column] != 0 and not run:
                non_zero = self.elements[row_index][column]
                col_index = column
                run = True
        if non_zero < 0 :
            sign = -1
        elif non_zero > 0 :
            sign = 1
        for rows in range(self.num_rows) :
            while self.elements[rows][col_index] != 0 and rows != row_index :
                if self.elements[rows][col_index] < 0 and sign == -1 :
                    sign = 1
                elif self.elements[rows][col_index] > 0 and sign == 1 :
                    sign = -1
                for column in range(self.num_cols) :
                    self.elements[rows][column] = self.elements[rows][column] + (self.elements[row_index][column] * sign)'''

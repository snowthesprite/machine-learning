class Matrix :
    def __init__(self,element) :
        self.elements = element
        self.num_rows = len(element)
        self.num_cols = len(element[0])

    def copy(self) :
        return self

    def add(self, matrix) :
        new_elements = [[] for blank in range(self.num_rows)]
        for rows in range(self.num_rows)  :
            for collums in range(self.num_cols) : 
                new_elements[rows].append(self.elements[rows][collums] + matrix.elements[rows][collums])
        return Matrix(new_elements)


    def subtract(self, matrix) :
        new_elements = [[] for blank in range(self.num_rows)]
        for rows in range(self.num_rows) :
            for collums in range(self.num_cols) : 
                new_elements[rows].append(self.elements[rows][collums] - matrix.elements[rows][collums])
        return Matrix(new_elements)

    def matrix_multiply(self, matrix) :
        new_elements = [[] for blank in range(self.num_rows)]
        for rows in range(self.num_rows) :
            for matrix_collums in range(matrix.num_cols) :
                end_number = 0
                for collums in range(self.num_cols) :
                    end_number += self.elements[rows][collums] * matrix.elements[collums][matrix_collums]
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
        for collums in range(self.num_cols) :
            for rows in range(self.num_rows) :
                new_elements[collums].append(self.elements[rows][collums])
        return Matrix(new_elements)

    def is_equal(self, matrix) : 
        for rows in range(self.num_rows)  :
            for collums in range(self.num_cols) : 
                if self.elements[rows][collums] != matrix.elements[rows][collums] :
                    return False
        return True

    def get_pivot_row(self, column_index) :
        for rows in range(self.num_rows) :
            if self.elements[rows][column_index] != 0 :
                return rows

    def swap_rows(self, row_index1, row_index2) :
        self.elements[row_index1], self.elements[row_index2] = self.elements[row_index2], self.elements[row_index1]

    def normalize_row(self, row_index) :
        run = False
        for collums in range(self.num_cols) :
            if self.elements[row_index][collums] != 0 and not run:
                normalizer = self.elements[row_index][collums]
                run = True
        for collums in range(self.num_cols) :
            self.elements[row_index][collums] = int(self.elements[row_index][collums] / normalizer)


    def clear_below(self, row_index) :
        run = False
        for collums in range(self.num_cols) :
            if self.elements[row_index][collums] != 0 and not run:
                non_zero = self.elements[row_index][collums]
                col_index = collums
                run = True
        if non_zero < 0 :
            sign = -1
        elif non_zero > 0 :
            sign = 1
        for rows in range(row_index, self.num_rows) :
            while self.elements[rows][col_index] != 0 and rows != row_index :
                if self.elements[rows][col_index] < 0 and sign == -1 :
                    sign = 1
                elif self.elements[rows][col_index] > 0 and sign == 1 :
                    sign = -1
                for collums in range(self.num_cols) :
                    self.elements[rows][collums] = self.elements[rows][collums] + (self.elements[row_index][collums] * sign)

    def clear_above(self, row_index) :
        run = False
        for collums in range(self.num_cols) :
            if self.elements[row_index][collums] != 0 and not run:
                non_zero = self.elements[row_index][collums]
                col_index = collums
                run = True
        if non_zero < 0 :
            sign = -1
        elif non_zero > 0 :
            sign = 1
        for rows in range(self.num_rows, row_index) :
            while self.elements[rows][col_index] != 0 and rows != row_index :
                if self.elements[rows][col_index] < 0 and sign == -1 :
                    sign = 1
                elif self.elements[rows][col_index] > 0 and sign == 1 :
                    sign = -1
                for collums in range(self.num_cols) :
                    self.elements[rows][collums] = self.elements[rows][collums] + (self.elements[row_index][collums] * sign)




#This is just clear above AND below, but keep it just in case
'''def clear_below(self, row_index) :
        run = False
        for collums in range(self.num_cols) :
            if self.elements[row_index][collums] != 0 and not run:
                non_zero = self.elements[row_index][collums]
                col_index = collums
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
                for collums in range(self.num_cols) :
                    self.elements[rows][collums] = self.elements[rows][collums] + (self.elements[row_index][collums] * sign)'''

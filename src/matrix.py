class Matrix :
    def __init__(self,element) :
        self.elements = element

    def copy(self) :
        return self

    def add(self, matrix) :
        new_elements = [[],[]]
        outer_leng = 0
        while outer_leng < 2 :
            inner_leng = 0
            while inner_leng < 2 : 
                new_elements[outer_leng].append(self.elements[outer_leng][inner_leng] + matrix.elements[outer_leng][inner_leng])
                inner_leng += 1
            outer_leng += 1
        return Matrix(new_elements)


    def subtract(self, matrix) :
        new_elements = [[],[]]
        outer_leng = 0
        while outer_leng < 2 :
            inner_leng = 0
            while inner_leng < 2 : 
                new_elements[outer_leng].append(self.elements[outer_leng][inner_leng] - matrix.elements[outer_leng][inner_leng])
                inner_leng += 1
            outer_leng += 1
        return Matrix(new_elements)

    def matrix_multiply(self, matrix) :
        top_left_elements = self.elements[0][0] * matrix.elements[0][0] + self.elements[0][1] * matrix.elements[1][0]
        top_right_elements = self.elements[0][0] * matrix.elements[0][1] + self.elements[0][1] * matrix.elements[1][1]
        bottom_left_elements = self.elements[1][0] * matrix.elements[0][0] + self.elements[1][1] * matrix.elements[1][0]
        bottom_right_elements = self.elements[1][0] * matrix.elements[0][1] + self.elements[1][1] * matrix.elements[1][1]
        new_elements = [[top_left_elements, top_right_elements], [bottom_left_elements, bottom_right_elements]]
        return Matrix(new_elements)
        
    def scalar_multiply(self, scalar) :
        new_elements = [[],[]]
        outer_leng = 0
        while outer_leng < 2 :
            inner_leng = 0
            while inner_leng < 2 : 
                new_elements[outer_leng].append(self.elements[outer_leng][inner_leng] * scalar)
                inner_leng += 1
            outer_leng += 1
        return Matrix(new_elements)

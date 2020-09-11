class Matrix :
    def __init__(self,element) :
        self.elements = element
        self.num_rows = len(element)
        self.num_cols = len(element[0])

    def copy(self) :
        return self

    def add(self, matrix) :
        new_elements = [[] for blank in range(self.num_rows)]
        rows = 0
        while rows < self.num_rows  :
            collums = 0
            while collums < self.num_cols : 
                new_elements[rows].append(self.elements[rows][collums] + matrix.elements[rows][collums])
                collums += 1
            rows += 1
        return Matrix(new_elements)


    def subtract(self, matrix) :
        new_elements = [[] for blank in range(self.num_rows)]
        rows = 0
        while rows < self.num_rows  :
            collums = 0
            while collums < self.num_cols : 
                new_elements[rows].append(self.elements[rows][collums] - matrix.elements[rows][collums])
                collums += 1
            rows += 1
        return Matrix(new_elements)

    def matrix_multiply(self, matrix) :
        top_left_elements = self.elements[0][0] * matrix.elements[0][0] + self.elements[0][1] * matrix.elements[1][0]
        top_right_elements = self.elements[0][0] * matrix.elements[0][1] + self.elements[0][1] * matrix.elements[1][1]
        bottom_left_elements = self.elements[1][0] * matrix.elements[0][0] + self.elements[1][1] * matrix.elements[1][0]
        bottom_right_elements = self.elements[1][0] * matrix.elements[0][1] + self.elements[1][1] * matrix.elements[1][1]
        new_elements = [[top_left_elements, top_right_elements], [bottom_left_elements, bottom_right_elements]]
        return Matrix(new_elements)
        
    def scalar_multiply(self, scalar) :
        new_elements = [[] for blank in range(self.num_rows)]
        rows = 0
        while rows < self.num_rows :
            for num in self.elements[rows] :
                new_elements[rows].append(round(num * scalar,1))
            rows += 1
        return Matrix(new_elements)

    def transpose(self) :
        new_elements = [[] for blank in range(self.num_cols)]
        collums = 0
        while collums < self.num_cols :
            rows = 0
            while rows < self.num_rows :
                new_elements[collums].append(self.elements[rows][collums])
                rows += 1
            collums += 1
        return Matrix(new_elements)

    def is_equal(self, matrix) : 
        rows = 0
        while rows < self.num_rows  :
            collums = 0
            while collums < self.num_cols : 
                if self.elements[rows][collums] != matrix.elements[rows][collums] :
                    return False
                collums += 1
            rows += 1
        return True
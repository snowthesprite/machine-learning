from matrix import Matrix

class Simplex () :
    def __init__(self, matrix) :
        self.matrix = matrix
        self.maximum = (lambda : [max for max in self.matrix.elements[-1]])
        self.ans = (lambda : [row[-1] for row in self.matrix.elements])

        self.add_slack_var()

        self.org_max = self.matrix.elements[-1]
    
    def add_slack_var(self) :
        slack_var = self.matrix.num_rows - 1
        #print(slack_var)
        for slack_num in range(slack_var) :
            #print(self.maximum())
            for row_num in range(self.matrix.num_rows) :
                if slack_num == row_num :
                    self.matrix.elements[row_num].insert(-1, 1)
                else :
                    self.matrix.elements[row_num].insert(-1, 0)
            self.matrix.num_cols += 1

    def pick_max_var(self) :
        maximum = self.maximum()
        maximum.pop(-1)
        max = (0, None) 
        for var_num in range(len(maximum)) :
            if maximum[var_num] > max[0] :
                max = (maximum[var_num], var_num)
        return max[1]

    
    def pick_best_constraint(self, var) : 
        ans = self.ans()
        ans.pop(-1)
        best = (ans[0], None)
        for row_num in range(len(ans)) :
            var_coeff = self.matrix.elements[row_num][var]
            #print(ans[row_num]/var_coeff)
            #print(0 < (ans[row_num]/var_coeff) < best[0])
            if 0 < (ans[row_num]/var_coeff) < best[0] :
                best = (ans[row_num]/var_coeff, row_num)
        return best[1]
    
    def check(self) :
        pass
    
    def run(self) :
        while True :
            print(self.maximum())
            max_var = self.pick_max_var()
            #print(max_var)
            if max_var == None :
                return
            chosen_row = self.pick_best_constraint(max_var)
            print()
            self.matrix = self.matrix.normalize_row(chosen_row, max_var)
            self.matrix = self.matrix.clear_above(chosen_row, max_var)
            self.matrix = self.matrix.clear_below(chosen_row, max_var)
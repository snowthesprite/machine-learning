from matrix import Matrix
class LinearRegressor :
    def __init__(self, data_frame, dependent_variable) :
        self.data_frame = data_frame
        self.depend_var = dependent_variable
        self.coefficients = self.calculate_coefficient()
        self.funct = lambda a : a

    def calculate_coefficient(self) :
        dict_data = self.data_frame.data_dict
        y_points = Matrix([[dict_data[self.depend_var][col_index]] for col_index in range(len(dict_data[self.depend_var]))])
        independ_var = [] 
        for x in dict_data :
            if x != self.depend_var :
                independ_var.append(x)
        eqn = [[1] for blank in range(len(dict_data[independ_var[0]]))]
        for row_index in range(len(dict_data[independ_var[0]])) :
            for var in independ_var :
                eqn[row_index].append(dict_data[var][row_index])
        line_eqn = Matrix(eqn)
        t_line_eqn = line_eqn.transpose()
        t_n_line = t_line_eqn @ line_eqn
        inverse_t_n_line = t_n_line.inverse()
        solved_line_eqn = t_line_eqn @ y_points
        solved_line_eqn = inverse_t_n_line @ solved_line_eqn
        done = solved_line_eqn.transpose().elements[0]
        for x in range(len(done)) :
            done[x] = round(done[x], 8)
        finished_dict = {'constant' : done[0]}
        for index in range(len(independ_var)) :
            finished_dict[independ_var[index]] = done[index + 1]
        return finished_dict
    
    def predict(self, predictor) :
        val = [1]
        for x in predictor.values() :
            val.append(x)
        coef_val = list(self.coefficients.values())
        y = 0
        for index in range(len(val)) :
            y += coef_val[index] * val[index]
        return self.funct(y)
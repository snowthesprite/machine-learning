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
        independ_var = [x for x in dict_data if x != self.depend_var] 
        eqn = [[1] for _ in range(len(dict_data[self.depend_var]))]
        for row_index in range(len(dict_data[self.depend_var])) :
            for var in independ_var :
                eqn[row_index].append(dict_data[var][row_index])
        line_eqn = Matrix(eqn)
        #print(line_eqn.elements)
        t_line_eqn = line_eqn.transpose()
        t_n_line = t_line_eqn @ line_eqn
        inverse_t_n_line = t_n_line.inverse()
        solved_line_eqn = t_line_eqn @ y_points
        solved_line_eqn = inverse_t_n_line @ solved_line_eqn
        done = solved_line_eqn.transpose().elements[0]
        finished_dict = {'constant' : done[0]}
        for index in range(len(independ_var)) :
            finished_dict[independ_var[index]] = done[index + 1]
        return finished_dict
    
    def predict(self, predictor) :
        predict = predictor.copy()
        #creates interaction terms if they exist
        for key in self.data_frame.columns :
            if '*' in key :
                sub_keys = key.split(' * ')
                predict[key] = 1
                for key_1 in sub_keys :
                    predict[key] = predict[key] * predict[key_1]
                
        predict_keys = [key for key in predict]
        predict_keys.insert(0, 'constant')
        val = [1]
        for x in predict.values() :
            val.append(x)
        coef_val = [self.coefficients[key] if key in list(self.coefficients.keys()) else 0 for key in predict_keys]
        y = 0
        for index in range(len(val)) :
            y += coef_val[index] * val[index]
        return self.funct(y)
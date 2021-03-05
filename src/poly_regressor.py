from dataframe import DataFrame
from linear_regressor import LinearRegressor

class PolynomialRegressor (LinearRegressor) :
    def __init__(self, degree) :
        self.degree = degree
        self.data_frame = None
        self.depend_var = None
        self.coefficients = None

    def fit (self, dataframe, dependent_variable) :
        self.data_frame = dataframe
        dict_data = self.data_frame.data_dict
        self.depend_var = dependent_variable
        independ_var = [var for var in dict_data if var != self.depend_var][0]
        if self.degree == 0 :
            self.data_frame = DataFrame({self.depend_var : dict_data[self.depend_var]}, [self.depend_var])
        for degree in range(1, self.degree) :
            col = independ_var + '^' + str(degree + 1)
            col_val = [dict_data[independ_var][index] ** (degree + 1) for index in range(len(dict_data[independ_var]))]
            self.data_frame = self.data_frame.add_data(col, col_val)
        self.coefficients = self.calculate_coefficient()

    def predict(self, predictor) :
        predict = predictor.copy()
        for key in self.data_frame.columns :
            if '^' in key :
                key_n_pwr = key.split('^')
                predict[key] = predict[key_n_pwr[0]] ** int(key_n_pwr[1])

        predict_keys = [key for key in predict]
        predict_keys.insert(0, 'constant')
        val = [x for x in predict.values()]
        val.insert(0, 1)
        coef_val = [self.coefficients[key] if key in list(self.coefficients.keys()) else 0 for key in predict_keys]
        y = 0
        for index in range(len(val)) :
            y += coef_val[index] * val[index]
        return y
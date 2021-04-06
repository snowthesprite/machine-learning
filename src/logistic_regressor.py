from linear_regressor import LinearRegressor
from dataframe import DataFrame
import math

class LogisticRegressor (LinearRegressor):
    def __init__(self, data_frame, dependent_variable, premade = False, upper_bound = 1) :
        self.depend_var = dependent_variable
        self.up_bound = upper_bound
        self.data_frame = data_frame
        if not premade :
            self.data_frame = self.transform(data_frame)
            self.coefficients = self.calculate_coefficient()
        else :
            self.data_frame = data_frame
        self.funct = lambda a : self.up_bound / (1 + math.exp(a))
    
    def transform(self, df) :
        dict_data = df.data_dict
        transformed_df = dict_data.copy()
        for index in range(len(dict_data[self.depend_var])) :
            element = dict_data[self.depend_var][index]
            if element == 0 :
                element = 0.1
            if element == 1 :
                element = 0.9
            transformed_df[self.depend_var][index] = math.log((self.up_bound/element) - 1)
        return DataFrame(transformed_df, df.columns)
    
    def calc_rss(self) :
        dict_data = self.data_frame.data_dict
        rss = 0
        independ_vars = [key for key in dict_data.keys() if key != self.depend_var]
        for index in range(len(dict_data[self.depend_var])) :
            predicting = {var : dict_data[var][index] for var in independ_vars}
            actual_y = dict_data[self.depend_var][index]
            rss += (actual_y - self.predict(predicting)) ** 2
        return rss

    def set_coefficients(self, coeffs) :
        self.coefficients = coeffs

    def calc_gradient(self, delta) :
        original = self.coefficients.copy()
        reMix_coeff = self.coefficients
        gradient = {}
        for var in original :
            parts = []
            for sign in [1,-1] :
                reMix_coeff[var] += delta * sign
                parts.append(self.calc_rss())
                reMix_coeff[var] = original[var]
            gradient[var] = (parts[0]-parts[1])/(2*delta)
        return gradient
            
    def gradient_descent(self, alpha, delta, num_steps, debug_mode = False) :
        independ_vars = [key for key in self.coefficients if key != self.depend_var]
        if debug_mode :
            print('Independent Variables:', independ_vars)
            print('Dependent Variable:', self.depend_var)
            print('Alpha, Delta, Num Steps:', alpha, delta, num_steps)
        for _ in range(num_steps) :
            gradient = self.calc_gradient(delta)
            if debug_mode :
                print('Current Step:', _)
                print('Gradient', gradient)
            for key in independ_vars :
                if debug_mode :
                    print('Old ' + key + ':', self.coefficients[key])
                    print('New ' + key + ':', self.coefficients[key] - alpha * gradient[key])
                self.coefficients[key] -= alpha * gradient[key]
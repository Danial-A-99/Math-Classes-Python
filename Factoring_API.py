import math
from Polynomial_API import Polynomial_Function

class Factoring_Function:

    def __init__(self,equation):
        self.equation = equation

    def split_values(self):
        splitting = Polynomial_Function(self.equation)
        constants = splitting.sep_c_v_e()[0]
        variables = splitting.sep_c_v_e()[1]
        exponents = splitting.sep_c_v_e()[2]

    def only_d_value(self,d_val,coefficients,variables,exponents):
        possible_x_intercepts = []
        for i in range(d_val):
            if i == d_val:
                possible_x_intercepts.append(i)
                break
            elif (d_val/i)%2 ==0:
                    possible_x_intercepts.append(i)
        
        xval = None
        for x_intercept in possible_x_intercepts:
            factor1 = eval(self.equation.replace(variables,f"*({x_intercept})**"))
            factor2 = eval(self.equation.replace(variables,f"*({-x_intercept})**"))
            if factor1 == 0:
                xval = x_intercept
                break
            elif factor2 == 0:
                xval = -x_intercept
                break
                
        first_coeff_value = coefficients[0]
        new_coeff_values = []
        new_coeff_values.append(first_coeff_value)
        for coeff in coefficients[0:]:
            tempcoeff = (new_coeff_values[-1]*xval) + coeff
            new_coeff_values.append(tempcoeff)

        if new_coeff_values[-1] == 0:
            new_coeff_values.pop(-1)
        
        finalized_equation = []
        for exp in exponents:
            pass
        
                


    def a_and_d_values(self):
        pass
        # = d/a
import math
from Polynomial_API import Polynomial_Function

class Factoring_Function:

    def __init__(self,equation=''):
        self.equation = equation

    def set_equation(self,equation):
        self.equation = equation

    def split_values(self):
        splitting = Polynomial_Function(self.equation)
        constants = splitting.sep_c_v_e()[0]
        variables = splitting.sep_c_v_e()[1]
        exponents = splitting.sep_c_v_e()[2]
        return constants,variables,exponents

    def only_d_value(self):
        constants = self.split_values()[0]
        variables = self.split_values()[1]
        exponents = self.split_values()[2]
        d_val = int(constants[-1])

        possible_x_intercepts = []
        for i in range(1,d_val):
            if i == d_val:
                possible_x_intercepts.append(i)
                break
            elif (d_val/i)%2 == 0:
                    possible_x_intercepts.append(i)
        
        xval = 1 #temporary - should be None
        for x_intercept in possible_x_intercepts:
            factor1 = eval(self.equation.replace(variables[0],f"*({x_intercept})**").replace("^",""))
            factor2 = eval(self.equation.replace(variables[0],f"*({-x_intercept})**").replace("^",""))
            if factor1 == 0:
                xval = x_intercept
                break
            elif factor2 == 0:
                xval = -x_intercept
                break
                
        first_coeff_value = constants[0]
        new_coeff_values = []
        new_coeff_values.append(first_coeff_value)
        for coeff in constants[0:]:
            tempcoeff = (new_coeff_values[-1]*xval) + coeff
            new_coeff_values.append(tempcoeff)

        remainder = new_coeff_values[-1]
        new_coeff_values.pop(-1)

        
        finalized_equation = []
        for i in range(len(new_coeff_values)):
            final_term = f"{new_coeff_values[i]}{variables[i]}^{float(exponents[i].replace("^",""))-1}"
            finalized_equation.append(final_term)
        
        finalized_equation = " + ".join(finalized_equation)
        finalized_equation += f"({variables[0]} + {xval})"

        return finalized_equation

    def a_and_d_values(self):
        pass
        # = d/a

if __name__ == "__main__":
    obje = Factoring_Function("1x^3 - 6x^2 + 11x^1 - 6)")
    equation = obje.only_d_value()
    print(equation)
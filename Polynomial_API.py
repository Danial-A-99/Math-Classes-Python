from Freq_Math import frequent_functions

class Polynomial_Function:
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
                "o","p","q","r","s","t","u","v","w","x","y","z"]
    
    def __init__(self,equation:str):
        self.equation = equation
    
    def sep_term(self):
        terms = []
        og_term_list = self.equation.split(" ")
        x = 0
        for i in range(len(og_term_list)):
            try:
                if og_term_list[x] in ("+","-","/","*"):
                    terms.append(f"{og_term_list[x]}{og_term_list[x+1]}")
                    x += 1
                else:
                    terms.append(og_term_list[x])
                x += 1
            except IndexError:
                pass
        return terms

    def sep_c_v_e(self):
        terms = self.sep_term()
        coeffs = []
        variables = []
        exponenets = []
        for term in terms:
            i = 0
            for val in term:
                if val in self.alphabet:
                    variables.append(val)
                    temp_term = term.split(val)
                    coeffs.append(temp_term[0])
                    exponenets.append(temp_term[1])
                    break
                else:
                    i += 1
        return coeffs,variables,exponenets

    def group_similar_vals(self): 
        coef,var,exp = self.sep_c_v_e()
        i=0
        new_coef,new_var,new_exp = [],[],[]

        while True:
            try: # fix up logic
                if var[i] == var[i+1] and exp[i] == exp[i+1]:
                    new_coef.append(float(coef[i]) + float(coef[i+1]))
                    new_var.append(var[i])
                    new_exp.append(exp[i])
                    i += 1
                else:
                    new_coef.append(coef[i])
                    new_var.append(var[i])
                    new_exp.append(exp[i])
                i += 1
            except IndexError:
                new_coef.append(coef[-1])
                new_var.append(var[-1])
                new_exp.append(exp[-1])
                break

        return new_coef,new_var,new_exp
    
    def exponent_replacer(self,equation):
        equation = (equation.replace("^0","⁰^").replace("^1","¹^").replace("^2","²^").replace("^3","³^").replace("^4","⁴^").replace("^5","⁵^").replace("^6","⁶^").replace("^7","⁷^").replace("^8","⁸^").replace("^9","⁹^").replace("^-0","⁻⁰^").replace("^-1","⁻¹^").replace("^-2","⁻²^").replace("^-3","⁻³^").replace("^-4","⁻⁴^").replace("^-5","⁻⁵^").replace("^-6","⁻⁶^").replace("^-7","⁻⁷^").replace("^-8","⁻⁸^").replace("^-9","⁻⁹^"))
        if "^" not in equation:
            print(equation)
        else:
            while True:
                equation = (equation.replace("^0","⁰^").replace("^1","¹^").replace("^2","²^").replace("^3","³^").replace("^4","⁴^").replace("^5","⁵^").replace("^6","⁶^").replace("^7","⁷^").replace("^8","⁸^").replace("^9","⁹^").replace("^-0","⁻⁰^").replace("^-1","⁻¹^").replace("^-2","⁻²^").replace("^-3","⁻³^").replace("^-4","⁻⁴^").replace("^-5","⁻⁵^").replace("^-6","⁻⁶^").replace("^-7","⁻⁷^").replace("^-8","⁻⁸^").replace("^-9","⁻⁹^"))
                equation = equation.strip()
                if equation[-2] == "^" or "^0" not in equation or "^1" not in equation or "^2" not in equation or "^3" not in equation or "^4" not in equation or "^5" not in equation or "^6" not in equation or "^7" not in equation or "^8" not in equation or "^9" not in equation:
                    if "^0" in equation or "^1" in equation or "^2" in equation or "^3" in equation or "^4" in equation or "^5" in equation or "^6" in equation or "^7" in equation or "^8" in equation or "^9" in equation:
                        pass
                    else:
                        equation = equation.replace("^","")
                        break
                else:
                    pass
        return equation

    def regroup_terms(self):
        coeffs,var,exp = self.group_similar_vals()
        final_equation = ""
        for i in range(len(coeffs)):
            final_equation += (f"{str((coeffs[i]))}{var[i]}{exp[i]} + ")
        equation = self.exponent_replacer(final_equation.replace(" + -"," - ").replace(" + +"," + ")[:-2])
        return equation

class Polynomial_Details:
    def __init__(self,equation):
        self.equation = equation
        obje = Polynomial_Function(self.equation)
        self.constants = obje.sep_c_v_e()[0]
        self.variables = obje.sep_c_v_e()[1]
        self.exponents = obje.sep_c_v_e()[2]
    
    def e_and_c_of_func(self):
        location = self.exponents.index(max(self.exponents))
        degree_of_func = self.exponents[location]
        coefficient_of_func = self.constants[location]
        return degree_of_func,coefficient_of_func
    
    def even_deg_func(self):
        if self.e_and_c_of_func()[0] %2 == 0:
            state = True
        else:
            state = False
        return state

    def end_behavior(self):
        coeff = self.e_and_c_of_func[1]
        if self.even_deg_func() and coeff > 0:
            end_behavior = "Q2 -> Q1"
        elif self.even_deg_func() == False and coeff > 0: 
            end_behavior = "Q3 -> Q1"
        elif self.even_deg_func() and coeff < 0:
            end_behavior = "Q3 -> Q4"
        elif self.even_deg_func() == False and coeff < 0:
            end_behavior = "Q2 -> Q4"
        return end_behavior
    
    def domain_range_with_inf(self):
        end_behave = self.end_behavior()
        if end_behave == "Q2 -> Q1":
            func_domain,func_range = "[XER | x = ±∞]","[YER | y = ∞]"
        elif end_behave == "Q2 -> Q4":
            func_domain,func_range = "[XER | x = ±∞]","[YER | y = ±∞]"
        elif end_behave == "Q3 -> Q1":
            func_domain,func_range = "[XER | x = ±∞]","[YER | y = ±∞]"
        elif end_behave == "Q3 -> Q4":
            func_domain,func_range = "[XER | x = ±∞]","[YER | y = -∞]"
        return func_domain,func_range
    
    def symetry_type(self):
        if self.even_deg_func():
            symetry_type = "line symetry"
        else:
            symetry_type = "point symetry"
        return symetry_type

    def lead_coeff_finite_diff(self,ycoords):
        turns = 0
        while True:
            diff_list = []
            if ycoords[1] - ycoords[0] == 0:
                break
            else:
                x = 0
                for i in range(1,len(ycoords)):
                    diff_list.append(ycoords[i]-x)
                    x+=1
            ycoords = diff_list
            turns +=1

        n_val = frequent_functions()
        n_val = n_val.factorial(turns)
        lead_coeff = ycoords[0]/n_val 
        return lead_coeff
    
    def max_turning_poins(self):
        degree = self.e_and_c_of_func()[0]
        return degree - 1
    
    def func_transformations(self):
        equation = self.equation
        temp_equation = equation.replace("("," ").replace(")"," ")
        obje = Polynomial_Function(temp_equation)
        new_equation = obje.sep_term()
        a_val = new_equation[0]
        k_val = new_equation[1]
        #x_var = new_equation[2]
        d_val = new_equation[3]
        #n_val = new_equation[4]
        c_val = new_equation[5]
        x_transformations = f"x/{k_val} + {d_val}"
        y_transformations = f"{a_val}y + {c_val}"
        return x_transformations,y_transformations
    
    def aroc(self,x1,y1,x2,y2):
        avg_roc = (y2-y1)/(x2-x1)
        return avg_roc
    
    def iroc(self,prev_x,prev_y,main_x,main_y,aftr_x,aftr_y):
        slope1 = self.aroc(prev_x,prev_y,main_x,main_y)
        slope2 = self.aroc(main_x,main_y,aftr_x,aftr_y)
        avg_iroc = (slope1 + slope2) / 2
        return avg_iroc
    

if __name__ == "__main__":
    obje = Polynomial_Function("3x^10 + 4x^10 + 7x^8 - 6x^6 + 5x^6 - 12x^5 - 3x^5 + 4x^4 - 0.25x^1")

    print(obje.regroup_terms())

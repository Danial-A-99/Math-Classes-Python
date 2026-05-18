

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


if __name__ == "__main__":
    obje = Polynomial_Function("3x^10 + 4x^10 + 7x^8 - 6x^6 + 5x^6 - 12x^5 - 3x^5 + 4x^4 - 0.25x^1")

    print(obje.regroup_terms())

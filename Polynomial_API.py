

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
                    new_coef.append(coef[i] + coef[i+1])
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

    def regroup_terms(self):
        coeffs,var,exp = self.group_similar_vals()
        final_equation = ""
        for i in range(len(coeffs)):
            final_equation += (f"{str(eval(coeffs[i]))}{var[i]}{exp[i]} + ")
        return final_equation.replace(" + -"," - ")[:-2]

obje = Polynomial_Function("2x^6 - 4x^6 + 5b^9 - 6b^9 + 7c^1 + 7c^1")

print(obje.regroup_terms())

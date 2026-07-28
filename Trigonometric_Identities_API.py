from Polynomial_API import Polynomial_Function 

class Trigonometric_Identities:
    trig_Id = {"cscθ":"1/sinθ",
               "secθ":"1/cosθ",
               "cotθ":"1/tanθ",
               "sinθ/cosθ":"tanθ",
               "sin²θ+cos²θ": 1}

    def __init__(self,equation):
        self.equation = equation

    def seperate_ls_rs(self):
        self.equation = self.equation.replace("sin²θ + cos²θ","sin²θ+cos²θ")
        ls = self.equation.split(" = ")[0]
        rs = self.equation.split(" = ")[1]
        return ls,rs
    
    def seperate_ls_rs_terms(self):
        new_ls = Polynomial_Function(self.seperate_ls_rs()[0])
        new_rs = Polynomial_Function(self.seperate_ls_rs()[1])
        ls_terms = new_ls.sep_term()
        rs_terms = new_rs.sep_term()
        return ls_terms,rs_terms
    
    def pick_side_to_simplify(self):
        ls = self.seperate_ls_rs_terms()[0]
        rs = self.seperate_ls_rs_terms()[1]
        if len(ls) > len(rs):
            side_to_simplify = ls
            side_to_compare = rs
        else:
            side_to_simplify = rs
            side_to_compare = ls
        return side_to_simplify,side_to_compare
    
    def mutate_side(self):
        side = self.pick_side_to_simplify()[0]


if __name__ == "__main__":

    obje = Trigonometric_Identities("sin²θ + cos²θ / 2 = 1/tanθ")

    print(obje.pick_side_to_simplify()[0])



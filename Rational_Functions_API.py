from Factoring_API import Factoring_Function

class Rational_Functions_Func:

    def __init__(self):
        self.numerator_func = ""
        self.denomenator_func = ""

    def set_numer_func(self,new_func):
        self.numerator_func = new_func

    def set_denom_func(self,new_func):
        self.denomenator_func = new_func

    def check_ration_or_recip(self):
        if len(self.numerator_func.split(" ")) < 2:
            return "recipriocal function"
        else:
            return "rational_function"

    def find_roots(self):
        if self.check_ration_or_recip() == "rational_function":
            numer_roots = Factoring_Function(self.numerator_func)#Fix
            denom_roots = Factoring_Function(self.denomenator_func)#Fix
            return numer_roots.only_d_value(),denom_roots.only_d_value()
        else:
            denom_roots = Factoring_Function(self.denomenator_func)#Fix
            return denom_roots.only_d_value()

    def find_horizontal_asymptotes(self):
        for valu in self.find_roots()[-1]:
            temp_val = valu.replace("(","").replace(")","")
            temp_val = temp_val.split("x")
            print(temp_val)
            print(temp_val) 
            print(temp_val)

if __name__ == "__main__":
    obje = Rational_Functions_Func()
    obje.set_numer_func("2")
    obje.set_denom_func("-x + 3")
    obje.find_horizontal_asymptotes()


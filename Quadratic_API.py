

class Quadratic_Function:
    
    def __init__(self,a:float,b:float,c:float):
        self.a = a
        self.b = b
        self.c = c
    
    def set_a_val(self,newval):
        self.a = newval

    def set_b_val(self,newval):
        self.b = newval

    def set_c_val(self,newval):
        self.c = newval

    def get_a_val(self):
        return self.a 

    def get_b_val(self):
        return self.b

    def get_c_val(self):
        return self.c
    
    def get_discriminant(self):
        return self.b**2 - 4*self.a*self.c
    
    def roots_exist(self):
        return self.get_discriminant() >= 0

    def roots_finder(self):
        if self.roots_exist():
            return [(-self.b+(self.get_discriminant())**0.5)/(2*self.a),
                    (-self.b-(self.get_discriminant())**0.5)/(2*self.a)]
        else:
            return []
        
    def display_root_form(self):
        if self.roots_exist():
            print(f"f(x) = {self.a}(x - {self.roots_finder()[0]}) (x - {self.roots_finder()[1]})")
        else:
            print("No Real Roots Exist")

    def display_standard_form(self):
        print(f"f(x) = {self.a}x² + {self.b}x + {self.c}")
    
    def display_point_slope_form(self):
        print(f"f(x) = {self.a}(x + {((self.b/self.a)/2)})² + {self.c-(self.a*(((self.b/self.a)/2)**2))}".replace("+ -","- ").replace(" 1(",""))
        
    def y_intercept(self):
        return self.c
    
    def max_value(self):
        return self.a <= 0
    
if __name__ == "__main__":
    obje = Quadratic_Function(1,5,6)
    obje.display_standard_form()
    obje.display_point_slope_form()
    obje.display_root_form()
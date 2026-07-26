

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

    def get_discriminant_with_steps(self):
        print("\nSolving For Discriminant Steps:")
        print(f"Step 1 (Sub in values):\n d = ({self.b})^2 - 4({self.a})({self.c})")
        print(f"Step 2 (Solve individual values):\n d = ({self.b**2}) - {4*self.a*self.c}")
        print(f"Step 3 (Perform final calculations):\n d = {self.b**2 - 4*self.a*self.c}")
        print(f"{"_":_^40}")
        return self.b**2 - 4*self.a*self.c
    
    def roots_exist(self):
        return self.get_discriminant() >= 0

    def roots_finder(self):
        if self.roots_exist():
            return [(-self.b+(self.get_discriminant())**0.5)/(2*self.a),
                    (-self.b-(self.get_discriminant())**0.5)/(2*self.a)]
        else:
            return []

    def roots_finder_with_steps(self):
        if self.roots_exist():
            discriminant = self.get_discriminant_with_steps()
            print("\nSolving For Roots Steps:")
            print(f"Step 1 (Sub in values to Quadratic Formula):\n \
                    x = -({self.b}) ± √({self.b}^2 - 4({self.a})({self.c})\n\
        --------------------------------------------------\n\
                        2({self.a}) \n")
            print(f"Step 2 (Solve individual values):\n \
                    x = -({self.b}) ± √({discriminant})\n\
        ------------------------------------------\n\
                        {2*self.a}\n ")
            print(f"Step 3 (Solve for each individual X value):\n \
                    x1 = -({self.b}) + ({discriminant**0.5}) \n\
        ------------------------------------------ \n\
                        {2*self.a} \n\
                    x1 = {(-self.b + discriminant**0.5) /2}\n\
        =======================================================\n\
                    x2 = -({self.b}) - ({discriminant**0.5}) \n\
        ------------------------------------------ \n\
                        {2*self.a} \n\
                    x1 = {(-self.b - discriminant**0.5) /2}\n")
            return [(-self.b+(discriminant)**0.5)/(2*self.a),
                    (-self.b-(discriminant)**0.5)/(2*self.a)]
        else:
            return []
        
    def display_root_form(self):
        if self.roots_exist():
            print(f"f(x) = {self.a}(x - {self.roots_finder()[0]}) (x - {self.roots_finder()[1]})")
        else:
            print("No Real Roots Exist")

    def display_root_form_with_steps(self):
        if self.roots_exist():
            self.roots_finder_with_steps()
            print(f"f(x) = {self.a}(x - {self.roots_finder()[0]}) (x - {self.roots_finder()[1]})")
        else:
            print("No Real Roots Exist")

    def display_standard_form(self):
        print(f"f(x) = {self.a}x² + {self.b}x + {self.c}")

    def display_standard_form_with_steps(self):
        print("Just Substitute in the a,b,c values into the equation:")
        print(f"f(x) = {self.a}x² + {self.b}x + {self.c}")
       
    def display_point_slope_form(self):
        print(f"f(x) = {self.a}(x + {((self.b/self.a)/2)})² + {self.c-(self.a*(((self.b/self.a)/2)**2))}".replace("+ -","- ").replace(" 1(",""))

    def display_point_slope_form_with_steps(self):
        print("\nSolving For The Point Slope Form Steps:")
        print(f"Step 1 (Show The standard Form):")
        self.display_standard_form()
        print(f"Step 2 (Enclose the a & b values and factor out a):\n\
f(x) = {self.a}(x² + {((self.b/self.a))}) + {self.c}")
        print(f"Step 3 (Take the new b value and divide by two and square, take both + & - versions):\n\
f(x) = {self.a}(x² + {((self.b/self.a)/2)**2} - {((self.b/self.a)/2)**2}) + {self.c}")
        print(f"Step 3 (Take the - b value and move outside of brackets with c):\n\
f(x) = {self.a}(x² + {((self.b/self.a)/2)**2}) + {-(self.a*(((self.b/self.a)/2)**2))} + {self.c}")
        print(f"Step 4 (Add -b and c and sqrt the values inside of the brackets, and place the ² outside of it):")
        print(f"f(x) = {self.a}(x + {((self.b/self.a)/2)})² + {self.c-(self.a*(((self.b/self.a)/2)**2))}".replace("+ -","- ").replace(" 1(",""))
        
    def y_intercept(self):
        return self.c
    
    def max_value(self):
        return self.a <= 0
    
if __name__ == "__main__":
    obje = Quadratic_Function(1,5,6)
    obje.display_root_form_with_steps()
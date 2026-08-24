import math
from Graphing_API import Graphing_Function

class Exponential_Function:

    def __init__(self,b = 1):
        self.b = b

    def get_exponential_function(self):
        return "y = bˣ"

    def get_inverse_exponential_function(self):
        return "x = bʸ","y = log♭x"

    def get_exponent_laws(self):
        return "(xᵃ)(xᵇ) = xᵃ⁺ᵇ","xᵃ ÷ xᵇ = xᵃ⁻ᵇ","(xᵃ)ᵇ = xᵃˣᵇ","x⁰ = 1","xᵃᐟᵇ = ᵇ√xᵃ = (ᵇ√x)ᵃ","x⁻ᵃ = 1/xᵃ"

    def get_power_law_of_logarithms(self):
        return "log♭xⁿ = nlog♭x"

    def get_change_of_base_formula(self):
        return "log♭x = logₐx ÷ logₐ♭"

    def get_power_law_of_logatithms_2(self):
        return "log♭(mⁿ) = nlog♭m"

    def get_product_multiplication_law(self):
        return "log♭(m x n) = log♭m + log♭n"

    def get_quotients_division(self):
        return "log♭(m / n) = log♭m - log♭n"

    def get_thechnique_for_solving_log_equations(self):
        return "logₐm = logₐn then m = n"

    def subscript_replacer(self,inverted_expo_func):
            equation = (inverted_expo_func.replace("_0","₀_").replace("_1","₁_").replace("_2","₂_").replace("_3","₃_").replace("_4","₄_").replace("_5","₅_").replace("_6","₆_").replace("_7","₇_").replace("_8","₈_").replace("_9","₉_").replace("_-0","₋₀_").replace("_-1","₋₁_").replace("_-2","₋₂_").replace("_-3","₋₃_").replace("_-4","₋₄_").replace("_-5","₋₅_").replace("_-6","₋₆_").replace("_-7","₋₇_").replace("_-8","₋₈_").replace("_-9","₋₉_"))
            if "_" not in equation:
                print(equation)
            else:
                while True:
                    equation = (equation.replace("_0","₀_").replace("_1","₁_").replace("_2","₂_").replace("_3","₃_").replace("_4","₄_").replace("_5","₅_").replace("_6","₆_").replace("_7","₇_").replace("_8","₈_").replace("_9","₉_").replace("_-0","₋₀_").replace("_-1","₋₁_").replace("_-2","₋₂_").replace("_-3","₋₃_").replace("_-4","₋₄_").replace("_-5","₋₅_").replace("_-6","₋₆_").replace("_-7","₋₇_").replace("_-8","₋₈_").replace("_-9","₋₉_"))
                    equation = equation.strip()
                    if equation[-2] == "_" or "_0" not in equation or "_1" not in equation or "_2" not in equation or "_3" not in equation or "_4" not in equation or "_5" not in equation or "_6" not in equation or "_7" not in equation or "_8" not in equation or "_9" not in equation:
                        if "_0" in equation or "_1" in equation or "_2" in equation or "_3" in equation or "_4" in equation or "_5" in equation or "_6" in equation or "_7" in equation or "_8" in equation or "_9" in equation:
                            pass
                        else:
                            equation = equation.replace("_","")
                            break
                    else:
                        pass
            return equation

    def invert_exponential_function(self,exponential_func):
        if "^" not in exponential_func:
            exponential_func += "^1"
        exponential_func = exponential_func.replace(" ","")
        temp_func = "|".join(exponential_func.split("^"))
        temp_func = "|".join(temp_func.split("="))
        temp_func = temp_func.split("|")
        y,b,x = temp_func[0],temp_func[1],temp_func[2]
        inverted_func = self.subscript_replacer(f"{y} = log_{b}") + x
        return inverted_func

    def get_log(self, x):
        '''tempval = 0
        while True:
            if self.b**(tempval) != x:
                tempval+=1
            else:
                break'''
        return math.log(x,self.b) 

    def get_log_base_10(self,x):
        return math.log10(x)

    def get_e_value(self):
        return math.e

    def get_ln(self,x):
        return math.log(x,self.get_e_value())

    def transform_log_func_coords(self,a=1,k=1,d=0,c=0):
        xcoords = self.get_expo_func_coords()[0]
        ycoords = self.get_expo_func_coords()[1]
        newxcoords = []
        newycoords = []
        for i in range(len(xcoords)):
            newxcoords.append(xcoords[i]/k + d)
            newycoords.append(ycoords[i]*a + c)
        return newxcoords,newycoords

    def get_expo_func_coords(self):
        ycoords = []
        xcoords = []
        for x in range(-25,26):
            ycoords.append(self.b**x)
            xcoords.append(x)
        return xcoords,ycoords

    def graph_expo_function(self):
        graph = Graphing_Function()
        graph.add_x_points(self.get_expo_func_coords()[0])
        graph.add_y_points(self.get_expo_func_coords()[1])
        graph.change_graph_picture_name("Exponential Graph")
        graph.plot_graph()

    

if __name__ == "__main__":
    obje = Exponential_Function(3)
    obje.graph_expo_function()
    print(obje.invert_exponential_function("20 = 3^7"))

    
        




import math
from Graphing_API import Graphing_Function

class Cubic_Function:
    def __init__(self,a=0,b=0,c=0,d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_p(self) -> float:
        return (3 * self.a * self.c - self.b ** 2) / (3 * self.a ** 2)

    def get_q(self) -> float:
        return (27 * self.a ** 2 * self.d - 9 * self.a * self.b * self.c + 2 * self.b ** 3) / (27 * self.a ** 3)

    def get_disc(self) -> float:
        return (self.get_q() / 2) ** 2 + (self.get_p() / 3) ** 3

    def real_roots_exist(self) -> str:
        if self.get_disc() <= 0:
            return True
        else:
            return False

    def cardanos_method(self) -> list:
        if self.real_roots_exist() == False:
            u = (-self.get_q() / 2 + (self.get_disc())**0.5)**(1/3)
            v = (-self.get_q() / 2 - (self.get_disc())**0.5)**(1/3)
            root = (u + v - self.b / (3 * self.a))
            return [root,0]
        else:
            return "There Are Real Roots, use Trigonometric Method"

    def trigonometric_method(self) -> list:
        if self.real_roots_exist():
            theta = math.acos(-self.get_q() / (2 * (-1 * (self.get_p() / 3) ** 3)**0.5)) / 3
            x1 = (2 * (-self.get_p() / 3)**0.5 * math.cos(theta) - self.b / (3 * self.a))
            x2 = (2 * (-self.get_p() / 3)**0.5 * math.cos(theta + (2 * math.pi) / 3) - self.b / (3 * self.a))
            x3 = (2 * (-self.get_p() / 3)**0.5 * math.cos(theta + (4 * math.pi) / 3) - self.b / (3 * self.a))
            return [x1,0],[x2,0],[x3,0]

    def get_root_terms(self) -> str:
        if self.get_disc() <= 0:
            x1 = self.trigonometric_method()[0]
            x2 = self.trigonometric_method()[1]
            x3 = self.trigonometric_method()[2]
            if x1 == x2 and x1 != x3:
                return "Double Real Roots, Single Real Root"
            elif x1 == x3 and x1 != x2:
                return "Double Real Roots, Single Real Root"
            elif x2 == x3 and x2 != x1:
                return "Double Real Roots, Single Real Root"
            elif x1 != x2 and x1 != x3:
                return "3 Distinct Real Roots"
            else:
                return "Triple Real Roots"
        else:
            x1 = self.cardanos_method()
            return "1 Real Root, 2 Complex Roots"

    def get_cubic_equation_coordinates(self):
        xcoords = []
        ycoords = []
        for x in range(-10,10):
            ycoords.append(self.a*x**3 + self.b*x**2 + self.c*x + self.d)
            xcoords.append(x)
        return xcoords,ycoords
    
    def graph_cubic_function(self):
        graph = Graphing_Function()
        graph.add_x_points(self.get_cubic_equation_coordinates()[0])
        graph.add_y_points(self.get_cubic_equation_coordinates()[1])
        graph.change_graph_picture_name("Cubic_Equation_Graph")
        graph.plot_graph()


if __name__ == "__main__":
    obje = Cubic_Function(2,3,4,-5)
    obje.graph_cubic_function()
    print(obje.get_root_terms())
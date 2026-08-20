from Graphing_API import Graphing_Function

class Linear_Function:
    
    def __init__(self,m:float=0,x:float=0,b:float=0):
        self.m = m
        self.x = x
        self.b = b
    
    def set_m_val(self,newval):
        self.m = newval

    def set_x_val(self,newval):
        self.x = newval

    def set_b_val(self,newval):
        self.b = newval

    def get_m_val(self):
        return self.m 

    def get_x_val(self):
        return self.x

    def get_b_val(self):
        return self.b
    
    def set_slope_by_coord(self,x1,y1,x2,y2):
        self.m = (y2-y1)/(x2-x1)

    def display_equation(self):
        print(f"y = ({self.m})x + ({self.b})")

    def get_y_val(self):
        return self.m*self.x + self.b

    def get_linear_equation_coordinates(self):
        xcoords = []
        ycoords = []
        for x in range(-5,5):
            ycoords.append(self.m*x + self.b)
            xcoords.append(x)
        return xcoords,ycoords

    def graph_linear_function(self):
        graph = Graphing_Function()
        graph.add_x_points(self.get_linear_equation_coordinates()[0])
        graph.add_y_points(self.get_linear_equation_coordinates()[1])
        graph.change_graph_picture_name("Linear_Equation_Graph")
        graph.plot_graph()

if __name__ == "__main__":
    obje = Linear_Function(-2,3,4)
    obje.graph_linear_function()

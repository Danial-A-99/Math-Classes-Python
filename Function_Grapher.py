from Graphing_API import Graphing_Function

class Function_Grapher:
    def __init__(self,*args):
        self.coefficients = args

    def get_equation_coordinates(self,startX:int=-10,endX:int=10):
        xcoords = []
        ycoords = []
        for x in range(startX,endX):
            degree_of_function = len(self.coefficients)-1
            yValue = 0
            for i in range(len(self.coefficients)):
                yValue += self.coefficients[i]*x**degree_of_function
                degree_of_function -= 1
            ycoords.append(yValue)
            xcoords.append(x)
        return xcoords,ycoords

    def graph_function(self,nameOfFunction:str):
        graph = Graphing_Function()
        graph.add_x_points(self.get_equation_coordinates()[0])
        graph.add_y_points(self.get_equation_coordinates()[1])
        graph.change_graph_picture_name(nameOfFunction)
        graph.plot_graph()


if __name__ == "__main__":
    obje = Function_Grapher(1,3)
    obje.graph_function("NewGraph")
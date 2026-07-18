import matplotlib.pyplot as plt
import numpy as np


class Graphing_API:
    def __init__(self):
        self.xpoints = [0]
        self.ypoints = [0]
        self.marker = ''
        self.color = 'blue'
        self.line_style = '-'
        self.line_width = 1.0
        self.title = "Graph"
        self.xlabel = "X coordinates"
        self.ylabel = "Y Coordinates"
        self.yn_grid = False
        self.grid_linestyle = ""
        self.grid_lineWidth = 1.0
        self.grid_lineColor = "Blue"

    def add_x_points(self, xpoints):
        self.xpoints = xpoints
    
    def add_y_points(self, ypoints):
        self.ypoints = ypoints

    def change_marker(self,marker):
        self.marker = marker
    
    def change_color(self, color):
        self.color = color

    def change_line_style(self, linestyle):
        self.line_style = linestyle

    def change_line_width(self, linewidth):
        self.line_width = linewidth

    def change_title(self,title):
        self.title = title

    def change_x_label(self,xlabel):
        self.xlabel = xlabel
    
    def change_y_label(self,ylabel):
        self.ylabel = ylabel

    def change_yn_grid(self,valforgrid:bool):
        self.yn_grid = valforgrid
    
    def change_grid_color(self,color):
        self.grid_lineColor = color

    def change_grid_width(self,width):
        self.grid_lineWidth = width

    def change_grid_linestyle(self,linestyle):
        self.grid_linestyle = linestyle

    def inverse_points(self):
        xpoints = self.ypoints
        ypoints = self.xpoints
        return xpoints,ypoints

    def plot_two_line_graph(self,args):
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.plot(self.xpoints, self.ypoints, marker=self.marker, color=self.color, linestyle=self.line_style, linewidth=self.line_width)
        for i in range(len(args)):
            if i %2 != 0:
                other_ypoints = args[i]
            else:
                other_xpoints = args[i]
            plt.plot(other_xpoints, other_ypoints)
        plt.grid(self.yn_grid,self.color,self.grid_linestyle,self.grid_lineWidth)
        plt.show()

    def scatter_plot_graph(self,args):
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        for i in range(len(args)):
            if i %2 != 0:
                other_ypoints = args[i]
            else:
                other_xpoints = args[i]
            plt.scatter(other_xpoints, other_ypoints, color=self.color)
        plt.grid(self.yn_grid,self.color,self.grid_linestyle,self.grid_lineWidth)
        plt.show()

    def plot_graph(self):
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.plot(self.xpoints, self.ypoints, marker=self.marker, color=self.color, linestyle=self.line_style, linewidth=self.line_width)
        plt.grid(self.yn_grid,self.color,self.grid_linestyle,self.grid_lineWidth)
        plt.show()


if __name__ == "__main__":
    obje = Graphing_API()

    obje.add_x_points([1,2,3,4,5,6,7])
    obje.add_y_points([2,3,4,5,6,7,8])

    obje.scatter_plot_graph()
    obje.plot_graph()
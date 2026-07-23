import math

class Shape_Function:
    PI = math.pi

    def __init__(self):
        pass

    def rectangle_area(self,height,width):
        area = width*height
        return area

    def square_area(self,height,width):
        return self.rectangle_area(height,width)

    def parralelograme_area(self,height,width):
        return self.rectangle_area(height,width)

    def trapezoid_area(self,height,base1,base2):
        area = 0.5*(base1 + base2)*height
        return area

    def rhombus_area(self,width,height):
        area = 0.5*height*width
        return area

    def standard_triangle_area(self,base,height):
        area = (base*height)/2
        return area

    def equillateral_triangle_area(self,side_length):
        area = ((3**0.5)/4)*side_length**2
        return area

    def herons_triagle_formula(self,side1,side2,side3):
        semi_perimiter = side1+side2+side3 
        area = (semi_perimiter*(semi_perimiter-side1)*(semi_perimiter-side2)*(semi_perimiter-side3))**0.5
        return area

    def circle_area(self,radius):
        area = Shape_Function.PI * radius**2 
        return area

    def oval_area(self,height,width):
        area = Shape_Function.PI*(height/2)*(width/2)
        return area

    def circle_sector_area(self,radius,radian_angle):
        area = 0.5*radius**2*radian_angle
        return area

    def regular_polygon_area(self,apothem,preimiter):
        area = 0.5*apothem*preimiter
        return area

    def cube_volume(self,side_length):
        volume = side_length**3
        return volume

    def rectangular_prism_volume(self,length,width,height):
        volume = length*width*height
        return volume

    def cylinder_colume(self,radius,height):
        volume = Shape_Function.PI*radius**2*height
        return volume

    def triangular_prism_volume(self,length,width,height):
        volume = (0.5*width*height)*length
        return volume

    def sphere_volume(self,radius):
        volume = (4/3)*Shape_Function.PI*radius**3
        return volume

    def cone_volume(self,base_radius,height):
        volume = (1/3)*Shape_Function.PI*base_radius**2*height
        return volume

    def regular_pyramid_volume(self,base_area,height):
        volume = (base_area*height)/3
        return volume

    def cube_surface_area(self,side_length):
        surface_area = 6*side_length**2
        return surface_area

    def rectangular_prism_surface_area(self,base,height,width):
        surface_area = 2*(base*height+base*width+height*width)
        return surface_area

    def cylinder_surface_area(self,radius,height):
        surface_area = 2*Shape_Function.PI*radius*(radius+height)
        return surface_area

    def cone_surface_area(self,radius,slant_height):
        surface_area = Shape_Function.PI*radius(radius+slant_height)
        return surface_area

    def sphere_surface_area(self,radius):
        surface_area = 4*Shape_Function.PI*radius**2
        return surface_area

    def hemisphere_surface_area(self,radius):
        surface_area = 3*Shape_Function.PI*radius**2
        return surface_area

    def square_pyramid_surface_area(self,base,slant_height):
        surface_area = base**2 + 2*base*slant_height
        return surface_area


if __name__ == "__main__":
    obje = Shape_Function()
    print(obje.trapezoid_area(2,3,4))
    

    
        
import math
from Graphing_API import Graphing_Function
from Polynomial_API import Polynomial_Function 

class Trigonometric_Function_Degrees:
    
    def __init__(self,theta:float|int=1):
        self.theta = theta

    def set_theta(self,new_val:float|int):
        self.theta = new_val

    def theta_by_sin(self,opposite,hypoteneuse):
        return math.asin(opposite/hypoteneuse)
    
    def theta_by_cos(self,adjacent,hypoteneuse):
        return math.acos(adjacent/hypoteneuse)
    
    def theta_by_tan(self,opposite,adjacent):
        return math.atan(opposite/adjacent)

    def sin_deg(self):
        return math.sin(math.radians(self.theta))
    
    def cos_deg(self):
        return math.cos(math.radians(self.theta))

    def tan_deg(self):
        return math.tan(math.radians(self.theta))
    
    def sine_law_2sides(self,sideA,sideB,angleA):
        angleB = self.theta_by_sin((sideB*self.sin_deg(angleA))/sideA)
        return angleB
    
    def sine_law_2angles(self,sideA,angleA,angleB):
        sideB = sideA*self.sin_deg(angleB)/self.sin_deg(angleA)
        return sideB
    
    def cosine_law(self,angleA,sideB,sideC):
        sideA = sideB**2 + sideC**2 - 2*sideB*sideC*self.cos_deg(angleA)
        return sideA


class Trigonometric_Function_Radians:#Radian_Measure_Function
    PI = math.pi

    def __init__(self,theta=None):
        self.theta = theta

    def set_theta(self,new_theta):
        self.theta=new_theta

    def rad_to_deg(self):
        return 180/Trigonometric_Function_Radians.PI * self.theta

    def deg_to_rad(self,deg_theta):
        return math.PI/(180/deg_theta)

    def arc_length(self,radius):
        return self.theta*radius

    def theta_from_arc_len(self,radius,arc_length):
        return arc_length/radius

    def angular_velocity(self,time):
        return self.theta/time # rad/sec

    def get_special_triangles(self):
        return r'''
    |\
    | \
    |  \
    |π/6\  
 √3 |    \  2
    |     \  
    |      \
    |π/2 π/3\
    |--------\
        1

    |\
    | \
    |  \
    |π/4\
    |    \
    |     \
  1 |      \  √2
    |       \  
    |        \  
    |         \  
    |          \
    |π/2     π/4\
    |------------\
           1
'''

    def get_val_sin(self):
        return math.sin(self.theta)

    def get_val_cos(self):
        return math.cos(self.theta)

    def get_val_tan(self):
        return math.tan(self.theta)

    def get_val_csc(self):
        return 1 / math.sin(self.theta)

    def get_val_sec(self):
        return 1 / math.cos(self.theta)

    def get_val_cot(self):
        return 1 / math.tan(self.theta)


class Trig_Functions_Function:

    def __init__(self):
        pass

    def graph_trig_function(self,xcoords,ycoords):
        graph = Graphing_Function()
        graph.add_x_points(xcoords)
        graph.add_y_points(ycoords)
        graph.change_graph_picture_name("Trig_Graph")
        graph.plot_graph()

    def sine_standard_coords(self):
        return [0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330,360],[0,1/2,(2**0.5)/2,(3**0.5)/2,1,(3**0.5)/2,(2**0.5)/2,1/2,0,-0.5,-(2**0.5)/2,-(3**0.5)/2,-1,-(3**0.5)/2,-(2**0.5)/2,-1/2,0]

    def cosine_standard_coords(self):
        return [0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330,360],[1,(3**0.5)/2,(2**0.5)/2,1/2,0,-1/2,-(2**0.5)/2,-(3**0.5)/2,-1,-(3**0.5)/2,-(2**0.5)/2,-1/2,0,1/2,(2**0.5)/2,(3**0.5)/2,1]

    def tangent_standard_coords(self):
        return [0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330,360],[0,(3**0.5)/2,1,(3**0.5),"UND",-(3**0.5),-1,-(3**0.5)/2,0,(3**0.5)/2,1,(3**0.5),"UND",-(3**0.5),-1,-(3**0.5)/2,0]

    def instructions_for_reciprocal(self):
        print("For csc & sec : x-intercepts = assymptotes | peaks and trophs = vertexes | Pos of peak/troph relative to center determines - or + a")
        print("For cot : x-intercepts = assymptotes | flip the original graph on the x axis")

    def transform_coords(self,sct,a,k,d,c):
        transformed_x_coords = []
        transformed_y_coords = []
        xcoords,ycoords = [],[]
        generate_coords = True
        if sct == "s":
            xcoords,ycoords = self.sine_standard_coords()[0],self.sine_standard_coords()[1]
        elif sct == "c":
            xcoords,ycoords = self.cosine_standard_coords()[0],self.cosine_standard_coords()[1]
        elif sct == "t":
            xcoords,ycoords = self.tangent_standard_coords()[0],self.tangent_standard_coords()[1]
        else:
            print("Please Enter Valid: s,c or t")
            generate_coords = False

        if generate_coords:
            for x_coord in xcoords:
                transformed_x_coords.append(x_coord/k + d)
            for y_coord in ycoords:
                transformed_y_coords.append(a*y_coord + c)  
            return transformed_x_coords,transformed_y_coords

    def reciprocal_coords(self,sct):
        inverted_y_coords = []
        generate_coords = True
        if sct == "s":
            xcoords,ycoords = self.sine_standard_coords()[0],self.sine_standard_coords()[1]
        elif sct == "c":
            xcoords,ycoords = self.cosine_standard_coords()[0],self.cosine_standard_coords()[1]
        elif sct == "t":
            xcoords,ycoords = self.tangent_standard_coords()[0],self.tangent_standard_coords()[1]
        else:
            print("Please Enter Valid: s,c or t")
            generate_coords = False

        if generate_coords:
            for y_coord in ycoords:
                inverted_y_coords.append(y_coord*-1)
            return xcoords,inverted_y_coords


class Trig_Expressions_Function:
    def __init__(self):
        pass

    def trig_ids(self):
        return {"cscθ":"1/sinθ",
               "secθ":"1/cosθ",
               "cotθ":"1/tanθ",
               "sinθ/cosθ":"tanθ",
               "sin²θ+cos²θ": 1}
    
    def trig_ids_rt(self):
        return {"sinθ" : ["cos(π/2 - θ)", "c/b"],
                "cosθ" : ["sin(π/2 - θ)", "a/b"],
                "tanθ" : ["cot(π/2 - θ)", "c/a"],
                "cscθ" : ["sec(π/2 - θ)", "b/c"],
                "secθ" : ["csc(π/2 - θ)", "b/a"],
                "cotθ" : ["tan(π/2 - θ)", "a/c"],}

    def trig_ids_transformations(self):
        return {"sinθ" : "cos(θ - π/2)",
                "cosθ" : "sin(θ + π/2)",
                "tanθ" : "-cot(θ - π/2)",
                "cscθ" : "sec(θ - π/2)",
                "secθ" : "csc(θ + π/2)",
                "cotθ" : "-tan(θ - π/2)",}

    def trig_ids_odd_func(self):
        return {"sin(-θ)" : "-sinθ",
                "csc(-θ)" : "-cscθ",
                "tan(-θ)" : "-tanθ",
                "cot(-θ)" : "-cotθ",}

    def trig_ids_even_func(self):
        return {"cos(-θ)" : "-cosθ",
                "sec(-θ)" : "-secθ",}

    def compound_angle_formulas(self):
        return {"sin(x+y)" : "sin(x)cos(y) + cos(x)sin(y)",
                "sin(x-y)" : "sin(x)cos(y) - cos(x)sin(y)",
                "cos(x+y)" : "cos(x)cos(y) - sin(x)sin(y)",
                "cos(x-y)" : "cos(x)cos(y) + sin(x)sin(y)",
                "tan(x+y)" : "[tan(x) + tan(y)] / [1 - tan(x)tan(y)]",
                "tan(x-y)" : "[tan(x) - tan(y)] / [1 + tan(x)tan(y)]"}

    def double_angle_formulas(self):
        return {"sin(2θ)" : "2sinθcosθ",
                "cos(2θ)" : "cos²θ - sin²θ",
                "cos(2θ)" : "2cos²θ - 1",
                "cos(2θ)" : "1 - 2sin²θ",
                "tan(2θ)" : "[2tanθ] / [1 - tan²θ]"}

    def half_angle_formulas(self):
        return {"sin(θ/2)" : "±√[(1-cosθ)/2]",
                "cos(θ/2)" : "±√[(1+cosθ)/2]",
                "tan(θ/2)" : "(1-cosθ)/(sinθ)",
                "tan(θ/2)" : "(sinθ/1+cosθ)"}

    def display_trig_ids(self):
        for t_id in self.trig_ids():
            print(f"{t_id} = {self.trig_ids()[t_id]}")
    
    def display_trig_ids_rt(self):
        for t_id in self.trig_ids_rt():
            print(f"{t_id} = {self.trig_ids_rt()[t_id][0]} = {self.trig_ids_rt()[t_id][1]} ")

    def display_trig_ids_transformations(self):
        for t_id in self.trig_ids_transformations():
            print(f"{t_id} = {self.trig_ids_transformations()[t_id]}")

    def display_trig_ids_odd_func(self):
        for t_id in self.trig_ids_odd_func():
            print(f"{t_id} = {self.trig_ids_odd_func()[t_id]}")

    def display_trig_ids_even_func(self):
        for t_id in self.trig_ids_even_func():
            print(f"{t_id} = {self.trig_ids_even_func()[t_id]}")

    def display_trig_ids_compound_angles(self):
        for t_id in self.compound_angle_formulas():
            print(f"{t_id} = {self.compound_angle_formulas()[t_id]}")

    def display_trig_ids_double_angles(self):
        for t_id in self.double_angle_formulas():
            print(f"{t_id} = {self.double_angle_formulas()[t_id]}")

    def display_trig_ids_half_angles(self):
        for t_id in self.half_angle_formulas():
            print(f"{t_id} = {self.half_angle_formulas()[t_id]}")


class Trigonometric_Identities:

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
    obje = Trig_Expressions_Function()
    obje.display_trig_ids()



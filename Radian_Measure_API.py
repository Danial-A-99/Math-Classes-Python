import math

class Radian_Measure_Function:
    def __init__(self):
        self.theta = None
        self.PI = math.pi

    def rad_to_deg(self):
        return 180/self.PI * self.theta

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

if __name__ == "__main__":
    obje = Radian_Measure_Function()

    print(obje.get_special_triangles())
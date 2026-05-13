
import math
class Trigonometric_Function:
    
    def __init__(self,theta:float|int):
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

    def sin_rad(self):
        return math.sin(self.theta)
    
    def cos_rad(self):
        return math.cos(self.theta)
    
    def tan_rad(self):
        return math.tan(self.theta)
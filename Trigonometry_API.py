
import math
class Trigonometric_Function:
    
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

    def sin_rad(self):
        return math.sin(self.theta)
    
    def cos_rad(self):
        return math.cos(self.theta)
    
    def tan_rad(self):
        return math.tan(self.theta)
    
    def sine_law_2sides(self,sideA,sideB,angleA):
        angleB = self.theta_by_sin((sideB*self.sin_deg(angleA))/sideA)
        return angleB
    
    def sine_law_2angles(self,sideA,angleA,angleB):
        sideB = sideA*self.sin_deg(angleB)/self.sin_deg(angleA)
        return sideB
    
    def cosine_law(self,angleA,sideB,sideC):
        sideA = sideB**2 + sideC**2 - 2*sideB*sideC*self.cos_deg(angleA)
        return sideA
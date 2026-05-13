

class Linear_Function:
    
    def __init__(self,m:float,x:float,b:float):
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
        self.m = (x2-x1)/(y2-y1)

    def display_equation(self):
        print(f"y = ({self.m})({self.x}) + ({self.b})")

    def get_y_val(self):
        return self.m*self.x + self.b
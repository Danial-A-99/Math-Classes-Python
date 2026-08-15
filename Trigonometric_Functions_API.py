
class Trig_Functions_Function:

    def __init__(self):
        pass

    def display_trig_function(self):
        pass # Need to write code that connects this to Graphing API

    def sine_standard_coords(self):
        return [0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330,360],
    [0,1/2,(2**0.5)/2,(3**0.5)/2,1,(3**0.5)/2,(2**0.5)/2,1/2,0,-0.5,-(2**0.5)/2,-(3**0.5)/2,-1,-(3**0.5)/2,-(2**0.5)/2,-1/2,0]

    def cosine_standard_coords(self):
        return [0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330,360],
    [1,(3**0.5)/2,(2**0.5)/2,1/2,0,-1/2,-(2**0.5)/2,-(3**0.5)/2,-1,-(3**0.5)/2,-(2**0.5)/2,-1/2,0,1/2,(2**0.5)/2,(3**0.5)/2,1]

    def tangent_standard_coords(self):
        return [0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330,360],
    [0,(3**0.5)/2,1,(3**0.5),"UND",-(3**0.5),-1,-(3**0.5)/2,0,(3**0.5)/2,1,(3**0.5),"UND",-(3**0.5),-1,-(3**0.5)/2,0]

    def instructions_for_reciprocal(self):
        print("For csc & sec : x-intercepts = assymptotes | peaks and trophs = vertexes | Pos of peak/troph relative to center determines - or + a")
        print("For cot : x-intercepts = assymptotes | flip the original graph on the x axis")

    def transform_coords(self,sct,a,k,d,c):
        transformed_x_coords = []
        transformed_y_coords = []
        xcoords,ycoords = [],[]
        generate_coords = True
        if sct == "s":
            xcoords,ycoords = self.sine_standard_coords[0],self.sine_standard_coords[1]
        elif sct == "c":
            xcoords,ycoords = self.cosine_standard_coords[0],self.cosine_standard_coords[1]
        elif sct == "t":
            xcoords,ycoords = self.tangent_standard_coords[0],self.tangent_standard_coords[1]
        else:
            print("Please Enter Valid: s,c or t")
            generate_coords = False

        if generate_coords:
            for x_coord in xcoords:
                transformed_x_coords.append(x_coord/k + d)
            for y_coord in ycoords:
                transformed_y_coords.append(a*y_coord + c)  
            return transformed_x_coords,transformed_y_coords

    def instructions_for_reciprocal(self,sct):
        inverted_y_coords = []
        generate_coords = True
        if sct == "s":
            xcoords,ycoords = self.sine_standard_coords[0],self.sine_standard_coords[1]
        elif sct == "c":
            xcoords,ycoords = self.cosine_standard_coords[0],self.cosine_standard_coords[1]
        elif sct == "t":
            xcoords,ycoords = self.tangent_standard_coords[0],self.tangent_standard_coords[1]
        else:
            print("Please Enter Valid: s,c or t")
            generate_coords = False

        if generate_coords:
            for y_coord in ycoords:
                inverted_y_coords.append(y_coord*-1)
            return inverted_y_coords
        
    







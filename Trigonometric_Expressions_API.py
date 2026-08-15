
class Trig_Expressions_Function:
    def __init__(self):
        pass

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

    

if __name__ == "__main__":
    obje = Trig_Expressions_Function()
    obje.display_trig_ids_rt()
    obje.display_trig_ids_transformations()
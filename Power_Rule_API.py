

class Power_Rule:
  def __init__(self,equation:str):
    self.equation = equation

  def split_eqution(self):
    temp_equation = self.equation.split("x^")
    coeffs = []
    exps = []
    for i in range(len(self.equation)):
      if i %2 == 0:
        coeffs.append(self.equation[i])
      else:
        exps.append(self.equation[i])
    return coeffs,exps
    
  def derive_to(self,place):
    coeffs = self.split_equation()[0]
    exps = self.split_equation()[1]
    
     

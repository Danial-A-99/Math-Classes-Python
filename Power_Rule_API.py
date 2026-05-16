

class Power_Rule:
  def __init__(self,equation:str):
    self.equation = equation

  def split_equation(self):
    temp_equation = self.equation.split(" ")
    temp_equation = "|".join(temp_equation)
    temp_equation = temp_equation.split("x")
    temp_equation = "|".join(temp_equation)
    temp_equation = temp_equation.split("|")
    coeffs = []
    exps = []
    for i in range(len(temp_equation)):
      if i %2 == 0:
        coeffs.append(temp_equation[i])
      else:
        exps.append(temp_equation[i])
    return coeffs,exps
    
  def derive_to(self,place):
    coeffs = self.split_equation()[0]
    exps = self.split_equation()[1]
    newcoeffs = []
    newexps = []
    tempexps = []
    for val in exps:
      if "^" in val:
        tempexps.append(val.replace("^",""))
      else:
        tempexps.append(val)

    for i in range(len(coeffs)):
      try:
        tempexpval = float(tempexps[i])
      except:
        tempexpval = ""
      if type(tempexpval) != int and type(tempexpval) != float:
        newcoeffs.append(0)
        newexps.append("")
      elif tempexpval == 0:
        newcoeffs.append(coeffs[i])
        newexps.append("")
      else:
        newcoeffs.append(float(coeffs[i]) * tempexpval)
        newexps.append(tempexpval - 1)

    return newcoeffs,newexps
  
  def re_assemble(self):
    pass


obje = Power_Rule("3x^3 4x^2 7x")    

print(obje.derive_to(2)[0])

print(obje.derive_to(2)[1])

     

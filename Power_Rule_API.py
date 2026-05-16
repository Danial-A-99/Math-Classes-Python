

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
  
  def deriver_func(self,coeffs,exps):
    newcoeffs = []
    newexps = []
    tempexps = []
    for val in exps:
      try:
        if "^" in val:
          tempexps.append(val.replace("^",""))
        else:
          tempexps.append(val)
      except:
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
  
  def derive_to(self,place):
    coeffs = self.split_equation()[0]
    exps = self.split_equation()[1]
    for i in range(place):
      coeffs = self.deriver_func(coeffs,exps)[0]
      exps = self.deriver_func(coeffs,exps)[1]

    return coeffs,exps
  
  def re_assemble(self,place):
    coeffs = self.derive_to(place)[0]
    exps = self.derive_to(place)[1]
    answer = ""
    for i in range(len(coeffs)):
       answer += f"{coeffs[i]}x^{exps[i]} + "
    tempanswer = answer.split()
    for val in tempanswer:
      if val.endswith("x^"):
        tempanswer.remove(val)
    while tempanswer[-1] == "+":
      tempanswer.pop(-1)
    answer = " ".join(tempanswer)
    answer = answer.replace("+ 0x^","").replace("x^0","").replace(".0","").replace("^1 "," ").replace("+ +","")
    return answer


user_inp = input("Enter The Equation: ")
to_point = int(input("Derive to: "))
#"3x^10 4x^9 7x^8 6x^7 5x^6 12x^5 4x^4 0.25x^3 3x^5 1x^1"
obje = Power_Rule(user_inp)    

print(obje.re_assemble(to_point))
     

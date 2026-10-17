
class frequent_functions:

    def __init__(self):
        pass

    def factorial(self,n):
        if (n == 0 or n == 1): return 1

        return n * self.factorial(n-1)

    def avrg(self,args):
        num_of_terms = len(args)
        sum_of_terms = sum(args)
        avg = sum_of_terms/num_of_terms
        return avg

    def fibonacci(self,num_of_terms):
        terms = [0,1]
        for i in range(num_of_terms - 2):
            terms.append(terms[-1] + terms[-2])
        return terms

    def pascals_triangle_gen(self,num_of_rows):
        templis = [1]
        triangle = [[templis[0]]]
        supertemplis = []
        for _ in range(num_of_rows):
            x = 0
            templis.append(0)
            templis.insert(0,0)
            for _ in templis:
                if x == (len(templis)) - 1:
                    templis = supertemplis
                    triangle.append(templis)
                    supertemplis = []
                    break
                else:
                    newnum = templis[x] + templis[x+1]
                    supertemplis.append(newnum)
                    x+=1
        return triangle

    def display_pascals_triangle(self,num_of_rows):
        for row in self.pascals_triangle_gen(num_of_rows):
            print(str(row).replace("[","").replace("]",""))

if __name__ == "__main__":
    obje = frequent_functions()
    obje.display_pascals_triangle(6)

    
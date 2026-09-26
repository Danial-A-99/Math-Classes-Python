
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

if __name__ == "__main__":
    obje = frequent_functions()
    print(obje.fibonacci(20))

    
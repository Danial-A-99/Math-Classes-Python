
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

    
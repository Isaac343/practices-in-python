import math


class McLaurin():

    def __init__(self):
        self.exponential = int(input('Exponente: '))

    def exponent_product(self, e):
        self.new_e = e ** self.exponential
        print('Valor: ', self.new_e, '\n')

    def results_calculation(self):
        self.data_r = []
        inc = 0
        self.results = 1
        self.medium = 0
        press = 0.000001
        while (self.medium > press):
            self.medium = ((self.exponential ** inc) / (math.factorial(inc)))
            inc = inc + 1
            # print(self.medium)
            self.results = self.results + self.medium
            print ("%i | %.6f " % (inc, self.results))


e = math.e
activate = McLaurin()
activate.exponent_product(e)
activate.results_calculation()

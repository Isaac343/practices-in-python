""" Obtener el producto de una serie de n-esimos números determinados por el
usuario"""


class Operator_two():
    """docstring for Operator_two."""
    def __init__(self, num_of_vars):
        self.quantity = num_of_vars
        self.data= []
        for a in range(self.quantity):
            self.value_a = float(input('Valor: '))
            self.data.append(self.value_a)

    def Operation_Multi(self):
        result = 1
        for b in self.data:
            result = result * b
        print(result)


num_of_vars = int(input('Cantidad de números a multiplicar: '))
Ot = Operator_two(num_of_vars)
Ot.Operation_Multi()

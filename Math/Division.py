class Division_action():

    def __init__(self, diver, divisor):
        self.divider = diver
        self.divisor = divisor

    def Scale(self):
        var_a = 0
        var_b = 0
        while (self.divider > var_a):
            var_a = self.divisor * var_b
            var_b = var_b + 1
            print(var_a)
        print(var_b - 1)


diver = int(input('Nuemero a dividir: '))
divisor = int(input('Numero divisor: '))
In = Division_action(diver, divisor)
In.Scale()

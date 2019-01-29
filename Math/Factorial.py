class Factorial():

    def __init__(self, num):
        self.number = num
        cont = 0
        sec = 1
        for a in range(self.number):
            cont = cont + 1
            sec = sec * cont
            print(sec)


num = int(input('Number to calculate: '))
i = Factorial(num)

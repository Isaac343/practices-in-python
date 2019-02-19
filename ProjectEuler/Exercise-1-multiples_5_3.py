class multiples():

    def __init__(self):
        self.counter = 0
        for a in range(0, 1001):
            self.A = a % 3
            self.B = a % 5
            if (self.A == 0) or (self.B == 0):
                self.counter = self.counter + a
        print (self.counter)


begin = multiples()

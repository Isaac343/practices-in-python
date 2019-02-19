class Matrix():

    def __init__(self):
        self.m1_y = int(input('Matrix one height: '))
        self.m1_x = int(input('Matrix one with: '))
        self.m2_y = int(input('Matrix two height: '))
        self.m2_x = int(input('Matrix two with: '))

    def validation(self):
        if (self.m1_x != self.m2_y):
            print('Matrix operation invalid')
        else:
            print('Matriz result will be: ', self.m1_x, ' x ', self.m2_y)

    def array_const(self):
        self.mat_lis_1 = [[]]

    def data_inputs(self):
        self.matrix_1 = (())
        for a in range(self.m1_y):
            for b in range(self.m1_x):
                self.var1 = int(input('Value on ', a, b, ': '))
                self.matrix_1.append(self.var1[a][b])


Aa = Matrix()
Aa.validation()

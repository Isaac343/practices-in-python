""" Realiza sumas y restas de numeros enteros y decimales. Si se quiere
sustraer un valor, el numero debera ser declarado como variable negativa."""


class Operator_one():
    # Esta funcion recibe los valoes, sean positivos o negativos.
    def Data_inputs(self, Var_quantity):
        self.quantity = Var_quantity
        self.data = []
        for i in range(self.quantity):
            self.value_i = float(input('Valor: '))
            self.data.append(self.value_i)

    # La operacion aritmetica se realiza la siguiente funcion.
    def Operation(self):
        # lenght = len(self.data)
        result = 0
        for j in self.data:
            result = result + j
        print('Resultado :', result)


Var_quantity = int(input('Cantidad de números a sumar: '))
Oo = Operator_one()
Oo.Data_inputs(Var_quantity)
Oo.Operation()

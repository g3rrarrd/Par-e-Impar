import operations

try:
    def init():
        print("Introduzca un numero del uno al cien")
        number = input()
        validation(int(number))
except ValueError:
    print("Se ha ingresado un valor no valido, intente de nuevo")

def validation(number):
    if (number > 100 or number < 1):
        print("Numero fuera del rango, por favor introduzca nuevamente el numero")
        print()
        init()
    else:
        operations.operaciones(number)
import operations

def init():
    print("Introduzca un numero del uno al cien")
    number = input()
    validation(number)

def validation(number):
    if (int(number) > 100 or int(number) < 1):
        print("Numero fuera del rango, por favor introduzca nuevamente el numero")
        init()
    else:
        operations.operaciones(number)
import Input

__value__ = True

while __value__ == True:
    try:
        def init():
            if(__name__ == "__main__"):
                Input.init()
            else:
                print(__name__)

        init()

        __value__ = False
    except ValueError as e:
        print("Valor no numerico ingresado")
        print()
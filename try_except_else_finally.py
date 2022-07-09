def division(x,y):
    try:
        resultado = x/y
        print(resultado)
    except ZeroDivisionError:
        print("division por cero")
    else:
        print("El resultado es: ", resultado)
    finally:
        print("Ejecutando la clausula finally")

division(2,1)
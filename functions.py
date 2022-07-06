# def hello(x="Person"): # parametro por defecto
#     print("Hello "+ x)

# hello("ryan")
# hello("joe")
# hello()

# def add(numberOne, numberTwo):
#     return numberOne + numberTwo

# print(add(10,30))
# print(add(600,10))

# print(len("hello"))

add = lambda numberOne, numberTwo : numberOne + numberTwo # lambda: tipo de funcion , aqui la funcion es add, tiene 2 parametros y despues del : es lo que retornara

print(add(10,30))
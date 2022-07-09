lista = []
print("Ingrese 4 numeros: ")
for i in range(0, 4):
    x = int(input("Ingrese numero: "))
    lista.append(x)
lista.sort()
print("El orden ascendente es: ")
print(lista)

######################################
lista = []
for i in range(0, 4):
    x = str(input("Ingrese nombre: "))
    lista.append(x)
lista.sort()
print("Lista de nombres ordenados: ")
print(lista)
#Generar 10 números aleatorios en una lista y mostrar el número mayor y número menor de la lista.
import random
lista = []
for x in range(10):
    ran = random.randint(1,101)
    lista.append(ran)
lista.sort()
print("La lista es: ",lista)
print("El numero mayor es: ",lista[-1],"El numero menor es: ",lista[0])
#Ingrese un número y construya una función que retorne la cifra Mayor de un número ingresado.

x = str(input("Inserte un numero: "))

def ciframayor(num):
    return max(num)

print("La cifra mayor es: ",ciframayor(x))
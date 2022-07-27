#Mostrar la tabla de multiplicar de un número positivo, para ello debe crear
#una función que muestre la tabla de multiplicar.

x = int(input("Inserte un numero: "))
def multi(num):
    i = 0
    for i in range(11):
        m = num*i
        i=i+1
        print(m)
print("tabla de multiplicar: ")
multi(x)

#Hallar si un número de 3 digitos es capicua, para ello debe crear una función
#capicúa.

x = int(input("Inserte un numero de 3 cifras: "))

def capicua(num):
    p = num // 100
    t = num%10
    if (p == t):
        print("Es capicua")
    else:
        print("No es capicua")


if(x >= 100):
    capicua(x)
else:
    print("No es de 3 digitos.")

n = int(input("Ingrese numero de 5 cifrast: "))
if (n>=10000):
    m = (n%1000)//100
else:
    print("El numero no es de 5 cifras")
print("El numero del medio es: ", m)
#Ejercicio 01: Ingresar 3 valores a indicar cual es el menor y el mayor
a=float(input("Ingrese primer valor: "))
minimo=a
maximo=a
b=float(input("Ingrese segundo valor: "))
if b<minimo:
    minimo=b
else:
    maximo=b
c=float(input("Introduce el tercer valor: "))
if c<minimo:
    minimo=c
elif c>maximo:
    maximo=c
print("El minimo es: ", minimo)
print("El maximo es: ", maximo)

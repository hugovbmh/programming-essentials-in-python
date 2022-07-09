lista = [12,34,56,22,11,45,67,89]
contador = 0
s = 0
for x in lista:
    if(x % 2 == 0):
        contador = contador + 1
    else:
        s = s + x
print("La cantidad de los pares es: ",contador)        
print("La suma de los impares es: ",s)

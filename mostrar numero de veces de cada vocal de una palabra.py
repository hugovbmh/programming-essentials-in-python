#Escribir un programa que pida al usuario una palabra y muestre por pantalla el numero de veces que contiene cada vocal
palabra=input("Introduce una palabra: ")
vocales=['a','e','i','o','u']
for i in vocales: #i recorrera cada valor del vector vocales
    vez=0 #contador
    for j in palabra: #j recorrera cada letra de la palabra
        if j == i :
            vez+=1
    print("La vocal " + i + " aparece " + str(vez) + " veces")

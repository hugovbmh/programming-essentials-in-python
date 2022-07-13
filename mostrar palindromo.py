#ejercicio07: Escribir un programa que pida al usuario una palabras y muestre en pantalla si es un palindromo
palabra=input("Introduzca una palabra: ")
reversa=palabra
palabra=list(palabra) #Convierte la palabra en una lista con valores de cada letra
reversa=list(reversa)
reversa.reverse()
if palabra==reversa:
    print("Es un palindromo")
    print(palabra)
else:
    print("No es un palindromo")
 
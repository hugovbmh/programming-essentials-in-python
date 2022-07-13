#Ejercicio 06: Escribir un programa que almacene la cadena de caracteres contraseña en un avariable. Pregunte al usuario por una contraseña hasta que introdusca la correcta
clave="senati"
password=""
while password != clave:
    password=input("Ingrese la contraseña: ")
print("La contraseña es correcta")

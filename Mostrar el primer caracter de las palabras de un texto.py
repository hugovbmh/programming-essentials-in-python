##Mostrar el primer carácter de las palabras de un texto ingresado
texto = []
texto=str(input("Ingrese el texto: "))
texto1 = texto.split()
x = 0
y = 0
for x in range(len(texto1)):
    for y in range(len(texto1)-1):
        print(texto1[x][y], end=" ")
    x=x+1

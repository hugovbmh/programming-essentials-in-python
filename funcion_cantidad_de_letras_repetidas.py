def cantidad_letras(frase,letra):
    contador=0
    cantidadletras=len(frase)
    for i in range(0,cantidadletras):
        if (frase[i]==letra):
            contador=contador+1
    return contador

xfrase=str(input("Ingrese frase: "))
xletra=str(input("Ingrese letra: "))

print("En la a frase ",xfrase,"se repite la letra ",cantidad_letras(xfrase,xletra))


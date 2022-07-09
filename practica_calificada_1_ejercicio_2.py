a = 0
u = 0
ns = 0
texto = str(input("Ingrese un texto: "))
print(texto)
print("Cantidad vocal a: ", texto.count("a"))
print("Cantidad vocal u: ", texto.count("u"))
print("Cantidad de las consonantes n y s: ", (texto.count("n")+texto.count("s")))
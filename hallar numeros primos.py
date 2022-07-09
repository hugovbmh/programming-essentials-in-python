lista = [11,2,56,13,45,7,1]
for xn in lista:
    #evaluamos los elementos de la lista
    xcon = 0 #xcon cuenta los valores divisibles
    for i in range(1, xn + 1, 1):
        if(xn % i == 0):
            xcon = xcon + 1
    if (xcon <= 2):
        print(xn," es primo")
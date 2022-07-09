nombre = ['Ana','Maria','Alberto','Ana','Jesus']

for i in range(5):
    contador=0
    for x in nombre:
        if(x==nombre[i]):
            contador=contador+1
    if(contador>=2):
        print("Se repite: ",nombre[i])
        nombre.remove('Ana')
        nombre.append('')
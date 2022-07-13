'''
#Ejercicio 05: generar un programa que pregunte al usuario un importe a invertir, el interes anual y el numero de años
mostrar por pantalla el capital obtenido en la inversion cada año

'''

importe = float(input("Importe a invertir: "))
interes = float(input("Interes porcentual anual: "))
years = int(input('numero de años: '))
for i in range(years):
    importe *= 1+interes/100
    print(f'el capital tras {i+1} año es : {round(importe, 2)}') #Round redondea a , x decimales
    


nombre = str(input("Ingrese nombre del obrero: "))
horas = int(input("Ingrese numero de horas trabajadas: "))
if(horas<=40):
    costohora=10
    salariosemanal=horas*costohora
else:
    costohoraextra=15
    salariosemanal=(40*10)+(horas-40)*15

print("El nombre es: ",nombre)
print("El numero de horas extras es: ",horas-40)
print("El salariosemanal es: ",salariosemanal)


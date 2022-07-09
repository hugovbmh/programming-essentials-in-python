m = int(input("Ingrese capital de Microsoft: "))
o = int(input("Ingrese capital de Oracle: "))
i = int(input("Ingrese capital de IBM: "))
total = m + o + i
print("La suma del capital es: ",total)
mp = (m*100)//total
print("El porcentaje de capital de Microsoft es: ",mp,"%")
op = (o*100)//total
print("El porcentaje de capital de Oracle es: ",op,"%")
ip = (i*100)//total
print("El porcentaje de capital de IBM es: ",ip,"%")
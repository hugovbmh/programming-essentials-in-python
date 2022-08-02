nombre = str(input("Ingresar apellidos y nombres: ")) 
cantidadhoras = int(input("Ingresar la cantidad de horas trabajadas: ")) 
valorhoras = int(input("Ingresar el valor de hora: ")) 
bruto = cantidadhoras*valorhoras
print("El sueldo bruto es: " , bruto)
descuento = bruto*0.13
print("El descuento de 13% de ley por aporte al SNP es: " , descuento)
bonofamiliar = bruto*0.07 
print("El bono familiar de 7% es: " , bonofamiliar)
sueldoneto = (bruto - descuento + bonofamiliar)
print("El sueldo neto es: " , sueldoneto)

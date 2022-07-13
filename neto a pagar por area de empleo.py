print("1.Seguridad")
print("2.Almacen")
print("3.Limpieza")

condicion = int(input("Ingrese la opcion de area de empleo : "))

horas = int(input("Ingrese horas trabajadas : "))
if(condicion == 1):
    
        neto1 = 10*horas

        if(neto1>700):
            impuesto1 = (10/100)*neto1
            netonuevo1 = neto1-impuesto1
            print(f"El neto de usted es : {netonuevo1}")

elif(condicion == 2):

        neto2 = 9*horas

        if(neto2>700):
            impuesto2  = 10/100*neto2
            netonuevo2 = neto2-impuesto         
            print(f"El neto de usted es : {netonuevo2}")

elif(condicion == 3):

        neto3 = 8*horas

        if(neto3>700):
            impuesto3 = 10/100*neto3
            netonuevo2 = neto3-impuesto
            print(f"El neto de usted es : {netonuevo3}")

else:
  
            print("Ingrese una opcion valida")

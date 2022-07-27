#Con respecto a los boletos que ofrece una vendedora de la Empresa Lima
#Metropolitana, el programa debe ingresar la numeración inicial y final de los
#boletos vendidos del tramo Callao a Lima cercado; así como también el precio
#del boleto. La Empresa otorga un incentivo de 20% respecto al importe de
#Boletos Vendidos solo si se vendieron más de 500 Boletos. Mostrar el
#incentivo.

x = int(input("Ingrese boletos vendidos: "))
p = int(input("Ingrese el precio del boleto: "))
if (x>500):
    incentivo = 0.20
    print("El incentivo es: ",x*p*incentivo)
else:
    print("No hay incentivo")

print("---DESCUENTO SEGUN EL NUMERO PAR E IMPAR DEL DIA---")
dia = int(input("Ingresar el numero del dia de la semana: "))
if (dia%2==0):
    print("El numero es par y HAY DESCUENTO")
else:
    print("El numero es impar y NO HAY DESCUENTO")

############################################################

print("---MOSTRAR SI PAGÓ O NO PAGÓ EL PRODUCTO---")
pago = str(input("¿Pagó el producto? si o no "))
if (pago=="si"):
    print("Pagó")
else:
    print("No pagó")

############################################################

print("---Inserte 5 numeros para ordenarlos en una lista---")
lista_numero = []
for x in range(5):
    num = int(input())
    lista_numero.append(num)
lista_numero.sort()
print(lista_numero)

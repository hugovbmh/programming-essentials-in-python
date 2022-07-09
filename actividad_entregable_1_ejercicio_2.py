print("---Refrescate---"); 
nombre = str(input("Ingresar nombre: "))
producto = str(input("Ingresar producto a consumir: "))
precio= int(input("Ingresar el precio del producto: "))
cantidad =int(input("Ingresar la cantidad: "))
subtotal = precio*cantidad
print("El subtotal es: ", subtotal)
igv = subtotal*0.18
print("El IGV de 18% del subtotal es: ", igv)
montototal = subtotal+igv
print("El monto total a pagar es: " , montototal)
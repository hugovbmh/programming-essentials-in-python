codigo = int(input("Ingresar codigo de usuario: ")) 
metrocubico = int(input("Ingresar la cantidad de metros cubicos obtenidos: ")) 
importe = metrocubico * 0.65
print("El importe inicial es: ", importe)
mantenimiento = importe*0.028
print("El Mantenimiento de Parques y Jardines (2.8%) es: " , mantenimiento)
relleno = importe*0.014
print("El Relleno Sanitario (1.4%) es: " , relleno)
mantenimientoG = importe*0.021
print("El Mantenimiento General (2.1%) es: " , mantenimientoG)
igv = importe*0.18
print("El IGV (18%) es: " , igv)
total = importe - mantenimiento - relleno - mantenimientoG - igv
print("El pago total es: ", total)
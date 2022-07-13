#Ejercicio 04: Convertir un numero de dia en letras. Use IF y elif
dia=int(input('Introduce un dia de la semana entre 1 y 7'))
print('El dia es: ',end='') #end concatenara el codigo de la siguiente linea
if dia==1:
  print('Lunes')
elif dia==2:
  print('Martes')
elif dia==3:
  print('Miercoles')
elif dia==4:
  print('Jueves')
elif dia==5:
  print('Viernes')
elif dia==6:
  print('Sabado')
elif dia==7:
  print('Domingo')
else:
  print('Incorrecto')
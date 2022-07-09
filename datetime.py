import datetime
def TiempoActual():
  print("HoraActual : ")
  today = datetime.datetime.strftime(datetime.datetime.today() , '%d/%m/%Y - %Hh/%Mm')
  print(today)

num = int(input("Ingrese numero de dias: "))
x = datetime.datetime.today() + datetime.timedelta(days = num)
TiempoActual()
print(f"Nueva fecha después de {num} dias: ")
print(datetime.datetime.strftime(x , '%d/%m/%Y-%Hh/%Mm'))
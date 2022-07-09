vuelto = int(input("Ingrese el vuelto: "))
c = vuelto//50
c1 = vuelto % 50
v = c1//20
v1 = c1 % 20
d = v1//10
d1 = v1%10
moneda5 = d1//5
moneda51 = d1%5
moneda1 = moneda51//1
print("Billetes de 50 :", c)
print("Billetes de 20 :", v)
print("Billetes de 10 :", d)
print("Monedas de 5 :", moneda5)
print("Monedas de 1 :", moneda1)
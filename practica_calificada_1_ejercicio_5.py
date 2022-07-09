num = [10,30,12, 13, 17, 50]
primo = []
p = 0
for xn in num:
    xcon = 0
    for i in range(1, xn + 1, 1):
        if(xn % i == 0):
            xcon = xcon + 1
    if (xcon <= 2):
        primo.insert(p,xn)
        p = p + 1
print("Los numeros primos son: ")
print(primo)


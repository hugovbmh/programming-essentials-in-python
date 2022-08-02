n1=int(input("Ingresa un numero: "))
n2=int(input("Ingresa otro numero: "))
if (n1!=n2):
    if (n1>n2):
        print("El numero", n1 ,"es mayor que ",n2)
    else:
        print("El numero", n2 ,"es mayor que ",n1)
else:
    print("Escriba 2 numeros diferentes")

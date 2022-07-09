codigo = ["P-01","P-02","P-03","P-04"]
frutas = ["Pera","Fresa","Manzana","Platano"]
precio = [3,4,5,2]
codigo = str(input("Ingrese el codigo: "))
if (codigo == "P-01"):
    print("El producto es: ",frutas[0])
    print("El precio es: ",precio[0])
elif (codigo == "P-02"):
    print("El producto es: ",frutas[1])
    print("El precio es: ",precio[1])
elif (codigo == "P-03"):
    print("El producto es: ",frutas[2])
    print("El precio es: ",precio[2])
elif (codigo == "P-04"):
    print("El producto es: ",frutas[3])
    print("El precio es: ",precio[3])
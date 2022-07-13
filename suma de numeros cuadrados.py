#Ejercicio 02: Llenar un vector con valores tipo float y calcular la suma de los cuadrados de dichos valores
v=[]
for i in range(10):
    v.append(float(input(f"Introduce el elemento {i}:")))
suma=0
for i in range(0,len(v)):
    suma+=v[i]**2 #Acumulador
print("La suma de los cuadrados es: ",suma)



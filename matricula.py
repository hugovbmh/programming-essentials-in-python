print('''En un colegio la pension:
Primaria (P): 460
Segundaria (S): 520
La matricula se calcula de la sgtem. manera:
M(añana) --> Matricula = 10% de la  pension
T(arde) --> Matricula = 5% de la  pension
N(oche) --> Matricula = 8% de la  pension''')

pension = str(input("Ingrese colegio: "))
if(pension=="P"):
    pensiondinero=460
else:
    pensiondinero=520
turno = str(input("Ingrese turno: "))
if(turno=="M"):
    descuento=0.10
elif(turno=="T"):
    descuento=0.05
else:
    descuento=0.08
matricula = pensiondinero*descuento
pago = pensiondinero + matricula

print("El neto a pagar es: ",pago)
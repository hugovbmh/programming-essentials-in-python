class Cuenta():
    def __init__(self,titular,cantidad=0): #Constructor
        self.__titular=titular #Atributo privado
        self.__cantidad=cantidad #Atributo privado

    @property
    def titular(self): #Getter(obtener datos)
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter #setter para asignar datos
    def titular(self,titular):
        self.__titular=titular

    def mostrar(self): #Imprimir los datos del titular de la cuenta
        return "Cuenta\n" + "Titular:" + self.titular + " - Cantidad :" + str(self.cantidad)
    
    def ingresar(self,cantidad): #Agregando dinero
        if cantidad>0:
            self.__cantidad=self.__cantidad + cantidad

    def retirar(self,cantidad): #Quitando dinero
        if cantidad>0:
            self.__cantidad=self.__cantidad - cantidad
#********************************************************

#Crear los objetos a partir de la clase Cuenta
cta_luis=Cuenta("Luis Llanos") #Instanciar la clase cuenta para crear el objeto cta_luis
cta_luis.ingresar(200)
cta_luis.ingresar(300)
cta_luis.retirar(100)
print("Datos:",cta_luis.mostrar())
cta_luis.titular='David Llanos' #Ejecuta el set para cambiar el nombre del titular
#cta_luis.cantidad=1000 # Error cantidad no tiene set
print("Datos:",cta_luis.mostrar())
#print(cta_luis.__titular) #Error porque el atributo__titular es privado(encapsulado)
print(cta_luis.titular)#ejecuta la propiedad titular para mostrar solo el nombre
print("------------------------------------------------")
cta_pedro=Cuenta("Pedro Ruiz Julca")
cta_pedro.ingresar(1000)
cta_pedro.retirar(200)
print("Datos:",cta_pedro.mostrar())
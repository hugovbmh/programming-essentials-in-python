class Persona: #Clase padre
    def __init__(self): #Constructor
        self.nombre=input("Ingrese nombre: ") #Atributo nombre
        self.edad=int(input("Ingrese la edad: ")) #Atributo edad
    
    def mostrar (self):
        print("Nombre:",self.nombre)
        print("Edad:", self.edad)

class Empleado(Persona): #Clase hija
    def __init__(self):
        super().__init__() #Invocando el constructor del padre
        self.sueldo=float(input("Ingrese sueldo: "))

    def mostrar(self):
        super().mostrar() #Ejecutar el metodo mostrar del padre
        print("Sueldo:",self.sueldo)

    def pagar_impuestos(self):
        if self.sueldo>3000:
            print("El empleado debe pagar impuestos")
        else:
            print("El empleado no paga impuesto")

#---------------------------------------------------------
#Creacion de objetos
#persona1=Persona() #Instancia, no olvidar que el constructor se ejecuta de manera automatica
#persona1.mostrar()
empleado_hugo=Empleado()
empleado_hugo.mostrar()
empleado_hugo.pagar_impuestos()
emp01=Empleado()
emp01.mostrar()
emp01.pagar_impuestos()
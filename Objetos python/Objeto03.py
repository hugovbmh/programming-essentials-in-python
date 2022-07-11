class Empleado:
    def __init__(self,nombres,apellidos):
        self.nombres=nombres
        self.apellidos=apellidos
    @property #cambia el metodo def email a un atributo
    def email(self):
        return '{}{}@senati.com'.format(self.nombres,self.apellidos)
    @property
    def fullname(self):
        return '{}{}'.format(self.nombres,self.apellidos)
    @fullname.setter#set --> asignar datos a fullname
    def fullname(self,nom):
        nombres,apellidos=nom.split('')#split convierte una cadena en una lista
        self.nombres=nombres
        self.apellidos=apellidos
#Crear objetos a partir de la clase Empleado
emp1=Empleado('Jhon',' Juarez ')
print(emp1.nombres)
print(emp1.email)        
print(emp1.fullname)  
emp2=Empleado('Jose',' Peralta ')
print(emp2.nombres)
print(emp2.email)        
print(emp2.fullname)  
#Creamos nuestra clase Persona
class Persona():
    #inicializamos Constructor con los parametros
    def __init__(self, nombre, edad):
        self.nombre=nombre #definimos que el atributo.nombre sera el nombre asignado
        self.edad=edad


#bloque principal
persona1=Persona("Richard", 23) #creando una instancia y pasando argumentos a la clase Persona
print(persona1.nombre)
print(persona1.edad)

class Persona2:
    def __init__(self, nombre, apellidos, edad):
        #acceso publico
        self.nombre=nombre

        #acceso protegido
        self._apellidos=apellidos

        #acceso privado
        self.__edad=edad

obj=Persona2("Maria", "Perez", 23)
#Acceder a la variable publica
print(obj.nombre)
#Acceder a la variable protegida
print(obj._apellidos)
#Acceder a la variable privada
print(obj._Persona2__edad)


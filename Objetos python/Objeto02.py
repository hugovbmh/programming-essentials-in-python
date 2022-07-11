class Circulo:
    _pi=3.1416 #Definiendo un atributo de clase
    def __init__(self,radio): #Constructor
        self.radio=radio
    def area(self):
        return self.radio*self.radio*self._pi

#Creando los objetos
cir1=Circulo(4) #Creando el obj cir1
cir2=Circulo(3) #Creando el obj cir2
micirculo=Circulo(8)
print(cir1.area())
print(cir2.area())
print(micirculo.area())
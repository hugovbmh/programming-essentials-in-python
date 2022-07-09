class direccion:
    num = 0
    calle = ""
    urb=""
    def direccion_final(self):
        print(self.calle+". #"+str(self.num)+". Urb."+self.urb)
direccion_01 = direccion()
direccion_01.num=int(input("Ingrese numero de casa: "))
direccion_01.calle=str(input("Ingrese la calle: "))
direccion_01.urb=str(input("Ingrese la urbanizacion: "))
print("La dirección es: ")
direccion_01.direccion_final()

##################################################################

class tienda:
    pro=''
    can=0
    pre=0
    
    def pre_final(self):
        if(self.can>=1 and self.can<=10):
            desc=0
        if(self.can>=11 and self.can<=20):
            desc=0.03
        if(self.can>=21):
            desc=0.05
        print('El precio final es: ',(self.can*self.pre)-((self.can*self.pre)*desc))
    
tienda01=tienda()
tienda01.pro=str(input('Ingrese el producto a llevar: '))
tienda01.can=int(input('Ingrese la cantidad a llevar: '))
tienda01.pre=float(input('Ingrese el precio del producto: '))
tienda01.pre_final()
class Usuario:
    def __init__(self,username,password,email):#Definimos el constructor
        #Definir atributos
        self.username=username
        self.password=password
        self.email=email
    #Definir metodos
    def __generar_passwrod(self,password): #metodo privado
        return password.upper() #upper convierte un dato a mayusculas
    def get_password(self): #metodo publico
        return self.password

#creando el objeto usuario1:
usuario1=Usuario('juan rivas','123A','jrivas@senati.pe')
print(usuario1.username)
print(usuario1.get_password())
#creando el objeto usuario2:
usuario2=Usuario('jan quispe','abcde','jquispe@senati.pe')
print(usuario2.username)
print(usuario2.get_password())
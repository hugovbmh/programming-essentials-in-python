#Usando estructure de datos
class Alumno(): #Estructura
    def __init__(self):
        self.nombre=''
        self.notas=[]
        self.final=0
num_alum=int(input('Cuantos alumnos tenemos?'))
while num_alum<1:
    num_alum=int(input('Cuantos alumnos tenemos?'))
clase=[] #vector con los alumnos de la clase
for i in range(0,num_alum):
    clase.append(Alumno()) #La clase alumno utiliza los atributos:nombre,nota y final
    clase[i].nombre=input(f'Introduce el nombre del alumno {i}:')
    notas=input(f'Introduce las notas del alumno {i} separadas por espacio:')
    for n in notas.split(' '): #Split permite dividir en una lista
        clase[i].notas.append(float(n))
print('Informe de notas finales')
for i in range(0,num_alum): #For para el control de los alumnos
    for j in range(0,len(clase[i].notas)): #For para el control de las notas
        clase[i].final += float(clase[i].notas[j])
    clase[i].final /=len(clase[i].notas)
    print(clase[i].nombre, ':' ,clase[i].final)

"""
Solución del laboratorio
"""

from custom_functions import temperature_methods
import statistics


nacio=[]

for i in range(0,12):
    try:
        temp=int(input("Escriba las temperaturas de la Guajira: "))
        nacio.append(temp)
    except ValueError:
        print("Solo se admiten numeros")

for i in range(0,12):
    try:
        temp=int(input("Escriba las temperaturas de Santander: "))
        nacio.append(temp)
    except ValueError:
        print("Solo se admiten numeros")


for i in range(0,12):
    try:
        temp=int(input("Escriba las temperaturas de Nariño: "))
        nacio.append(temp)
    except ValueError:
        print("Solo se admiten numeros")

guajira=nacio[0:12]
santander=nacio[12:24]
narigno=nacio[24:36]

meses= { 0:"enero", 1:"febrero",2:"marzo",3:"abril",4:"mayo",5:"junio",6:"julio",7:"agosto",8:"septiembre",9:"octubre",10:"noviembre",11:"diciembre",12:"enero",13:"febrero",14:"marzo",15:"abril",16:"mayo",17:"junio",18:"julio",19:"agosto",20:"septiembre",21:"octubre",22:"noviembre",23:"diciembre",24:"enero",25:"febrero",26:"marzo",27:"abril",28:"mayo",29:"junio",30:"julio",31:"agosto",32:"septiembre",33:"octubre",34:"noviembre",35:"diciembre"}

print("------------------------")
print("A)")
print()
#Aqui se saca el promedio de todas las temperaturas de cada departamento, con la funcion dada
promedio_guajira=temperature_methods.promedio(guajira)
promedio_santander=temperature_methods.promedio(santander)
promedio_narigno=temperature_methods.promedio(narigno)

print("El promedio de la Guajira es: ",promedio_guajira)
print("El promedio de Santander es: ",promedio_santander)
print("El promedio de  Nariño es: ",promedio_narigno)

print()
print("------------------------")
print("B)")
print()
#Aqui se suman todos los promedios y se le saca promedio con la funcion
promedio_nacional=temperature_methods.promedio(guajira+santander+narigno)
print("El promedio Nacional es: ",promedio_nacional)

print()
print("------------------------")
print("C)")
print()
#Aqui se usa la funcion para saber el mayor para saber cual es el mes mas caliente de cada departamento
mas_caliente_guajira=temperature_methods.componente_mayor(guajira)
mas_caliente_santander=temperature_methods.componente_mayor(santander)
mas_caliente_narigno=temperature_methods.componente_mayor(narigno)

print("El mas caliente de la Guajira es: ",mas_caliente_guajira)
print("El mas calinte Santander es: ",mas_caliente_santander)
print("El mas caliente de  Nariño es: ",mas_caliente_narigno)

print()
print("------------------------")
print("D)")
print()
#Aqui es para saber cual es el mas alto de los 3 departamentos
mas_alto_3=[mas_caliente_guajira,mas_caliente_santander,mas_caliente_narigno]
promedio_mas_alto_3=temperature_methods.promedio(mas_alto_3)
print("El promedio de los mas calientes de los 3 departamentos es: ",promedio_mas_alto_3)

print()
print("------------------------")
print("E)")
print()
#Aqui es para saber cual es el mas caliente de los 3 promedios
los_3_departamentos_calientes=[promedio_guajira,promedio_santander,promedio_narigno]
promedio_3_departamentos_calientes=temperature_methods.componente_mayor(los_3_departamentos_calientes)
print("El promedio mas caliente de los 3 departanentos es: ",promedio_3_departamentos_calientes)

print()
print("------------------------")
print("F)")
print()
#Aqui es para saber el mayor de todos
departamento_mayor=[mas_caliente_guajira,mas_caliente_santander,mas_caliente_narigno]
mayor_total=temperature_methods.componente_mayor(departamento_mayor)
print("-La Mayor de todos es: ",mayor_total)

#Se usa index para que este busque en esa lista el mayor
posicion=mas_alto_3.index(mayor_total)
n_dep=["guajira","santander","narigno"]
print("-La temperatura mayor del departamento se presenta en: ",(meses[posicion]))
print("-El departamento con mas calor fue: ",(n_dep[posicion]))

print()
print("------------------------")
print("G)")
print()
###################### Froma 1

#acu=0
#for a in guajira:
 #   x=promedio_guajira-a
  #  acu=acu+x

#d1=math.sqrt((acu*acu)/2)
#print("La desviacion estandar en la Guajira es: ",d1)

#acu2=0
#for b in santander:
  #  y=promedio_santander-b
   # acu2=acu2+y

#d2=math.sqrt((acu2*acu2)/2)
#print("La desviacion estandar en Santander es: ",d2)

#acu3=0
#for c in narigno:
 #   z=promedio_narigno-c
  #  acu3=acu3+z

#d3=math.sqrt((acu3*acu3)/2)
#print("La desviacion estandar en Nariño es: ",d3)

###################### Forma 2
d1=temperature_methods.desviacion_estandar(guajira)
d2=temperature_methods.desviacion_estandar(santander)
d3=temperature_methods.desviacion_estandar(narigno)

print("La desviacion estandar de la guajira es: ",d1)
print("La desviacion estandar de narigno es: ",d2)
print("La desviacion estandar de santander es: ",d3)


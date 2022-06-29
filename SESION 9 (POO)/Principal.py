

from Alumno import *

#Creando objetos
persona1=Persona("Nicolas","Guzman",30)
print("Me llamo", persona1.nombre)
print("Mis apellidos",persona1.apellidos)
print("y tengo",persona1.edad," años")
persona1.comer()
persona1.caminando()

persona2=Persona("Bruno","DFGH",20)
print(persona2.nombre)
#llamando alumno
alumno1=Alumno("Miguel","S0202201")
print(alumno1.promedio())
print(alumno1.comer())


mi_archivo=open("persona.txt","w")
try:
    mi_archivo.write(f"esta es una persona {alumno1.nombre}\n")
    mi_archivo.write(f"Otra persona {persona1.nombre}")
finally:
    mi_archivo.close()



lista_alumnos_aprobados=[]
lista_alumnos_reprobados=[]

while True:
    nombre= input("Anota tu nombre: ")
    calificacion= int(input("Anota tu calificacion final: "))
    if calificacion >=0 and calificacion <=69:
        lista_alumnos_reprobados.append([nombre])
        #lista_alumnos_reprobados.append([calificacion])


    elif calificacion >=70 and calificacion <=100:
        lista_alumnos_aprobados.append(nombre),
        lista_alumnos_aprobados.append(calificacion)

    condicion=input("¿Desea hacer otro registro?(S=si N=no): ")
    if condicion=="n" or condicion=="N":
        break

print("Lista reprobados",lista_alumnos_reprobados)
print(lista_alumnos_reprobados)

print("Lista aprobados",lista_alumnos_aprobados)

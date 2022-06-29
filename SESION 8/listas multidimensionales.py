

lista_alumnos=[
    ["Victor","Mateos Francisco","victor@gmail.com"],
    ["Bruno", "Cruz guzmán","bruno@gmail.com"],
    ["Diana","Guzman Ines","mari@gmail.com"]
]
print(lista_alumnos)
#solo una lista
print(lista_alumnos[0])
#mostrar un registro
print(lista_alumnos[1][2])
#enlistar los datos nombres nomas
for alumnos in lista_alumnos:
    print(alumnos[0])

#anlistar todos los datos de un  alumno
for alumnos in lista_alumnos:
    for elemento in alumnos:
        if alumnos.index(elemento)==0:
            print(f"Nombre alumno: {elemento}")
        elif alumnos.index(elemento)==1:
            print(f"Apellidos: {elemento}")
        elif alumnos.index(elemento)==2:
            print(f"Correo: {elemento}")
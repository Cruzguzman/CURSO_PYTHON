
lista_alumnos_isic=[
        ["Miguel Ángel","Olivera Ortega","miguel@gmail.com"],
        ["Marina","Toribio Salgado","marina@gmail.com"],
        ["Victor","Mateos Francisco","victor@gmail.com"],
        ["Gabriel","Garcia Dolores","gabriel@gmail.com"]

]
print(lista_alumnos_isic)

#mostrar una lista determinada
print(lista_alumnos_isic[1])

#mostrar un registro
print(lista_alumnos_isic[3][2])

#mostrar nombres
for nombres in lista_alumnos_isic:
        print(nombres[0])
        print(nombres[1])

for alumnos in lista_alumnos_isic:
        for elemento in alumnos:
                if alumnos.index(elemento)==0:
                        print(f"Nombre:{elemento}")
                elif alumnos.index(elemento)==1:
                        print(f"Apellidos: {elemento}")
                elif alumnos.index(elemento)==2:
                        print(f"Correo: {elemento}")
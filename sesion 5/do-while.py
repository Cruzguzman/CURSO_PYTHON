

while True:
    nombre_alumno=input("Anota el nombre del alumno: ")
    apellidos_alumno=input("Anota el apellido paterno: ")
    edad_alumno=input("Anota la edad: ")
    print(f"Alumno : {nombre_alumno},{apellidos_alumno},{edad_alumno} registrado correctamente")
    condicion=input("¿Desea hacer otro registro?(S=si N=no): ")
    if condicion=="n" or condicion=="N":
        break
print("Gracias por usar la calculadora")

nombre_alumno=input("Anota un nombre de alumno: ")

alumno1="Victor"
alumno2="Bruno"
alumno3="Diana"
alumno4="Cira"

matricula_alumno1="S2112201"
matricula_alumno2="S2112202"
matricula_alumno3="S2112203"
matricula_alumno4="S2112204"

if nombre_alumno==alumno1 or nombre_alumno==alumno2 or nombre_alumno==alumno3 or nombre_alumno==alumno4:
    matricula_alumno = input("Anota la matricula: ")
    print("Bienvenido al curso de Python")
    if matricula_alumno==matricula_alumno1 or matricula_alumno==matricula_alumno2 or matricula_alumno==matricula_alumno3 or matricula_alumno==matricula_alumno4:
        print(f"Matricula asignada a {nombre_alumno}")
    else:
        print("Matricula no asignada")
else:
    print("Alumno no registrado")




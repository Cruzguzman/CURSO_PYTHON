
nombre_alumno=input("Aota tu nombre : ")
calificacion_alumno=int(input("Anota tu calificacion : "))
mensaje=None

if 0<= calificacion_alumno <=69:
    mensaje="Calificacion no aprobable"
elif 70<= calificacion_alumno <=74:
    mensaje="Calificacion suficiente"
elif 75<= calificacion_alumno <=84:
    mensaje="Calificacion buena"
elif 85<= calificacion_alumno <=94:
    mensaje ="Calificacion Notable"
elif 95 <= calificacion_alumno <=100:
    mensaje="Calificacion Excelente Felicidades!!!!!!"
print(f"{nombre_alumno} su calificacion({calificacion_alumno})es: {mensaje}")

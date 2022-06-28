#para sesion uno
import math

numero_uno=float(input("Anota una cantidad entera: "))
numero_dos=int(input("Anota otra cantidad entera: "))
#interpolacion para mandar msg en pantalla
#f literal

print(f"La suma de: {numero_uno} mas {numero_dos} es: " ,numero_uno+numero_dos)
print(f"La resta de {numero_uno} menos {numero_dos} es igual a: ", numero_uno-numero_dos)
print(f"La multiplicacion de {numero_uno} por {numero_dos} es: ",numero_uno*numero_dos)
print(f"La division de {numero_uno} entre {numero_dos} es: ", numero_uno/numero_dos)
print(f"La division entera entre {numero_uno} y {numero_dos} es igual a: ", numero_uno//numero_dos)
print(f"El residuo de la divison de {numero_uno} entre {numero_dos} es igual a: ", numero_uno%numero_dos)
print("El resultado de la potencia es", math.pow(numero_uno,numero_dos))
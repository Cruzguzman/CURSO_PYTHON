import math

numero1=int(input("Anota un numero entero: "))
numero2=float(input("Anota otro numero: "))
#suma=numero1+numero2
#print(suma)
print(f"La suma de {numero1} mas {numero2} es igual a: ",numero1+numero2)
print(f"La resta de {numero1} menos {numero2} es igual a: ",numero1-numero2)
print(f"La multiplicacion de {numero1} por {numero2} es igual a: ",numero1*numero2)
print(f"La division de {numero1} entre {numero2} es igual a: ",numero1/numero2)
print(f"La division entera de {numero1} entre {numero2} es igual a: ",numero1//numero2)
print(f"El residuo o modulo de la division  de {numero1} entre {numero2} es igual a: ",numero1%numero2)
base=5
eleva=2
print("El resultado de la potenciacion es igual a: ",math.pow(base,eleva))
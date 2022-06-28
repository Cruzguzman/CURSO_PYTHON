
def menu():
    print("Para calcular, elija algunas opciones")
    print("1-Para suma")
    print("2-Para resta")
    print("3-Para multiplicacion")
    print("4-Para division")

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    return a/b

def validando_opciones():
    opcion = int(input("Anota una opcion(1=Suma,2=Resta,3=Mult.,4=Div.: "))
    numero1 = int(input("Anota un numero: "))
    numero2 = int(input("Anota otro numero: "))
    if opcion == 1:
        print(suma(numero1, numero2))
    elif opcion == 2:
        print(resta(numero1, numero2))
    elif opcion == 3:
        print(multiplicacion(numero1, numero2))
    elif opcion == 4:
        print(division(numero1, numero2))

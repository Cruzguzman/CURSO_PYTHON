

import  paquete_funciones

paquete_funciones.menu()
paquete_funciones.validando_opciones()

while True:
    decision = input("¿Desea hacer otra operacion?. S=Si, N=N0: ")
    paquete_funciones.menu()
    paquete_funciones.validando_opciones()
    if decision == "n" or decision == "N":
        break
print("Gracias por usar la calculadora")
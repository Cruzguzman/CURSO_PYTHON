
lista_nombres=["Diana","Bruno","Victor","Gabriel"]
lista_numeros=[2,8,12,1,90]


#print(lista_numeros)
print(lista_nombres)

#tamaño lista
print(len(lista_nombres))
#acceder a una pocision
print(lista_nombres[1])

#imprimir rango determinado
print(lista_nombres[2][3])

#agregar un elemento
lista_nombres.insert(3,"Cira")
print(lista_nombres)

#iterar
#for elementos in lista_nombres:
 #   print(elementos)

#agregar
lista_nombres.append("Miguel")
print(lista_nombres)

#quitar un elemento
lista_nombres.remove("Bruno")
print(lista_nombres)

#eliminar el ultimo elemento
lista_nombres.pop()
print(lista_nombres)

#limpiar lista
lista_nombres.clear()
print(lista_nombres)

#eliminar lista
#del lista_nombres
#print(lista_nombres)

#ordenar
lista_numeros.sort()
print(lista_numeros)
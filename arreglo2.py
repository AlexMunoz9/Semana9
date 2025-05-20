#arreglos de tipo entero

array_int = [5, 4, 9, 2, 1]

#arreglar de mayor a menor
array_int.sort()
print("Arreglo de enteros ordenados:", array_int)

#arreglar de menor a mayor
array_int.sort(reverse=True)
print("Arreglo de enteros ordenados:", array_int)

#Buscar un elemento en el arreglo
elemento = 4
if elemento in array_int:
    print(f"El elemento {elemento} se encuentra en el arreglo.")
else:
    print(f"El elemento {elemento} no se encuentra en el arreglo.")
    
#insertar un elemento en el arreglo
array_int.append(6)
print("Arreglo de enteros después de insertar 6:", array_int)
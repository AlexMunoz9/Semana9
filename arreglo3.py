array_str  = ["uno", "dos", "tres", "cuatro", "cinco"]
print("Array de cadenas:", array_str)

#instertar un elemente al inicio del arreglo
array_str.insert(3, "cero")
print("Arreglo de cadenas después de insertar 'cero' al inicio:", array_str)

#eliminar un elemento del arreglo
array_str.remove("tres")
print("Arreglo de cadenas después de eliminar 'tres':", array_str)

#otra forma de eliminar un elemento del arreglo
array_str.pop(2)
print("Arreglo de cadenas después de eliminar el elemento en la posición 2:", array_str)
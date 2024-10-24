entero = 8
print(entero)  # Salida: 8

flotante = 10.5
print(flotante)  # Salida: 10.5

cadena1 = "ejercicio"
print(cadena1)  # Salida: ejercicio

mi_conjunto = {entero, flotante, cadena1}
print(mi_conjunto)  # Salida: {entero,flotante, cadena1}

mi_conjunto.add(4)
print(mi_conjunto)  # Salida: {1, 2, 3, 4}

mi_conjunto.update([5, 6])
print(mi_conjunto)  # Salida: {1, 2, 3, 4, 5, 6}
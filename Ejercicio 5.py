'''Ejercicio 5: Suma de Números Pares
Escribe un programa que calcule la suma de todos los números pares del 1 al 100'''

# Inicializamos la suma en 0
suma_pares = 0

# Iteramos a través de los números del 1 al 100
for numero in range(1, 101):
    # Verificamos si el número es par
    if numero % 2 == 0:
        suma_pares += numero  # Sumamos el número par a la suma total

# Mostramos el resultado
print("La suma de todos los números pares del 1 al 100 es:", suma_pares)
'''Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.'''

# Solicitar al usuario que ingrese una lista de números separados por comas
entrada = input("Ingresa una lista de números separados por comas: ")

# Convertir la entrada en una lista de números
numeros = [float(num) for num in entrada.split(",")]

# Sumar todos los números en la lista
suma_total = sum(numeros)

# Mostrar el resultado
print(f"La suma de los números es: {suma_total}")
'''Ejercicio 18: Contador de Palabras

Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario'''



# Solicitar al usuario que ingrese una oración
oracion = input("Por favor, ingresa una oración: ")

# Contar las palabras en la oración
cantidad_palabras = len(oracion.split())

# Mostrar el resultado
print(f"La cantidad de palabras en la oración es: {cantidad_palabras}")
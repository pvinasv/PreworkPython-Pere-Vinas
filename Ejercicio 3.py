'''Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.'''

# Solicitar la edad al usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Determinar si es mayor de edad
if edad >= 18:
    print("Mayor de edad.")
else:
    print("No mayor de edad.")
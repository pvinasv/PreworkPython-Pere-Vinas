''' Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
'''

# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Solicitar al usuario que ingrese la temperatura en Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Llamar a la función y mostrar el resultado
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

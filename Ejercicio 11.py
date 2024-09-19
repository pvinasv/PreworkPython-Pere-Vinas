''' Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.'''

from datetime import datetime

# Solicitar el año de nacimiento al usuario
anio_nacimiento = int(input("Por favor, ingresa tu año de nacimiento: "))

# Obtener el año actual
anio_actual = datetime.now().year

# Calcular la edad
edad = anio_actual - anio_nacimiento

# Mostrar la edad
print(f"Tienes {edad} años.")
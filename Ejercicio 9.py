'''Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.'''

def convertir_dolares_a_euros(dolares):
    tasa_cambio = 0.85
    euros = dolares * tasa_cambio
    return euros

# Solicitar al usuario la cantidad de dólares
cantidad_dolares = float(input("Introduce la cantidad de dólares que deseas convertir a euros: "))
cantidad_euros = convertir_dolares_a_euros(cantidad_dolares)

print(f"{cantidad_dolares} dólares son equivalentes a {cantidad_euros:.2f} euros.")
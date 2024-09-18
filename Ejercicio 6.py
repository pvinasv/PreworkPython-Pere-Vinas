'''Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''

def es_palindromo(palabra):
    # Convertimos la palabra a minúsculas y eliminamos espacios
    palabra = palabra.replace(" ", "").lower()
    # Comparamos la palabra con su reverso
    return palabra == palabra[::-1]

# Solicitamos al usuario que ingrese una palabra
entrada = input("Ingresa una palabra: ")

# Verificamos si es un palíndromo
if es_palindromo(entrada):
    print(f"La palabra '{entrada}' es un palíndromo.")
else:
    print(f"La palabra '{entrada}' no es un palíndromo.")
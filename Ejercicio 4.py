'''Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.'''

def contar_vocales(palabra):
    # Definimos las vocales
    vocales = "aeiouAEIOU"
    contador = 0
    
    # Contamos las vocales en la palabra
    for letra in palabra:
        if letra in vocales:
            contador += 1
            
    return contador

# Solicitamos al usuario que ingrese una palabra
palabra_usuario = input("Por favor, ingresa una palabra: ")
numero_vocales = contar_vocales(palabra_usuario)

print(f"La palabra '{palabra_usuario}' tiene {numero_vocales} vocales.")

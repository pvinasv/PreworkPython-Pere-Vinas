'''
Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.'''



def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero*0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicitar al usuario que ingrese un número
numero_usuario = int(input("Ingresa un número: "))

# Verificar si el número es primo
if es_primo(numero_usuario):
    print(f"{numero_usuario} es un número primo.")
else:
    print(f"{numero_usuario} no es un número primo.")
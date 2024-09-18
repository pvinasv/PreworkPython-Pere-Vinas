'''Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''

# Solicitar al usuario que ingrese un número del 1 al 7
numero_dia = int(input("Ingresa un número del 1 al 7: "))

# Diccionario para mapear números a días de la semana
dias_de_la_semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

# Verificar si el número ingresado es válido
if numero_dia in dias_de_la_semana:
    print(f"El día correspondiente es: {dias_de_la_semana[numero_dia]}")
else:
    print("Por favor, ingresa un número válido entre 1 y 7.")

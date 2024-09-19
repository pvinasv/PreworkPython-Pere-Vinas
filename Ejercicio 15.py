'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.'''


def convertir_minutos_a_horas(minutos):
    horas = minutos // 60  # División entera para obtener las horas
    minutos_restantes = minutos % 60  # Módulo para obtener los minutos restantes
    return horas, minutos_restantes

# Ejemplo de uso
minutos_input = int(input("Introduce el número de minutos: "))
horas, minutos = convertir_minutos_a_horas(minutos_input)
print(f"{minutos_input} minutos son {horas} horas y {minutos} minutos.")
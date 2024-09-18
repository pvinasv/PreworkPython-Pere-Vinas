'''Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''

def calcular_total(cuenta):
    propina = cuenta * 0.15  # Calcula el 15% de la cuenta
    total = cuenta + propina  # Suma la cuenta y la propina
    return total

# Solicitar al usuario que ingrese el total de la cuenta
total_cuenta = float(input("Ingrese el total de la cuenta: "))

# Calcular el total a pagar
total_a_pagar = calcular_total(total_cuenta)

# Mostrar el resultado
print(f"Total a pagar: {total_a_pagar:.2f}")
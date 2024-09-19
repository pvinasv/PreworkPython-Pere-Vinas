'''Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.'''


def calcular_precio_final(precio_original):
    descuento = 0.20  # 20% de descuento
    precio_final = precio_original * (1 - descuento)
    return precio_final

# Ejemplo de uso
precio_original = float(input("Introduce el precio original del artículo: "))
precio_final = calcular_precio_final(precio_original)
print(f"El precio final después de aplicar el descuento del 20% es: {precio_final:.2f}")

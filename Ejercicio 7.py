'''Ejercicio 7: Calculadora Simple
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.'''

def calcular():
    print("Bienvenido a la calculadora simple")
    print("Selecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        eleccion = input("Ingresa el número de la operación (1/2/3/4): ")

        if eleccion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if eleccion == '1':
                resultado = num1 + num2
                print(f"La suma de {num1} y {num2} es: {resultado}")
            elif eleccion == '2':
                resultado = num1 - num2
                print(f"La resta de {num1} y {num2} es: {resultado}")
            elif eleccion == '3':
                resultado = num1 * num2
                print(f"La multiplicación de {num1} y {num2} es: {resultado}")
            elif eleccion == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"La división de {num1} entre {num2} es: {resultado}")
                else:
                    print("Error: No se puede dividir entre cero.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

calcular()

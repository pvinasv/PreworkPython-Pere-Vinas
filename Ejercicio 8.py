'''Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.'''

def calcular_imc(peso, altura):
    imc = peso / (altura*2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    print("Bienvenido al calculador de IMC")
    peso = float(input("Por favor, ingresa tu peso en kilogramos: "))
    altura = float(input("Por favor, ingresa tu altura en metros: "))
    
    imc = calcular_imc(peso, altura)
    interpretacion = interpretar_imc(imc)
    
    print(f"Tu IMC es: {imc:.2f}")
    print(f"Interpretación: {interpretacion}")

if __name__ == "__main__":
    main()
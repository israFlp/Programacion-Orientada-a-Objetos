"""
Programa: Calculadora de Área de un Triángulo
Descripción: Este programa solicita al usuario la base y la altura de un triángulo,
calcula el área utilizando la fórmula (base * altura) / 2 y muestra el resultado.
También valida que los valores ingresados sean positivos.
"""

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo dado su base y altura.
    :param base: Base del triángulo (float).
    :param altura: Altura del triángulo (float).
    :return: Área del triángulo (float).
    """
    return (base * altura) / 2


# Función principal
def main():
    """
    Solicita al usuario la base y la altura del triángulo,
    valida que sean números positivos y muestra el área calculada.
    """
    print("Calculadora de Área de un Triángulo")

    # Solicitar la base del triángulo
    base_valida = False
    while not base_valida:
        try:
            base = float(input("Ingrese la base del triángulo (en cm): "))
            if base > 0:
                base_valida = True
            else:
                print("La base debe ser un número positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    # Solicitar la altura del triángulo
    altura_valida = False
    while not altura_valida:
        try:
            altura = float(input("Ingrese la altura del triángulo (en cm): "))
            if altura > 0:
                altura_valida = True
            else:
                print("La altura debe ser un número positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    # Calcular y mostrar el área
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo con base {base} cm y altura {altura} cm es: {area:.2f} cm²")


# Verificar si el programa se ejecuta como script principal
if __name__ == "__main__":
    main()

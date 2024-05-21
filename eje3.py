def main():
    print("")
    rango = input("Digite el rango al cual pertenece (1, 2 o 3): ")
    print("")

    # Validar que el rango ingresado sea un número válido
    if rango not in ['1', '2', '3']:
        print("Rango inválido. Por favor, ingrese 1, 2 o 3.")
        return

    sueldo = input("Digite el valor de sueldo mensual (en números): ")
    print("")

    # Validar que el sueldo ingresado sea un número válido
    if not sueldo.isdigit():
        print("Sueldo inválido. Por favor, ingrese un número válido.")
        return

    sueldo = int(sueldo)

    # Calcular la asignación en función del valor de rango y sueldo ingresados
    if rango == '1':
        asig = sueldo * 83 / 100
    elif rango == '2':
        asig = sueldo * 120 / 100
    elif rango == '3':
        asig = sueldo * 500 / 100

    print(f"Su asignación, según su rango, será de: {asig:.2f} pesos argentinos")
    print("")

if __name__ == "__main__":
    main()

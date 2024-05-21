def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

def main():
    while True:
        print("\nCalculadora Simple")
        print("Seleccione la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Ingrese su opción (1/2/3/4/5): ")

        if opcion == '5':
            print("Saliendo...")
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")
                continue

            if opcion == '1':
                print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
            elif opcion == '4':
                resultado = division(num1, num2)
                print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
def calculadora():
    while True:
        print("\n--- CALCULADORA ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("Saliendo de la calculadora...")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            print("Resultado:", num1 + num2)
        elif opcion == "2":
            print("Resultado:", num1 - num2)
        elif opcion == "3":
            print("Resultado:", num1 * num2)
        elif opcion == "4":
            if num2 != 0:
                print("Resultado:", num1 / num2)
            else:
                print("Error: No se puede dividir por cero")
        elif opcion == "5":
            print("Resultado:", num1 ** num2)
        else:
            print("Opción inválida")

calculadora()
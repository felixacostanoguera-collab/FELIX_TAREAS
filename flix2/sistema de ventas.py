ventas = []

def registrar_venta():
    producto = input("Producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))

    total = precio * cantidad
    ventas.append(total)

    print("Venta registrada. Total:", total)

def mostrar_resumen():
    if not ventas:
        print("No hay ventas")
        return

    print("Total de ventas:", sum(ventas))
    print("Cantidad de ventas:", len(ventas))

while True:
    print("\n--- SISTEMA DE VENTAS ---")
    print("1. Registrar venta")
    print("2. Ver resumen")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        registrar_venta()
    elif opcion == "2":
        mostrar_resumen()
    elif opcion == "0":
        break
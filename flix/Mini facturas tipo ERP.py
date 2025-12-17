ARCHIVO = "facturas.txt"

def crear_factura():
    cliente = input("Cliente: ")
    productos = []
    total = 0

    while True:
        nombre = input("Producto (o ENTER para terminar): ")
        if nombre == "":
            break
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        subtotal = precio * cantidad
        productos.append((nombre, cantidad, subtotal))
        total += subtotal

    with open(ARCHIVO, "a") as f:
        f.write(f"{cliente}|{total}\n")

    print("\n--- FACTURA ---")
    for p in productos:
        print(f"{p[0]} x{p[1]} = {p[2]}")
    print("TOTAL:", total)

def ver_facturas():
    try:
        with open(ARCHIVO, "r") as f:
            for linea in f:
                cliente, total = linea.strip().split("|")
                print(f"Cliente: {cliente} - Total: {total}")
    except FileNotFoundError:
        print("No hay facturas")

while True:
    print("\n--- MINI ERP ---")
    print("1. Crear factura")
    print("2. Ver facturas")
    print("0. Salir")

    op = input("Opción: ")

    if op == "1":
        crear_factura()
    elif op == "2":
        ver_facturas()
    elif op == "0":
        break
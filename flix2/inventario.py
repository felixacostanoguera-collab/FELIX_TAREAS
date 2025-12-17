inventario = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("Producto agregado")

def mostrar_inventario():
    if not inventario:
        print("Inventario vacío")
        return

    for p in inventario:
        print(f"{p['nombre']} - Precio: {p['precio']} - Cantidad: {p['cantidad']}")

def valor_total():
    total = sum(p["precio"] * p["cantidad"] for p in inventario)
    print("Valor total del inventario:", total)

while True:
    print("\n--- INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Valor total")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        valor_total()
    elif opcion == "0":
        break
    else:
        print("Opción inválida")
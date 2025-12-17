ARCHIVO = "movimientos.txt"
saldo = 1000000
PIN = "1234"

def guardar_movimiento(texto):
    with open(ARCHIVO, "a") as f:
        f.write(texto + "\n")

def autenticar():
    for _ in range(3):
        pin = input("Ingrese PIN: ")
        if pin == PIN:
            return True
        print("PIN incorrecto")
    return False

def consultar_saldo():
    print("Saldo disponible:", saldo)

def depositar():
    global saldo
    monto = float(input("Monto a depositar: "))
    saldo += monto
    guardar_movimiento(f"Depósito: {monto}")
    print("Depósito exitoso")

def retirar():
    global saldo
    monto = float(input("Monto a retirar: "))
    if monto <= saldo:
        saldo -= monto
        guardar_movimiento(f"Retiro: {monto}")
        print("Retiro exitoso")
    else:
        print("Saldo insuficiente")

if autenticar():
    while True:
        print("\n--- CAJERO AUTOMÁTICO ---")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("0. Salir")

        op = input("Opción: ")

        if op == "1":
            consultar_saldo()
        elif op == "2":
            depositar()
        elif op == "3":
            retirar()
        elif op == "0":
            break
else:
    print("Tarjeta bloqueada")
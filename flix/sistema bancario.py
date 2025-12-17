ARCHIVO = "cuentas.txt"

def cargar_cuentas():
    cuentas = {}
    try:
        with open(ARCHIVO, "r") as f:
            for linea in f:
                nro, nombre, saldo = linea.strip().split(",")
                cuentas[nro] = {"nombre": nombre, "saldo": float(saldo)}
    except FileNotFoundError:
        pass
    return cuentas

def guardar_cuentas(cuentas):
    with open(ARCHIVO, "w") as f:
        for nro, datos in cuentas.items():
            f.write(f"{nro},{datos['nombre']},{datos['saldo']}\n")

def crear_cuenta(cuentas):
    nro = input("Número de cuenta: ")
    if nro in cuentas:
        print("Cuenta ya existe")
        return
    nombre = input("Titular: ")
    cuentas[nro] = {"nombre": nombre, "saldo": 0}
    guardar_cuentas(cuentas)
    print("Cuenta creada")

def depositar(cuentas):
    nro = input("Cuenta: ")
    monto = float(input("Monto: "))
    if nro in cuentas and monto > 0:
        cuentas[nro]["saldo"] += monto
        guardar_cuentas(cuentas)
        print("Depósito exitoso")

def retirar(cuentas):
    nro = input("Cuenta: ")
    monto = float(input("Monto: "))
    if nro in cuentas and cuentas[nro]["saldo"] >= monto:
        cuentas[nro]["saldo"] -= monto
        guardar_cuentas(cuentas)
        print("Retiro exitoso")
    else:
        print("Fondos insuficientes")

def transferir(cuentas):
    origen = input("Cuenta origen: ")
    destino = input("Cuenta destino: ")
    monto = float(input("Monto: "))

    if origen in cuentas and destino in cuentas:
        if cuentas[origen]["saldo"] >= monto:
            cuentas[origen]["saldo"] -= monto
            cuentas[destino]["saldo"] += monto
            guardar_cuentas(cuentas)
            print("Transferencia realizada")
        else:
            print("Saldo insuficiente")

cuentas = cargar_cuentas()

while True:
    print("\n--- SISTEMA BANCARIO ---")
    print("1. Crear cuenta")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Transferir")
    print("0. Salir")

    op = input("Opción: ")

    if op == "1":
        crear_cuenta(cuentas)
    elif op == "2":
        depositar(cuentas)
    elif op == "3":
        retirar(cuentas)
    elif op == "4":
        transferir(cuentas)
    elif op == "0":
        break
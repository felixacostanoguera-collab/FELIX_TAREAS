usuarios = {}

def registrar():
    usuario = input("Nuevo usuario: ")
    clave = input("Contraseña: ")
    usuarios[usuario] = clave
    print("Usuario registrado")

def login():
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario] == clave:
        print("Acceso concedido")
    else:
        print("Credenciales incorrectas")

while True:
    print("\n--- SISTEMA DE USUARIOS ---")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        registrar()
    elif opcion == "2":
        login()
    elif opcion == "0":
        break
tareas = []

def agregar_tarea():
    titulo = input("Título de la tarea: ")
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada")

def listar_tareas():
    if not tareas:
        print("No hay tareas")
        return

    for i, tarea in enumerate(tareas, start=1):
        estado = "✔" if tarea["completada"] else "✖"
        print(f"{i}. {tarea['titulo']} [{estado}]")

def completar_tarea():
    listar_tareas()
    indice = int(input("Número de tarea a completar: ")) - 1
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print("Tarea completada")
    else:
        print("Tarea inválida")

while True:
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("0. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()
    elif opcion == "3":
        completar_tarea()
    elif opcion == "0":
        break
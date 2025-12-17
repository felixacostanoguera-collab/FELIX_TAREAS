print("--- MOTOR DE DECISIONES (IA SIMPLE) ---")

edad = int(input("Edad: "))
ingreso = float(input("Ingreso mensual: "))
historial = input("Historial crediticio (bueno/malo): ").lower()

puntaje = 0

if edad >= 21:
    puntaje += 2
if ingreso >= 3000000:
    puntaje += 3
if historial == "bueno":
    puntaje += 4

print("\n--- EVALUACIÓN ---")
print("Puntaje:", puntaje)

if puntaje >= 7:
    print("✅ CRÉDITO APROBADO")
elif puntaje >= 5:
    print("⚠ CRÉDITO EN REVISIÓN")
else:
    print("❌ CRÉDITO RECHAZADO")
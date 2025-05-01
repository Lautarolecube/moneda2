def guardar_archivo(base, moneda, monto):
    with open("historial.txt", "a") as file:
        file.write(f"Moneda base: {base}, Moneda: {moneda}, Monto convertido: {monto:.2f}\n")
    print("\nHistorial guardado exitosamente.")

def historial():
    try:
        with open("historial.txt", "r") as file:
            print("\nHistorial de conversiones:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("\nNo hay historial disponible todavía.")

print("Conversor de monedas con historial")

opcion = input("Bienvenido, ¿qué desea hacer? \n1. Convertir moneda \n2. Ver historial de conversiones \nZ. Salir \n").strip()

if opcion.lower() == 'z':
    print("Saliendo del programa...")
    exit()

elif opcion == '2':
    historial()

elif opcion == '1':
    while True:
        conversor = input("\n¿A qué moneda desea convertir? (Base en pesos ARS): \nA. USD \nB. EUR \nC. BRL \nZ. Salir \n").strip()

        if conversor.lower() == 'a':
            moneda = "USD"
            tasa = 1150

        elif conversor.lower() == 'b':
            moneda = "EUR"
            tasa = 1300

        elif conversor.lower() == 'c':
            moneda = "BRL"
            tasa = 250

        elif conversor.lower() == 'z':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
            continue

        try:
            pesos = float(input("Ingrese el monto en pesos ARS: "))
            convertido = pesos / tasa
            print(f"\nEl monto en {moneda} es: {convertido:.2f}")
            guardar_archivo("ARS", moneda, convertido)
        except ValueError:
            print("Error: ingrese un valor numérico válido.")

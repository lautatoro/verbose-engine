class Deudor:
    def __init__(self, dni="", apellido="", nombre="", dni_cotitular="", apellido_cotitular="",
                 nombre_cotitular="", monto_adeudado=0.0, año_deuda=0):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.dni_cotitular = dni_cotitular
        self.apellido_cotitular = apellido_cotitular
        self.nombre_cotitular = nombre_cotitular
        self.monto_adeudado = monto_adeudado
        self.año_deuda = año_deuda

    def calcular_deuda_actual(self):
        año_actual = 2025
        años = año_actual - self.año_deuda
        deuda_actual = self.monto_adeudado * ((1 + 0.21) ** años)
        return round(deuda_actual, 2)

    def realizar_plan_de_pago(self, cuotas):
        deuda_actual = self.calcular_deuda_actual()
        if cuotas <= 3:
            interes = 0
        elif 4 <= cuotas <= 6:
            interes = 0.10
        elif 7 <= cuotas <= 12:
            interes = 0.19
        else:
            print("Cantidad de cuotas no válida (máx 12).")
            return None
        deuda_total = deuda_actual * (1 + interes)
        valor_cuota = deuda_total / cuotas
        return round(valor_cuota, 2)

    def cambiar_cotitular(self, nuevo_dni, nuevo_apellido, nuevo_nombre):
        self.dni_cotitular = nuevo_dni
        self.apellido_cotitular = nuevo_apellido
        self.nombre_cotitular = nuevo_nombre
        self.monto_adeudado *= 1.05  # Se incrementa un 5%

    def ver_datos_deudor(self):
        print(f"Deudor: {self.nombre} {self.apellido} - DNI: {self.dni}")

    def ver_datos_cotitular(self):
        print(f"Cotitular: {self.nombre_cotitular} {self.apellido_cotitular} - DNI: {self.dni_cotitular}")

    def ver_todos_los_datos(self):
        print("----- DATOS COMPLETOS -----")
        self.ver_datos_deudor()
        self.ver_datos_cotitular()
        print(f"Monto adeudado: ${self.monto_adeudado}")
        print(f"Año de la deuda: {self.año_deuda}")
        print("----------------------------")

def ingresar_datos():
    print("Ingrese los datos del deudor:")
    dni = input("DNI: ")
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    dni_cotitular = input("DNI del cotitular: ")
    apellido_cotitular = input("Apellido del cotitular: ")
    nombre_cotitular = input("Nombre del cotitular: ")
    monto_adeudado = float(input("Monto adeudado: "))
    año_deuda = int(input("Año de la deuda: "))
    return Deudor(dni, apellido, nombre, dni_cotitular, apellido_cotitular, nombre_cotitular, monto_adeudado, año_deuda)

def menu(deudor):
    while True:
        print("\n--- Menú ---")
        print("1. Calcular deuda actual")
        print("2. Realizar plan de pago")
        print("3. Cambiar cotitular")
        print("4. Ver datos del deudor")
        print("5. Ver datos del cotitular")
        print("6. Ver todos los datos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            deuda = deudor.calcular_deuda_actual()
            print(f"Deuda actual: ${deuda}")
        elif opcion == "2":
            cuotas = int(input("Ingrese cantidad de cuotas (1 a 12): "))
            valor_cuota = deudor.realizar_plan_de_pago(cuotas)
            if valor_cuota is not None:
                print(f"Cada cuota será de: ${valor_cuota}")
        elif opcion == "3":
            print("Ingrese los datos del nuevo cotitular:")
            nuevo_dni = input("DNI: ")
            nuevo_apellido = input("Apellido: ")
            nuevo_nombre = input("Nombre: ")
            deudor.cambiar_cotitular(nuevo_dni, nuevo_apellido, nuevo_nombre)
            print("Cotitular actualizado. La deuda se incrementó un 5%.")
        elif opcion == "4":
            deudor.ver_datos_deudor()
        elif opcion == "5":
            deudor.ver_datos_cotitular()
        elif opcion == "6":
            deudor.ver_todos_los_datos()
        elif opcion == "7":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")

# Ejecución principal
deudor = ingresar_datos()
menu(deudor)

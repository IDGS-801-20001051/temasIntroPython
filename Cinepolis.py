from io import open

class Cinepolis:
    def __init__(self):
        self.nombreComprador = ""
        self.totalBoletos = 0
        self.totalPagar = 0
        self.precioBoleto = 12.00

    def ingresarDatos(self):
        self.nombreComprador = input("Escribe el nombre del comprador: ")
        numeroPersonas = int(input("¿Cuántas personas irán a la función?: "))
        self.totalBoletos = int(input("¿Cuántos boletos deseas comprar?: "))

        while self.totalBoletos > 7 * numeroPersonas:
            print("\nNo es posible adquirir más de 7 boletos por persona.")
            print("1. Cambiar número de personas")
            print("2. Cambiar número de boletos")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                numeroPersonas = int(input("Introduce el nuevo número de personas: "))
            elif opcion == "2":
                self.totalBoletos = int(input("Introduce la nueva cantidad de boletos: "))
            else:
                print("Opción inválida. Inténtalo de nuevo.")

        print("\nSelecciona el método de pago:")
        print("1. Tarjeta CINECO")
        print("2. Efectivo")
        
        while True:
            opcionPago = input("Elige una opción: ")
            if opcionPago == "1":
                descuentoCineco = True
                break
            elif opcionPago == "2":
                descuentoCineco = False
                break
            else:
                print("Opción inválida. Inténtalo nuevamente.")
        
        self.totalPagar = self.calcularTotal(self.totalBoletos, self.precioBoleto, descuentoCineco)

    def obtenerDescuento(self, cantidadBoletos):
        if cantidadBoletos >= 6:
            return 0.15
        elif 5 >= cantidadBoletos >= 3:
            return 0.10
        else:
            return 0.0

    def calcularTotal(self, cantidadBoletos, precioBoleto, descuentoCineco=False):
        subtotal = cantidadBoletos * precioBoleto
        descuento = self.obtenerDescuento(cantidadBoletos)
        total = subtotal * (1 - descuento)

        if descuentoCineco:
            total *= 0.90

        return total

    def guardarVenta(self):
        with open("ventas.txt", "a") as archivo:
            archivo.write(f"{self.nombreComprador} tuvo una compra de {self.totalPagar:.2f}\n")

    def mostrarCompras():
        try:
            with open("ventas.txt", "r") as archivo:
                lineas = archivo.readlines()
        except FileNotFoundError:
            print("No hay ventas registradas.")
            return

        totalVentas = 0
        print("\n--- Resumen de Ventas ---")
        print("+-----------------+------------+")
        print("| Comprador       | Total      |")
        print("+-----------------+------------+")
        for linea in lineas:
            partes = linea.strip().split(" ")
            nombre = " ".join(partes[:-5])
            total = partes[-1]
            print(f"| {nombre:<15} | ${float(total):<10.2f} |")
            print("+-----------------+------------+")
            totalVentas += float(total)
        print(f"| {'Total Ventas':<15} | ${totalVentas:<10.2f} |")
        print("+-----------------+------------+")

        with open("ventas.txt", "w") as archivo:
            archivo.write("")

    def mostrarResumen(self):
        print(f"\nResumen de la compra:")
        print(f"{self.nombreComprador} adquirió {self.totalBoletos} boletos por un monto total de ${self.totalPagar:.2f}")

def main():
    while True:
        print("\nCINEPOLIS...")
        print("1. Comprar")
        print("2. Terminar")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            compra = Cinepolis()
            compra.ingresarDatos()
            compra.guardarVenta()
            compra.mostrarResumen()

        elif opcion == "2":
            Cinepolis.mostrarCompras()
            print("\nGracias por su compra.")
            break

        else:
            print("Opción inválida. Inténtalo nuevamente.")


if __name__ == "__main__":
    main()

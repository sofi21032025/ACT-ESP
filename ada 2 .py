class Cola:
    def __init__(self, nombre_servicio):
        self.nombre = nombre_servicio
        self.elementos = []
        self.contador = 0  

    def llegar_cliente(self):
        self.contador += 1
        numero_atencion = f"{self.nombre}-{self.contador}"
        self.elementos.append(numero_atencion)
        print(f"Cliente agregado a {self.nombre}: número {numero_atencion}")

    def atender_cliente(self):
        if not self.elementos:
            print(f"No hay clientes en la cola de {self.nombre}.")
        else:
            numero = self.elementos.pop(0)
            print(f"Atendiendo al cliente número {numero}")


def main():
    colas = {
        1: Cola("Seguros de Vida"),
        2: Cola("Seguros de Auto"),
        3: Cola("Seguros Médicos")
    }

    print("=== SISTEMA DE COLAS - COMPAÑÍA DE SEGUROS ===")
    print("Comandos disponibles:")
    print("  C <número_servicio>  → Llegada de cliente (ej: C 1)")
    print("  A <número_servicio>  → Atender cliente (ej: A 2)")
    print("  S                   → Salir del sistema\n")

    while True:
        comando = input("Ingrese comando: ").strip().upper()

        if comando == "S":
            print("Saliendo del sistema...")
            break

        partes = comando.split()

        if len(partes) != 2:
            print("Comando inválido. Ejemplo: C 1 o A 2")
            continue

        letra, num = partes
        if not num.isdigit() or int(num) not in colas:
            print("Número de servicio inválido.")
            continue

        servicio = colas[int(num)]

        if letra == "C":
            servicio.llegar_cliente()
        elif letra == "A":
            servicio.atender_cliente()
        else:
            print("Comando no reconocido. Use C, A o S.")

if __name__ == "__main__":
    main()

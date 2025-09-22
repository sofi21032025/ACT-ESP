class Ventas:
    def __init__(self):
        self.meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        self.departamentos = ["Ropa", "Deportes", "Juguetería"]
        self.ventas = [[0 for _ in range(3)] for _ in range(12)]

    # 1) Insertar una venta
    def insertar_venta(self, mes, depto, monto):
        i_mes = self.meses.index(mes)
        i_depto = self.departamentos.index(depto)
        self.ventas[i_mes][i_depto] = monto

    # 2) Buscar una venta
    def buscar_venta(self, mes, depto):
        i_mes = self.meses.index(mes)
        i_depto = self.departamentos.index(depto)
        return self.ventas[i_mes][i_depto]

    # 3) Eliminar una venta
    def eliminar_venta(self, mes, depto):
        i_mes = self.meses.index(mes)
        i_depto = self.departamentos.index(depto)
        self.ventas[i_mes][i_depto] = 0

    # 4) Imprimir tabla
    def imprimir_tabla(self):
        print(f"{'Mes':<12}{'Ropa':<12}{'Deportes':<12}{'Juguetería':<12}")
        for i, mes in enumerate(self.meses):
            print(f"{mes:<12}{self.ventas[i][0]:<12}{self.ventas[i][1]:<12}{self.ventas[i][2]:<12}")


# Ejemplo de uso
v = Ventas()
v.insertar_venta("Enero", "Ropa", 1500)
v.insertar_venta("Enero", "Deportes", 2000)
v.insertar_venta("Febrero", "Juguetería", 3500)
v.insertar_venta("Diciembre", "Ropa", 5000)

print("\nTABLA DE VENTAS:")
v.imprimir_tabla()

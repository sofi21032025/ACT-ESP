# ══════════════════════════════════════════════════════════════════
# ██████╗ ███╗   ███╗███████╗███╗   ██╗   ███████╗ █████╗    ██████╗██╗   ██╗
# ██╔════╝████╗ ████║██╔════╝████╗  ██║   ██╔════╝██╔══██╗  ██╔════╝██║   ██║
# ██║     ██╔████╔██║███████╗██╔██╗ ██║   ███████╗███████║  ██║     ██║   ██║
# ██║     ██║╚██╔╝██║╚════██║██║╚██╗██║   ╚════██║██╔══██║  ██║     ╚██╗ ██╔╝
# ╚██████╗██║ ╚═╝ ██║███████║██║ ╚████║██╗███████║██║  ██║██╗╚██████╗ ╚████╔╝ 
#  ╚═════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝  ╚═══╝  
# ══════════════════════════════════════════════════════════════════
# 🏢 SISTEMA DE CONTROL DE INVENTARIO EMPRESARIAL
# ══════════════════════════════════════════════════════════════════
# 👤 Desarrollador: Johansen Uriel Samos Godoy
# 📅 Fecha: 06-03-2025
# 🏷️  Versión: 2.0 Professional Edition
# ══════════════════════════════════════════════════════════════════

import os
import sys
from datetime import datetime

class Colors:
    """Clase para manejar colores en la consola"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    # Colores de texto
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Colores de fondo
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_header():
    """Muestra el encabezado principal del sistema"""
    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║                    🏢 MSN.SA.CV - INVENTARIO PRO                 ║")
    print("║                                                                  ║")
    print("║              📦 SISTEMA DE CONTROL DE INVENTARIO                 ║")
    print("║                        Version 2.0                              ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print(f"{Colors.RESET}")
    
def mostrar_separador():
    """Muestra un separador visual"""
    print(f"{Colors.BLUE}{'═' * 70}{Colors.RESET}")

def mostrar_subseparador():
    """Muestra un subseparador visual"""
    print(f"{Colors.CYAN}{'─' * 70}{Colors.RESET}")

def mostrar_timestamp():
    """Muestra la fecha y hora actual"""
    ahora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    print(f"{Colors.MAGENTA}📅 Fecha y hora: {ahora}{Colors.RESET}")

def input_styled(mensaje, color=Colors.YELLOW):
    """Input con estilo personalizado"""
    return input(f"{color}➤ {mensaje}: {Colors.RESET}")

def print_success(mensaje):
    """Mensaje de éxito"""
    print(f"{Colors.GREEN}✅ {mensaje}{Colors.RESET}")

def print_error(mensaje):
    """Mensaje de error"""
    print(f"{Colors.RED}❌ {mensaje}{Colors.RESET}")

def print_info(mensaje):
    """Mensaje informativo"""
    print(f"{Colors.BLUE}ℹ️  {mensaje}{Colors.RESET}")

def print_warning(mensaje):
    """Mensaje de advertencia"""
    print(f"{Colors.YELLOW}⚠️  {mensaje}{Colors.RESET}")

class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __str__(self):
        return f"📦 {self.nombre:<20} │ Cantidad: {self.cantidad:<6} │ Precio: ${self.precio:<8.2f}"

class Inventario:
    def __init__(self):
        self.articulos = []
    
    def agregar_articulo(self, articulo):
        self.articulos.append(articulo)
        print_success(f"Artículo '{articulo.nombre}' agregado exitosamente al inventario")
    
    def mostrar_inventario(self):
        if self.articulos:
            print(f"\n{Colors.CYAN}{Colors.BOLD}📋 INVENTARIO ACTUAL{Colors.RESET}")
            mostrar_separador()
            print(f"{Colors.BLUE}{Colors.BOLD}{'PRODUCTO':<20} │ {'CANTIDAD':<10} │ {'PRECIO':<10} │ {'VALOR TOTAL':<12}{Colors.RESET}")
            mostrar_subseparador()
            
            total_general = 0
            for i, articulo in enumerate(self.articulos, 1):
                valor_total = articulo.precio * articulo.cantidad
                total_general += valor_total
                
                # Alternar colores para mejor legibilidad
                color = Colors.WHITE if i % 2 == 0 else Colors.CYAN
                print(f"{color}{articulo.nombre:<20} │ {articulo.cantidad:<10} │ ${articulo.precio:<9.2f} │ ${valor_total:<11.2f}{Colors.RESET}")
            
            mostrar_subseparador()
            print(f"{Colors.GREEN}{Colors.BOLD}💰 VALOR TOTAL DEL INVENTARIO: ${total_general:.2f}{Colors.RESET}")
            mostrar_separador()
        else:
            print_warning("El inventario está vacío")
    
    def ventas(self, nombre, cantidad):
        for articulo in self.articulos:
            if articulo.nombre.casefold() == nombre.casefold():
                if articulo.cantidad >= cantidad:
                    articulo.cantidad -= cantidad
                    total_venta = articulo.precio * cantidad
                    
                    print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 VENTA REALIZADA EXITOSAMENTE{Colors.RESET}")
                    mostrar_subseparador()
                    print(f"{Colors.CYAN}📦 Producto: {articulo.nombre}{Colors.RESET}")
                    print(f"{Colors.CYAN}🔢 Cantidad vendida: {cantidad} unidades{Colors.RESET}")
                    print(f"{Colors.CYAN}💵 Precio unitario: ${articulo.precio:.2f}{Colors.RESET}")
                    print(f"{Colors.GREEN}{Colors.BOLD}💰 TOTAL DE LA VENTA: ${total_venta:.2f}{Colors.RESET}")
                    print(f"{Colors.BLUE}📊 Cantidad restante: {articulo.cantidad} unidades{Colors.RESET}")
                    mostrar_subseparador()
                else:
                    print_error(f"Stock insuficiente. Solo hay {articulo.cantidad} unidades disponibles")
                return
        
        print_error(f"Producto '{nombre}' no encontrado en el inventario")
    
    def valor_total(self):
        if self.articulos:
            total = sum(a.precio * a.cantidad for a in self.articulos)
            
            print(f"\n{Colors.MAGENTA}{Colors.BOLD}💎 RESUMEN FINANCIERO{Colors.RESET}")
            mostrar_separador()
            print(f"{Colors.CYAN}📊 Total de productos: {len(self.articulos)}{Colors.RESET}")
            print(f"{Colors.CYAN}📦 Total de unidades: {sum(a.cantidad for a in self.articulos)}{Colors.RESET}")
            print(f"{Colors.GREEN}{Colors.BOLD}💰 VALOR TOTAL DEL INVENTARIO: ${total:.2f}{Colors.RESET}")
            mostrar_separador()
        else:
            print_warning("No hay productos en el inventario para calcular")

def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print(f"\n{Colors.YELLOW}{Colors.BOLD}🎛️  MENÚ PRINCIPAL{Colors.RESET}")
    mostrar_separador()
    
    opciones = [
        ("1", "📋 Ver inventario completo", Colors.CYAN),
        ("2", "➕ Agregar nuevo artículo", Colors.GREEN),
        ("3", "🛒 Realizar venta", Colors.YELLOW),
        ("4", "💰 Valor total del inventario", Colors.MAGENTA),
        ("5", "❌ Salir del sistema", Colors.RED)
    ]
    
    for numero, descripcion, color in opciones:
        print(f"{color}[{numero}] {descripcion}{Colors.RESET}")
    
    mostrar_separador()

def mostrar_bienvenida():
    """Muestra mensaje de bienvenida"""
    limpiar_pantalla()
    mostrar_header()
    mostrar_timestamp()
    print(f"\n{Colors.GREEN}🎉 ¡Bienvenido al Sistema de Control de Inventario!{Colors.RESET}")
    print(f"{Colors.BLUE}Administre su inventario de manera profesional y eficiente{Colors.RESET}")

def inicializar_productos_demo(inventario):
    """Inicializa productos de demostración"""
    productos = [
        ("Llave Trupper", 10, 98.00),
        ("Teflón Industrial", 25, 15.00),
        ("Broca para Metal", 35, 25.00),
        ("Cinta Aislante", 17, 15.00),
        ("Hilo de Algodón", 50, 4.00),
        ("Foco LED", 110, 70.00)
    ]
    
    print(f"\n{Colors.BLUE}🔄 Inicializando inventario con productos de demostración...{Colors.RESET}")
    
    for nombre, cantidad, precio in productos:
        inventario.agregar_articulo(Articulo(nombre, cantidad, precio))
    
    print_success("Productos de demostración cargados correctamente")

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input(f"\n{Colors.YELLOW}📌 Presione Enter para continuar...{Colors.RESET}")

def confirmar_salida():
    """Confirma si el usuario desea salir"""
    while True:
        respuesta = input_styled("¿Está seguro que desea salir del sistema? (s/n)", Colors.RED).lower()
        if respuesta in ['s', 'si', 'sí', 'yes', 'y']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print_error("Respuesta no válida. Ingrese 's' para sí o 'n' para no")

def main():
    """Función principal del programa"""
    inventario = Inventario()
    
    # Mostrar bienvenida
    mostrar_bienvenida()
    
    # Inicializar productos de demostración
    inicializar_productos_demo(inventario)
    
    pausar()
    
    while True:
        try:
            limpiar_pantalla()
            mostrar_header()
            mostrar_menu()
            
            opcion = input_styled("Seleccione una opción", Colors.WHITE)
            
            if opcion == "1":
                limpiar_pantalla()
                mostrar_header()
                inventario.mostrar_inventario()
                pausar()
                
            elif opcion == "2":
                limpiar_pantalla()
                mostrar_header()
                print(f"\n{Colors.GREEN}{Colors.BOLD}➕ AGREGAR NUEVO ARTÍCULO{Colors.RESET}")
                mostrar_separador()
                
                try:
                    nombre = input_styled("Nombre del producto")
                    if not nombre.strip():
                        print_error("El nombre del producto no puede estar vacío")
                        pausar()
                        continue
                        
                    cantidad = int(input_styled("Cantidad"))
                    if cantidad < 0:
                        print_error("La cantidad no puede ser negativa")
                        pausar()
                        continue
                        
                    precio = float(input_styled("Precio unitario"))
                    if precio < 0:
                        print_error("El precio no puede ser negativo")
                        pausar()
                        continue
                    
                    inventario.agregar_articulo(Articulo(nombre, cantidad, precio))
                    
                except ValueError:
                    print_error("Error: Ingrese valores numéricos válidos para cantidad y precio")
                
                pausar()
                
            elif opcion == "3":
                limpiar_pantalla()
                mostrar_header()
                print(f"\n{Colors.YELLOW}{Colors.BOLD}🛒 REALIZAR VENTA{Colors.RESET}")
                mostrar_separador()
                
                if not inventario.articulos:
                    print_warning("No hay productos en el inventario para vender")
                    pausar()
                    continue
                
                try:
                    nombre = input_styled("Nombre del producto a vender")
                    cantidad = int(input_styled("Cantidad a vender"))
                    
                    if cantidad <= 0:
                        print_error("La cantidad debe ser mayor a 0")
                        pausar()
                        continue
                    
                    inventario.ventas(nombre, cantidad)
                    
                except ValueError:
                    print_error("Error: Ingrese un valor numérico válido para la cantidad")
                
                pausar()
                
            elif opcion == "4":
                limpiar_pantalla()
                mostrar_header()
                inventario.valor_total()
                pausar()
                
            elif opcion == "5":
                if confirmar_salida():
                    limpiar_pantalla()
                    print(f"{Colors.CYAN}{Colors.BOLD}")
                    print("╔══════════════════════════════════════════════════════════════════╗")
                    print("║                                                                  ║")
                    print("║                    👋 HASTA PRONTO                               ║")
                    print("║                                                                  ║")
                    print("║          Gracias por usar MSN.SA.CV - Inventario Pro            ║")
                    print("║                                                                  ║")
                    print("║                 Desarrollado por: Johansen Uriel                ║")
                    print("║                                                                  ║")
                    print("╚══════════════════════════════════════════════════════════════════╝")
                    print(f"{Colors.RESET}")
                    
                    mostrar_timestamp()
                    print(f"\n{Colors.GREEN}✨ Sistema cerrado correctamente{Colors.RESET}")
                    sys.exit(0)
            else:
                print_error("Opción no válida. Seleccione una opción del 1 al 5")
                pausar()
                
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}Interrupción detectada. Cerrando sistema...{Colors.RESET}")
            sys.exit(0)
        except Exception as e:
            print_error(f"Error inesperado: {str(e)}")
            pausar()

if __name__ == "__main__":
    main()
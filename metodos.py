def busqueda_secuencial(lista, dato):
    """Busca 'dato' recorriendo la lista uno por uno."""
    for i in range(len(lista)):
        if lista[i] == dato:
            return i
    return -1


def busqueda_binaria(lista, dato):
    """Busca 'dato' en una lista ORDENADA usando búsqueda binaria."""
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == dato:
            return medio
        elif dato < lista[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1


def buscar_usuario_hash(usuarios, username):
    """Busca 'username' en un diccionario (tabla hash)."""
    return usuarios.get(username, None)

def ejercicio_inventario_secuencial():
    productos = [
        (101, "Arroz"),
        (102, "Frijol"),
        (103, "Azúcar"),
        (104, "Aceite"),
        (105, "Galletas"),
        (106, "Jabón"),
        (107, "Detergente")
    ]

    print("\n=== EJERCICIO 1: INVENTARIO DE TIENDA ===")
    print("Método de búsqueda: SECUENCIAL\n")
    print("Lista de productos:")
    for codigo, nombre in productos:
        print(f"Código: {codigo}  ->  Producto: {nombre}")

    try:
        codigo_buscar = int(input("\nIngresa el CÓDIGO del producto a buscar: "))
    except ValueError:
        print("Error: debes ingresar un número entero.")
        return

    lista_codigos = [codigo for codigo, _ in productos]
    pos = busqueda_secuencial(lista_codigos, codigo_buscar)

    if pos != -1:
        print(f"\nProducto encontrado: {productos[pos][1]} (posición {pos})")
    else:
        print("\nEl producto NO se encuentra en el inventario.")

def ejercicio_matriculas_binaria():
    matriculas = [12001, 12005, 12008, 12010,
                  12015, 12020, 12025, 12030]

    print("\n=== EJERCICIO 2: MATRÍCULAS DE ALUMNOS ===")
    print("Método de búsqueda: BINARIA\n")
    print("Matrículas registradas (ORDENADAS):")
    print(matriculas)

    try:
        mat_buscar = int(input("\nIngresa la MATRÍCULA a buscar: "))
    except ValueError:
        print("Error: debes ingresar un número entero.")
        return

    pos = busqueda_binaria(matriculas, mat_buscar)

    if pos != -1:
        print(f"\nMatrícula {mat_buscar} encontrada en la posición {pos}.")
    else:
        print(f"\nLa matrícula {mat_buscar} NO está registrada.")


def ejercicio_usuarios_hash():
    usuarios = {
        "emilia01": "emilia01@correo.com",
        "leo_prog": "leo_prog@correo.com",
        "valen_dev": "valen_dev@correo.com",
        "admin": "admin@sistema.com"
    }

    print("\n=== EJERCICIO 3: SISTEMA DE USUARIOS ===")
    print("Método de búsqueda: HASH (diccionario)\n")
    print("Usuarios registrados (username -> correo):")
    for user, correo in usuarios.items():
        print(f"{user:10s} -> {correo}")

    username = input("\nIngresa el NOMBRE DE USUARIO (username) a buscar: ")

    correo = buscar_usuario_hash(usuarios, username)

    if correo is not None:
        print(f"\nUsuario encontrado. Correo asociado: {correo}")
    else:
        print("\nEl usuario NO está registrado en el sistema.")
        
def menu_principal():
    while True:
        print("\n===================================")
        print("      MENÚ DE MÉTODOS DE BÚSQUEDA  ")
        print("===================================")
        print("1) Inventario de tienda  (Secuencial)")
        print("2) Matrículas de alumnos (Binaria)")
        print("3) Sistema de usuarios   (Hash)")
        print("4) Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ejercicio_inventario_secuencial()
        elif opcion == "2":
            ejercicio_matriculas_binaria()
        elif opcion == "3":
            ejercicio_usuarios_hash()
        elif opcion == "4":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()

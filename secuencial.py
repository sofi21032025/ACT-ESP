def busqueda_secuencial(lista, dato):
    for i in range(len(lista)):
        if lista[i] == dato:
            return i   
    return -1        

productos = [
    (101, "Arroz"),
    (102, "Frijol"),
    (103, "Azúcar"),
    (104, "Aceite"),
    (105, "Galletas"),
    (106, "Jabón"),
    (107, "Detergente")
]

print("INVENTARIO DE LA TIENDA:")
for codigo, nombre in productos:
    print(f"Código: {codigo}  ->  Producto: {nombre}")

codigo_buscar = int(input("\nIngresa el código del producto a buscar: "))

lista_codigos = [codigo for codigo, _ in productos]

pos = busqueda_secuencial(lista_codigos, codigo_buscar)

if pos != -1:
    print(f"\nProducto encontrado: {productos[pos][1]} (posición {pos})")
else:
    print("\nEl producto NO se encuentra en el inventario.")

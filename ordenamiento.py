import random
import time

def imprimir_vector(vector):
    """Devuelve el vector en formato bonito tipo tabla."""
    return " | ".join(f"{x:2d}" for x in vector)


def insercion_sin_mostrar(lista):
    pasos = 0
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        pasos += 1  

        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
            pasos += 1  

        lista[j + 1] = actual
        pasos += 1  

    return lista, pasos


def burbuja_sin_mostrar(lista):
    pasos = 0
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            pasos += 1 
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                pasos += 1  
    return lista, pasos


def seleccion_sin_mostrar(lista):
    pasos = 0
    for i in range(len(lista)):
        minimo = i
        for j in range(i + 1, len(lista)):
            pasos += 1  
            if lista[j] < lista[minimo]:
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]
        pasos += 1 
    return lista, pasos

def insercion_pasos(lista):
    pasos = 0
    print("\n--- PROCESO: Inserción ---")
    print("Vector original:")
    print(imprimir_vector(lista))

    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        print(f"\nTomamos el valor {actual} (posición {i}) y lo comparamos hacia atrás")
        pasos += 1

        while j >= 0 and lista[j] > actual:
            print(f"{lista[j]} > {actual}, movemos {lista[j]} a la derecha")
            lista[j + 1] = lista[j]
            j -= 1
            pasos += 1

        lista[j + 1] = actual
        pasos += 1
        print("Lista después de insertar:", imprimir_vector(lista))

    print("\nVector final ordenado:", imprimir_vector(lista))
    print(f"Pasos totales (aprox.): {pasos}")
    return lista, pasos


def burbuja_pasos(lista):
    pasos = 0
    print("\n--- PROCESO: Burbuja ---")
    print("Vector original:")
    print(imprimir_vector(lista), "\n")

    n = len(lista)

    for i in range(n - 1):
        print(f"Iteración {i + 1}:")
        for j in range(n - i - 1):
            estado = imprimir_vector(lista)
            pasos += 1 

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                pasos += 1 
                mensaje = "Se genera cambio"
            else:
                mensaje = "No hay cambio"

            print(estado, " → ", mensaje)

        print(imprimir_vector(lista), "→ Fin de iteración\n")

    print("Vector final ordenado:")
    print(imprimir_vector(lista))
    print(f"Pasos totales (aprox.): {pasos}")
    return lista, pasos


def seleccion_pasos(lista):
    pasos = 0
    print("\n--- PROCESO: Selección ---")
    print("Vector original:")
    print(imprimir_vector(lista))

    for i in range(len(lista)):
        minimo = i
        print(f"\nBuscamos el mínimo desde la posición {i}:")
        for j in range(i + 1, len(lista)):
            print(f"Comparamos mínimo actual {lista[minimo]} con {lista[j]}")
            pasos += 1 
            if lista[j] < lista[minimo]:
                minimo = j
                print(f"Nuevo mínimo encontrado: {lista[minimo]}")

        print(f"Intercambiamos {lista[i]} con {lista[minimo]}")
        lista[i], lista[minimo] = lista[minimo], lista[i]
        pasos += 1  
        print("Lista después del intercambio:", imprimir_vector(lista))

    print("\nVector final ordenado:")
    print(imprimir_vector(lista))
    print(f"Pasos totales (aprox.): {pasos}")
    return lista, pasos

print("Elige el origen de los números:")
print("1. Los escribe el usuario (se muestra paso a paso)")
print("2. Generar 1000 números al azar (NO muestra proceso)")

while True:
    origen = input("Opción (1 o 2): ")
    if origen in ("1", "2"):
        break
    print("Opción inválida. Solo 1 o 2.")

if origen == "1":
    numeros = input("\nIngresa los números separados por comas: ")
    lista = [int(x.strip()) for x in numeros.split(",")]
    print(f"\nSe capturaron {len(lista)} números.")
else:
    lista = [random.randint(1, 1000) for _ in range(1000)]
    print("\nSe generaron 1000 números aleatorios.")

print("\nMétodos de ordenamiento:")
print("1. Inserción")
print("2. Burbuja")
print("3. Selección")

while True:
    opcion = input("Elige una opción (1, 2 o 3): ")
    if opcion in ("1", "2", "3"):
        break
    print("Opción inválida. Solo 1, 2 o 3.")

lista_a_ordenar = lista.copy()
inicio = time.time()

if origen == "1":
    if opcion == "1":
        resultado, pasos = insercion_pasos(lista_a_ordenar)
    elif opcion == "2":
        resultado, pasos = burbuja_pasos(lista_a_ordenar)
    else:
        resultado, pasos = seleccion_pasos(lista_a_ordenar)
else:
    if opcion == "1":
        resultado, pasos = insercion_sin_mostrar(lista_a_ordenar)
    elif opcion == "2":
        resultado, pasos = burbuja_sin_mostrar(lista_a_ordenar)
    else:
        resultado, pasos = seleccion_sin_mostrar(lista_a_ordenar)

fin = time.time()

print("\n======== RESUMEN FINAL ========")
print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
print(f"Pasos totales (aprox.): {pasos}")

if len(resultado) <= 30:
    print("\nVector ordenado completo:")
    print(resultado)
else:
    print("\nPrimeros 20 elementos ordenados:")
    print(resultado[:20])
    print("Últimos 20 elementos ordenados:")
    print(resultado[-20:])

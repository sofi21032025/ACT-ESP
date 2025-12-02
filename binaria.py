def busqueda_binaria(lista, dato):
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

matriculas = [12001, 12005, 12008, 12010, 12015, 12020, 12025, 12030]

print("MATRÍCULAS REGISTRADAS (ORDENADAS):")
print(matriculas)

mat_buscar = int(input("\nIngresa la matrícula a buscar: "))

pos = busqueda_binaria(matriculas, mat_buscar)

if pos != -1:
    print(f"\nMatrícula {mat_buscar} encontrada en la posición {pos}.")
else:
    print(f"\nLa matrícula {mat_buscar} NO está registrada.")

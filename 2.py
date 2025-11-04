from ada3 import Postre

def eliminar_repetidos(lista_postres):
    nombres_vistos = set()
    lista_limpia = []
    for p in lista_postres:
        if p.nombre.lower() not in nombres_vistos:
            nombres_vistos.add(p.nombre.lower())
            lista_limpia.append(p)
        else:
            print(f"Eliminando duplicado: {p.nombre}")
    return lista_limpia



if __name__ == "__main__":
    p1 = Postre("Pastel")
    p1.ingredientes.agregar("Harina")
    p1.ingredientes.agregar("Leche")

    p2 = Postre("Helado")
    p2.ingredientes.agregar("Leche")

    p3 = Postre("Pastel") 
    p3.ingredientes.agregar("Azúcar")

    lista = [p1, p2, p3]

    print("=== Lista original ===")
    for p in lista:
        print(f"- {p.nombre}: {p.ingredientes.mostrar()}")

    lista = eliminar_repetidos(lista)

    print("\n=== Lista sin duplicados ===")
    for p in lista:
        print(f"- {p.nombre}: {p.ingredientes.mostrar()}")
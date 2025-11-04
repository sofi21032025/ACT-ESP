class Node:
    """Clase que representa un nodo de la lista enlazada."""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    """Implementación de la lista simplemente enlazada."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Verifica si la lista está vacía."""
        return self.head is None

    def insert_beginning(self, data):
        """Inserta un nodo al inicio."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        """Inserta un nodo al final."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, prev_data, data):
        """Inserta un nodo después de un valor específico."""
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if not current:
            print("El elemento no fue encontrado.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        """Elimina un nodo que contenga el valor especificado."""
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if not current:
            print("Elemento no encontrado.")
            return
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        print(f"Nodo con valor {data} eliminado correctamente.")

    def search(self, data):
        """Busca un nodo y devuelve True si existe."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def traverse(self):
        """Devuelve los elementos de la lista como lista de Python."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def size(self):
        """Devuelve el número de elementos en la lista."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


if __name__ == "__main__":
    lista = LinkedList()

    while True:
        print("\n========= MENÚ LINKED LIST =========")
        print("1. Insertar al inicio")
        print("2. Insertar al final")
        print("3. Insertar después de un valor")
        print("4. Eliminar un valor")
        print("5. Buscar un valor")
        print("6. Mostrar la lista")
        print("7. Mostrar tamaño de la lista")
        print("8. Salir")
    

        opcion = input("Elige una opción: ")

        if opcion == "1":
            dato = input("Dato a insertar al inicio: ")
            lista.insert_beginning(dato)
        elif opcion == "2":
            dato = input("Dato a insertar al final: ")
            lista.insert_end(dato)
        elif opcion == "3":
            previo = input("Insertar después de qué valor: ")
            dato = input("Dato a insertar: ")
            lista.insert_after(previo, dato)
        elif opcion == "4":
            dato = input("Dato a eliminar: ")
            lista.delete(dato)
        elif opcion == "5":
            dato = input("Dato a buscar: ")
            encontrado = lista.search(dato)
            print("Encontrado" if encontrado else "No encontrado")
        elif opcion == "6":
            print("Lista actual:", lista.traverse())
        elif opcion == "7":
            print("Tamaño de la lista:", lista.size())
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

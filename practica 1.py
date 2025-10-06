class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.items = [None] * capacidad
        self.tope = 0  

    def esta_vacia(self):
        return self.tope == 0

    def esta_llena(self):
        return self.tope == self.capacidad

    def insertar(self, elemento):
        if self.esta_llena():
            print(f"Error: Desbordamiento al intentar insertar '{elemento}'")
            return
        self.items[self.tope] = elemento
        self.tope += 1
        self.mostrar_estado(f"Insertar({elemento})")

    def eliminar(self):
        if self.esta_vacia():
            print(f"Error: Subdesbordamiento al intentar eliminar")
            return None
        self.tope -= 1
        eliminado = self.items[self.tope]
        self.items[self.tope] = None
        self.mostrar_estado(f"Eliminar({eliminado})")
        return eliminado

    def mostrar_estado(self, operacion):
        print(f"\nOperación: {operacion}")
        print(f"Pila: {self.items}")
        print(f"TOPE: {self.tope}")

pila = Pila(8)

pila.insertar('X')  
pila.insertar('Y')  
pila.eliminar()     
pila.eliminar()     
pila.eliminar()     
pila.insertar('V')  
pila.insertar('W')  
pila.eliminar()     
pila.insertar('R')  

print(f"\nEstado final de la pila: {pila.items}")
print(f"Cantidad de elementos en la pila: {pila.tope}")
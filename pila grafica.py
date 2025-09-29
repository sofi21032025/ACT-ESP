import tkinter as tk
from tkinter import messagebox

class Pilas:
    def __init__(self):
        self.pila = []

    def isEmpty(self):
        return len(self.pila) == 0
    
    def push(self, value):
        self.pila.append(value)

    def pop_pila(self):
        if not self.isEmpty():
            return self.pila.pop()
        else:
            return None
    
    def peek(self):
        if not self.isEmpty():
            return self.pila[-1]
        else:
            return None


def actualizar_pila():
    """Actualiza la vista de la pila en la interfaz"""
    lista.delete(0, tk.END)
    for elem in reversed(pilaUno.pila):
        lista.insert(tk.END, elem)

def apilar():
    valor = entry.get()
    if valor:
        pilaUno.push(valor)
        entry.delete(0, tk.END)
        actualizar_pila()
    else:
        messagebox.showwarning("Advertencia", "Ingrese un valor para apilar")

def desapilar():
    valor = pilaUno.pop_pila()
    if valor is not None:
        messagebox.showinfo("Desapilar", f"Se quitó: {valor}")
        actualizar_pila()
    else:
        messagebox.showerror("Error", "La pila está vacía")

def ver_cima():
    valor = pilaUno.peek()
    if valor is not None:
        messagebox.showinfo("Cima", f"El elemento en la cima es: {valor}")
    else:
        messagebox.showerror("Error", "La pila está vacía")


pilaUno = Pilas()


root = tk.Tk()
root.title("Simulación de Pila")


entry = tk.Entry(root, width=20)
entry.pack(pady=5)

btn_push = tk.Button(root, text="Apilar", command=apilar)
btn_push.pack(pady=2)

btn_pop = tk.Button(root, text="Desapilar", command=desapilar)
btn_pop.pack(pady=2)

btn_peek = tk.Button(root, text="Ver cima", command=ver_cima)
btn_peek.pack(pady=2)


lista = tk.Listbox(root, height=10, width=30)
lista.pack(pady=10)

root.mainloop()
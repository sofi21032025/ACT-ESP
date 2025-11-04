import tkinter as tk
from tkinter import messagebox



class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class ListaIngredientes:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre):
        nuevo = NodoIngrediente(nombre)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar(self, nombre):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.nombre.lower() == nombre.lower():
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def mostrar(self):
        ingredientes = []
        actual = self.cabeza
        while actual:
            ingredientes.append(actual.nombre)
            actual = actual.siguiente
        return ingredientes


class Postre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = ListaIngredientes()




class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Postres")
        self.root.geometry("680x450")
        self.root.config(bg="#fef9f3")


        self.postres = []


        tk.Label(root, text="Gestor de Postres y sus Ingredientes",
                 font=("Arial", 16, "bold"), bg="#fef9f3", fg="#7a4b24").pack(pady=10)


        marco = tk.Frame(root, bg="#fff5eb", bd=2, relief="groove")
        marco.pack(padx=20, pady=10, fill="both", expand=True)


        tk.Label(marco, text="Nombre del Postre:", bg="#fff5eb").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_postre = tk.Entry(marco, width=25)
        self.entry_postre.grid(row=0, column=1, pady=5)

        tk.Label(marco, text="Ingrediente:", bg="#fff5eb").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_ingrediente = tk.Entry(marco, width=25)
        self.entry_ingrediente.grid(row=1, column=1, pady=5)


        boton_frame = tk.Frame(marco, bg="#fff5eb")
        boton_frame.grid(row=2, column=0, columnspan=2, pady=10)

        tk.Button(boton_frame, text="Alta Postre", command=self.alta_postre, bg="#a8e6cf").grid(row=0, column=0, padx=5)
        tk.Button(boton_frame, text="Baja Postre", command=self.baja_postre, bg="#ffaaa5").grid(row=0, column=1, padx=5)
        tk.Button(boton_frame, text="Agregar Ingrediente", command=self.agregar_ingrediente, bg="#ffd3b6").grid(row=0, column=2, padx=5)
        tk.Button(boton_frame, text="Eliminar Ingrediente", command=self.eliminar_ingrediente, bg="#dcedc1").grid(row=0, column=3, padx=5)
        tk.Button(boton_frame, text="Mostrar Ingredientes", command=self.mostrar_ingredientes, bg="#c4fcef").grid(row=0, column=4, padx=5)


        tk.Label(marco, text="Lista de Postres (A-Z):", bg="#fff5eb", font=("Arial", 10, "bold")).grid(row=3, column=0, columnspan=2)
        self.lista_postres = tk.Listbox(marco, width=55, height=10)
        self.lista_postres.grid(row=4, column=0, columnspan=2, pady=5)

        tk.Label(root, text="Hecho con en Python y Tkinter", bg="#fef9f3", fg="#7a4b24", font=("Arial", 9, "italic")).pack(pady=5)



    def buscar_postre(self, nombre):
        for p in self.postres:
            if p.nombre.lower() == nombre.lower():
                return p
        return None

    def actualizar_lista(self):
        self.postres.sort(key=lambda x: x.nombre.lower())
        self.lista_postres.delete(0, tk.END)
        for p in self.postres:
            self.lista_postres.insert(tk.END, p.nombre)

    def alta_postre(self):
        nombre = self.entry_postre.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "Ingrese el nombre del postre.")
            return
        if self.buscar_postre(nombre):
            messagebox.showwarning("Error", "Ese postre ya existe.")
            return

        nuevo = Postre(nombre)
        ingr = self.entry_ingrediente.get().strip()
        if ingr:
            nuevo.ingredientes.agregar(ingr)
        self.postres.append(nuevo)
        self.actualizar_lista()
        messagebox.showinfo("Éxito", f"Postre '{nombre}' agregado correctamente.")

    def baja_postre(self):
        nombre = self.entry_postre.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "Ingrese el nombre del postre.")
            return
        postre = self.buscar_postre(nombre)
        if not postre:
            messagebox.showwarning("Error", "El postre no existe.")
            return
        self.postres.remove(postre)
        self.actualizar_lista()
        messagebox.showinfo("Éxito", f"Postre '{nombre}' eliminado correctamente.")

    def agregar_ingrediente(self):
        nombre_p = self.entry_postre.get().strip()
        ingr = self.entry_ingrediente.get().strip()
        if not nombre_p or not ingr:
            messagebox.showwarning("Error", "Ingrese el nombre del postre y del ingrediente.")
            return
        postre = self.buscar_postre(nombre_p)
        if not postre:
            messagebox.showwarning("Error", "El postre no existe.")
            return
        postre.ingredientes.agregar(ingr)
        messagebox.showinfo("Éxito", f"Ingrediente '{ingr}' agregado a '{nombre_p}'.")

    def eliminar_ingrediente(self):
        nombre_p = self.entry_postre.get().strip()
        ingr = self.entry_ingrediente.get().strip()
        if not nombre_p or not ingr:
            messagebox.showwarning("Error", "Ingrese el nombre del postre y del ingrediente.")
            return
        postre = self.buscar_postre(nombre_p)
        if not postre:
            messagebox.showwarning("Error", "El postre no existe.")
            return
        if postre.ingredientes.eliminar(ingr):
            messagebox.showinfo("Éxito", f"Ingrediente '{ingr}' eliminado de '{nombre_p}'.")
        else:
            messagebox.showwarning("Error", f"Ingrediente '{ingr}' no encontrado en '{nombre_p}'.")

    def mostrar_ingredientes(self):
        nombre = self.entry_postre.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "Ingrese el nombre del postre.")
            return
        postre = self.buscar_postre(nombre)
        if not postre:
            messagebox.showwarning("Error", "El postre no existe.")
            return
        ingredientes = postre.ingredientes.mostrar()
        if not ingredientes:
            messagebox.showinfo("Ingredientes", f"El postre '{nombre}' no tiene ingredientes.")
        else:
            lista = "\n- ".join(ingredientes)
            messagebox.showinfo("Ingredientes", f"Ingredientes de '{nombre}':\n- {lista}")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
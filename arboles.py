import tkinter as tk
from tkinter import Canvas, messagebox

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def esVacio(self):
        return self.raiz is None

    def insertar(self, dato):
        def _insertar(nodo, dato):
            if nodo is None:
                return Nodo(dato)
            if dato < nodo.dato:
                nodo.izq = _insertar(nodo.izq, dato)
            elif dato > nodo.dato:
                nodo.der = _insertar(nodo.der, dato)
            return nodo
        self.raiz = _insertar(self.raiz, dato)

    def buscar(self, dato):
        def _buscar(nodo, dato):
            if nodo is None:
                return False
            if nodo.dato == dato:
                return True
            elif dato < nodo.dato:
                return _buscar(nodo.izq, dato)
            else:
                return _buscar(nodo.der, dato)
        return _buscar(self.raiz, dato)

    # Recorridos que devuelven listas
    def preOrden(self):
        res = []
        def _pre(n):
            if n:
                res.append(n.dato)
                _pre(n.izq)
                _pre(n.der)
        _pre(self.raiz)
        return res

    def inOrden(self):
        res = []
        def _in(n):
            if n:
                _in(n.izq)
                res.append(n.dato)
                _in(n.der)
        _in(self.raiz)
        return res

    def postOrden(self):
        res = []
        def _post(n):
            if n:
                _post(n.izq)
                _post(n.der)
                res.append(n.dato)
        _post(self.raiz)
        return res

    def _maximo(self, nodo):
        while nodo.der:
            nodo = nodo.der
        return nodo

    def _minimo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    def eliminar_predecesor(self, dato):
        def _eliminar(nodo, dato):
            if nodo is None:
                return nodo
            if dato < nodo.dato:
                nodo.izq = _eliminar(nodo.izq, dato)
            elif dato > nodo.dato:
                nodo.der = _eliminar(nodo.der, dato)
            else:
                if nodo.izq is None:
                    return nodo.der
                elif nodo.der is None:
                    return nodo.izq
                temp = self._maximo(nodo.izq)
                nodo.dato = temp.dato
                nodo.izq = _eliminar(nodo.izq, temp.dato)
            return nodo
        self.raiz = _eliminar(self.raiz, dato)

    def eliminar_sucesor(self, dato):
        def _eliminar(nodo, dato):
            if nodo is None:
                return nodo
            if dato < nodo.dato:
                nodo.izq = _eliminar(nodo.izq, dato)
            elif dato > nodo.dato:
                nodo.der = _eliminar(nodo.der, dato)
            else:
                if nodo.izq is None:
                    return nodo.der
                elif nodo.der is None:
                    return nodo.izq
                temp = self._minimo(nodo.der)
                nodo.dato = temp.dato
                nodo.der = _eliminar(nodo.der, temp.dato)
            return nodo
        self.raiz = _eliminar(self.raiz, dato)

    def recorrido_por_niveles(self):
        if self.raiz is None:
            return []
        q = [self.raiz]
        res = []
        while q:
            node = q.pop(0)
            res.append(node.dato)
            if node.izq: q.append(node.izq)
            if node.der: q.append(node.der)
        return res

    def altura(self):
        if self.raiz is None:
            return 0
        q = [(self.raiz, 1)]
        max_h = 0
        while q:
            node, lvl = q.pop(0)
            if lvl > max_h: max_h = lvl
            if node.izq: q.append((node.izq, lvl+1))
            if node.der: q.append((node.der, lvl+1))
        return max_h

    def contar_hojas(self):
        def _contar(n):
            if n is None:
                return 0
            if n.izq is None and n.der is None:
                return 1
            return _contar(n.izq) + _contar(n.der)
        return _contar(self.raiz)

    def contar_nodos(self):
        def _contar(n):
            if n is None:
                return 0
            return 1 + _contar(n.izq) + _contar(n.der)
        return _contar(self.raiz)

    def es_completo(self):
        if self.raiz is None:
            return True
        q = [self.raiz]
        found_none = False
        while q:
            n = q.pop(0)
            if n.izq:
                if found_none: return False
                q.append(n.izq)
            else:
                found_none = True
            if n.der:
                if found_none: return False
                q.append(n.der)
            else:
                found_none = True
        return True

    def es_lleno(self):
        def _lleno(n):
            if n is None:
                return True
            if (n.izq is None) ^ (n.der is None):
                return False
            return _lleno(n.izq) and _lleno(n.der)
        return _lleno(self.raiz)

    def eliminar_arbol(self):
        self.raiz = None

    def grados_por_nodo(self):
        res = []
        def _rec(n):
            if n:
                grado = (1 if n.izq else 0) + (1 if n.der else 0)
                res.append((n.dato, grado))
                _rec(n.izq)
                _rec(n.der)
        _rec(self.raiz)
        return res

class ArbolGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Árbol Binario (GUI)")
        self.pack(fill="both", expand=True)
        self.arbol = ArbolBinario()

        # Layout
        left = tk.Frame(self)
        left.pack(side="left", fill="y", padx=6, pady=6)
        center = tk.Frame(self)
        center.pack(side="left", fill="both", expand=True, padx=6, pady=6)
        right = tk.Frame(self, width=280)
        right.pack(side="right", fill="y", padx=6, pady=6)

        # Entrada y botones
        tk.Label(left, text="Número:").pack(anchor="w")
        self.entry = tk.Entry(left, width=18)
        self.entry.pack(pady=4)
        self.entry.focus()

        botones = [
            ("Insertar", self.insertar),
            ("Buscar", self.buscar),
            ("Eliminar (Predecesor)", self.eliminar_predecesor),
            ("Eliminar (Sucesor)", self.eliminar_sucesor),
            ("Mostrar Árbol", self.mostrar_arbol),
            ("Limpiar Árbol", self.limpiar_arbol),
            ("InOrden", self.mostrar_inorden),
            ("PreOrden", self.mostrar_preorden),
            ("PostOrden", self.mostrar_postorden),
            ("Por Niveles", self.mostrar_niveles),
            ("Altura", self.mostrar_altura),
            ("Hojas", self.mostrar_hojas),
            ("Nodos", self.mostrar_nodos),
            ("¿Completo?", self.verificar_completo),
            ("¿Lleno?", self.verificar_lleno),
            ("Grados", self.mostrar_grados),
        ]
        for (txt, cmd) in botones:
            tk.Button(left, text=txt, width=20, command=cmd).pack(pady=2)

        # Canvas
        self.canvas = Canvas(center, bg="white", width=820, height=620)
        self.canvas.pack(fill="both", expand=True)

        # Panel de resultados
        tk.Label(right, text="Resultados:").pack(anchor="w")
        self.result_list = tk.Listbox(right, width=44, height=32)
        self.result_list.pack(side="left", fill="y")
        sb = tk.Scrollbar(right, command=self.result_list.yview)
        sb.pack(side="right", fill="y")
        self.result_list.config(yscrollcommand=sb.set)
        self.status = tk.Label(self, text="Listo.", anchor="w")
        self.status.pack(side="bottom", fill="x")

    # Métodos funcionales (sin cambios)
    def _push_result(self, titulo, contenido):
        self.result_list.insert(tk.END, f"{titulo}: {contenido}")
        self.result_list.yview_moveto(1.0)
        self.status.config(text=f"{titulo} mostrado.")

    def _clear_results(self):
        self.result_list.delete(0, tk.END)
        self.status.config(text="Resultados limpiados.")

    def insertar(self):
        txt = self.entry.get().strip()
        if not txt:
            messagebox.showwarning("Aviso", "Ingrese un número.")
            return
        try:
            num = int(txt)
            self.arbol.insertar(num)
            self.entry.delete(0, tk.END)
            self.status.config(text=f"Insertado {num}.")
            self.mostrar_arbol()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número entero válido.")

    def buscar(self):
        txt = self.entry.get().strip()
        if not txt:
            return
        try:
            num = int(txt)
            ok = self.arbol.buscar(num)
            self._push_result("Buscar", f"{num} -> {'Encontrado' if ok else 'No encontrado'}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def eliminar_predecesor(self):
        txt = self.entry.get().strip()
        if not txt:
            return
        try:
            num = int(txt)
            self.arbol.eliminar_predecesor(num)
            self._push_result("Eliminar (Pre)", f"{num}")
            self.mostrar_arbol()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def eliminar_sucesor(self):
        txt = self.entry.get().strip()
        if not txt:
            return
        try:
            num = int(txt)
            self.arbol.eliminar_sucesor(num)
            self._push_result("Eliminar (Suc)", f"{num}")
            self.mostrar_arbol()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def mostrar_inorden(self): self._push_result("InOrden", self.arbol.inOrden())
    def mostrar_preorden(self): self._push_result("PreOrden", self.arbol.preOrden())
    def mostrar_postorden(self): self._push_result("PostOrden", self.arbol.postOrden())
    def mostrar_niveles(self): self._push_result("Por Niveles", self.arbol.recorrido_por_niveles())
    def mostrar_altura(self): self._push_result("Altura", self.arbol.altura())
    def mostrar_hojas(self): self._push_result("Hojas", self.arbol.contar_hojas())
    def mostrar_nodos(self): self._push_result("Nodos", self.arbol.contar_nodos())
    def verificar_completo(self): self._push_result("¿Completo?", self.arbol.es_completo())
    def verificar_lleno(self): self._push_result("¿Lleno?", self.arbol.es_lleno())

    def mostrar_grados(self):
        grados = self.arbol.grados_por_nodo()
        if not grados:
            self._push_result("Grados", "Árbol vacío")
            return
        self._push_result("Grados (nodo,grado)", grados)

    def limpiar_arbol(self):
        self.arbol.eliminar_arbol()
        self.canvas.delete("all")
        self._clear_results()
        self.status.config(text="Árbol limpiado.")

    def mostrar_arbol(self):
        self.canvas.delete("all")
        if not self.arbol.raiz:
            return

        niveles = {}
        def _fill(n, nivel, pos_x):
            if nivel not in niveles:
                niveles[nivel] = []
            niveles[nivel].append((n, pos_x))
            if n.izq:
                _fill(n.izq, nivel + 1, pos_x - 80 / (nivel + 1))
            if n.der:
                _fill(n.der, nivel + 1, pos_x + 80 / (nivel + 1))

        _fill(self.arbol.raiz, 0, 0)

        width = int(self.canvas.winfo_width() or 800)
        height = int(self.canvas.winfo_height() or 600)
        level_y_gap = max(80, height // (len(niveles) + 2))

        all_x = [pos for nivel in niveles.values() for (_, pos) in nivel]
        min_x, max_x = min(all_x), max(all_x)
        scale = (width - 100) / (max_x - min_x + 1e-5)

        positions = {}
        for nivel, nodos in niveles.items():
            for nodo, pos_x in nodos:
                x = int((pos_x - min_x) * scale + 50)
                y = 50 + nivel * level_y_gap
                positions[nodo] = (x, y)

        for nodo, (x, y) in positions.items():
            if nodo.izq:
                x2, y2 = positions[nodo.izq]
                self.canvas.create_line(x, y, x2, y2, width=2)
            if nodo.der:
                x2, y2 = positions[nodo.der]
                self.canvas.create_line(x, y, x2, y2, width=2)

        r = 22
        for nodo, (x, y) in positions.items():
            self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="#90caf9", outline="black")
            self.canvas.create_text(x, y, text=str(nodo.dato), font=("Arial", 10, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x740")
    app = ArbolGUI(root)
    app.mainloop()

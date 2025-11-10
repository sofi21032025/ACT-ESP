# mexico_7_estados_realista.py
import math
import itertools
import os
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Tuple, List

# -------------------- Centroides aproximados (lat, lon) --------------------
ESTADOS_COORD: Dict[str, Tuple[float, float]] = {
    "Aguascalientes": (21.8818, -102.2916),
    "Baja California": (32.5343, -117.0379),
    "Baja California Sur": (24.1426, -110.3128),
    "Campeche": (19.8301, -90.5349),
    "Coahuila": (25.4267, -101.0000),
    "Colima": (19.2433, -103.7250),
    "Chiapas": (16.7520, -93.1167),
    "Chihuahua": (28.6353, -106.0889),
    "Ciudad de México": (19.4326, -99.1332),
    "Durango": (24.0277, -104.6532),
    "Guanajuato": (21.0190, -101.2574),
    "Guerrero": (17.5515, -99.5000),
    "Hidalgo": (20.1230, -98.7333),
    "Jalisco": (20.6736, -103.3440),
    "México": (19.2899, -99.6532),
    "Michoacán": (19.7008, -101.1844),
    "Morelos": (18.9242, -99.2216),
    "Nayarit": (21.5110, -104.8957),
    "Nuevo León": (25.6866, -100.3161),
    "Oaxaca": (17.0732, -96.7266),
    "Puebla": (19.0414, -98.2063),
    "Querétaro": (20.5888, -100.3899),
    "Quintana Roo": (18.5000, -88.3000),
    "San Luis Potosí": (22.1565, -100.9855),
    "Sinaloa": (24.8066, -107.3940),
    "Sonora": (29.0729, -110.9559),
    "Tabasco": (17.9892, -92.9291),
    "Tamaulipas": (23.7369, -99.1411),
    "Tlaxcala": (19.3182, -98.2375),
    "Veracruz": (19.5438, -96.9103),
    "Yucatán": (20.9674, -89.5926),
    "Zacatecas": (22.7709, -102.5833),
}

# -------------------- Silueta (respaldo) --------------------
MEXICO_POLY: List[Tuple[float, float]] = [
    (-117.1, 32.5), (-114.7, 31.3), (-112.9, 28.8), (-111.5, 26.0), (-111.4, 24.7),
    (-110.4, 24.1), (-109.9, 23.0), (-111.5, 24.8), (-112.9, 27.5), (-114.5, 30.0),
    (-112.2, 31.3), (-109.5, 31.3), (-106.5, 31.8), (-103.0, 29.0), (-99.5, 26.0),
    (-97.3, 25.5), (-96.0, 22.5), (-95.5, 20.8), (-94.5, 18.5), (-93.0, 18.0),
    (-92.2, 16.0), (-92.2, 15.0), (-95.2, 16.0), (-98.0, 16.3), (-103.6, 18.2),
    (-106.5, 20.5), (-108.9, 23.2), (-110.0, 24.0), (-114.0, 30.5), (-117.1, 32.5),
]

# -------------------- Distancia (Haversine en km) --------------------
def haversine_km(lat1, lon1, lat2, lon2) -> float:
    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(a))

def costo(u: str, v: str) -> int:
    (la, lo), (lb, lblo) = ESTADOS_COORD[u], ESTADOS_COORD[v]
    return int(round(haversine_km(la, lo, lb, lblo)))

# -------------------- Hamiltoniano mínimo --------------------
def hamiltoniano_minimo(nodes: List[str]) -> Tuple[List[str], int]:
    start = nodes[0]
    others = [n for n in nodes if n != start]
    mejor_camino, mejor_costo = None, math.inf
    for perm in itertools.permutations(others):
        path = [start] + list(perm)
        cost = sum(costo(a, b) for a, b in zip(path, path[1:]))
        if cost < mejor_costo:
            mejor_costo, mejor_camino = cost, path
    return mejor_camino, mejor_costo

# ============================ GUI ============================
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("7 estados de México — Mapa realista en Tkinter")
        self.geometry("1220x780")

        # ----- izquierda: selección -----
        left = ttk.Labelframe(self, text="Elige exactamente 7 estados", padding=8)
        left.pack(side="left", fill="y", padx=10, pady=10)

        self.lb = tk.Listbox(left, selectmode=tk.MULTIPLE, width=28, height=24)
        for e in sorted(ESTADOS_COORD.keys()):
            self.lb.insert(tk.END, e)
        self.lb.pack(fill="y", expand=False)

        btns = ttk.Frame(left); btns.pack(fill="x", pady=6)
        ttk.Button(btns, text="Usar selección (7)", command=self.usar).pack(fill="x", pady=2)
        ttk.Button(btns, text="Limpiar", command=lambda: self.lb.selection_clear(0, tk.END)).pack(fill="x", pady=2)

        # ----- derecha: resultados -----
        right = ttk.Labelframe(self, text="Resultados", padding=8)
        right.pack(side="right", fill="both", expand=False, padx=10, pady=10)
        self.txt = tk.Text(right, width=48, height=36, font=("Consolas", 10))
        self.txt.pack(fill="both", expand=True)

        # ----- centro: canvas mapa -----
        mid = ttk.Labelframe(self, text="Mapa de la República Mexicana", padding=8)
        mid.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.W, self.H = 860, 680
        self.canvas = tk.Canvas(mid, width=self.W, height=self.H, bg="white")
        self.canvas.pack(fill="both", expand=True)

        # bounding box geográfica (debe corresponder al PNG si lo usas)
        self.lon_min, self.lon_max = -118, -86
        self.lat_min, self.lat_max = 14, 33.5

        # fondo (PNG opcional)
        self.bg_image = None
        self.use_photo = False
        self._try_load_background()

        topbar = ttk.Frame(mid); topbar.place(x=10, y=10)
        self.toggle_btn = ttk.Button(topbar, text="Fondo: silueta", command=self.toggle_background)
        self.toggle_btn.pack()

        self.seleccion: List[str] = []
        self._draw_background()

    # ---------- cargar/alternar fondo ----------
    def _try_load_background(self):
        # Carga mapa_mexico.png si existe (mismo directorio)
        png_path = os.path.join(os.path.dirname(__file__), "mapa_mexico.png")
        if os.path.exists(png_path):
            try:
                # Tk PhotoImage soporta PNG en Tk 8.6+
                self.bg_image = tk.PhotoImage(file=png_path)
                self.use_photo = True
            except Exception:
                self.bg_image = None
                self.use_photo = False

    def toggle_background(self):
        self.use_photo = not self.use_photo and (self.bg_image is not None)
        self.toggle_btn.config(text="Fondo: mapa" if self.use_photo else "Fondo: silueta")
        self._draw_background()
        if self.seleccion:
            self._draw_all(self.seleccion)

    # ---------- transformaciones ----------
    def _geo_to_xy(self, lat, lon):
        # Proyección equirectangular simple
        x = (lon - self.lon_min) / (self.lon_max - self.lon_min) * (self.W - 40) + 20
        y = (self.lat_max - lat) / (self.lat_max - self.lat_min) * (self.H - 40) + 20
        return x, y

    # ---------- dibujo del fondo ----------
    def _draw_background(self):
        self.canvas.delete("all")
        if self.use_photo and self.bg_image is not None:
            # Ajustar imagen centrada (asumimos que fue preparada para estos límites)
            self.canvas.create_image(self.W//2, self.H//2, image=self.bg_image)
        else:
            # Silueta vectorial de respaldo
            pts = []
            for (lon, lat) in MEXICO_POLY:
                x, y = self._geo_to_xy(lat, lon)
                pts.extend([x, y])
            self.canvas.create_polygon(*pts, fill="#eef6ff", outline="#1a73e8", width=2)
        # grid suave
        for lon in range(-118, -85, 4):
            x1, y1 = self._geo_to_xy(self.lat_min, lon)
            x2, y2 = self._geo_to_xy(self.lat_max, lon)
            self.canvas.create_line(x1, y1, x2, y2, fill="#00000018")
        for lat in range(14, 35, 3):
            x1, y1 = self._geo_to_xy(lat, self.lon_min)
            x2, y2 = self._geo_to_xy(lat, self.lon_max)
            self.canvas.create_line(x1, y1, x2, y2, fill="#00000018")

    # ---------- interacción ----------
    def usar(self):
        idx = self.lb.curselection()
        if len(idx) != 7:
            messagebox.showerror("Error", "Selecciona exactamente 7 estados.")
            return
        self.seleccion = [self.lb.get(i) for i in idx]
        self._draw_all(self.seleccion)
        self._mostrar_estados_y_relaciones()
        self._calcula_y_dibuja_recorridos()

    # ---------- dibujo y cálculo ----------
    def _draw_all(self, estados: List[str]):
        self._draw_background()
        # puntos de estados
        for e in estados:
            lat, lon = ESTADOS_COORD[e]
            x, y = self._geo_to_xy(lat, lon)
            r = 7
            self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="#ffcc80", outline="#e65100", width=2)
            self.canvas.create_text(x+10, y-10, text=e, anchor="w", font=("Arial", 9, "bold"))
        # líneas grises y pesos
        for i in range(len(estados)):
            for j in range(i+1, len(estados)):
                a, b = estados[i], estados[j]
                la, loa = ESTADOS_COORD[a]
                lb, lob = ESTADOS_COORD[b]
                xa, ya = self._geo_to_xy(la, loa)
                xb, yb = self._geo_to_xy(lb, lob)
                self.canvas.create_line(xa, ya, xb, yb, fill="#777", width=1)
                xm, ym = (xa+xb)/2, (ya+yb)/2
                self.canvas.create_text(xm, ym, text=str(costo(a, b)), fill="#333", font=("Consolas", 8))

    def _calcula_y_dibuja_recorridos(self):
        path, cost_a = hamiltoniano_minimo(self.seleccion)
        ciclo = path + [path[0]]
        cost_b = cost_a + costo(path[-1], path[0])

        # dibujar encima
        def draw_seg(u, v, color, dash=None, width=4):
            la, loa = ESTADOS_COORD[u]
            lb, lob = ESTADOS_COORD[v]
            xa, ya = self._geo_to_xy(la, loa)
            xb, yb = self._geo_to_xy(lb, lob)
            self.canvas.create_line(xa, ya, xb, yb, fill=color, width=width, dash=dash)

        for u, v in zip(path, path[1:]):
            draw_seg(u, v, "#d32f2f")          # camino (a)
        draw_seg(ciclo[-2], ciclo[-1], "#2e7d32", dash=(6, 4))  # cierre (b)

        # salida
        self._append("\n=== RECORRIDOS ===")
        self._append(f"(a) Sin repetir:\n    {' -> '.join(path)}")
        self._append(f"    Costo total (a): {cost_a} km\n")
        self._append(f"(b) Repitiendo al menos uno (tour):\n    {' -> '.join(ciclo)}")
        self._append(f"    Costo total (b): {cost_b} km\n")

    # ---------- texto ----------
    def _mostrar_estados_y_relaciones(self):
        self.txt.delete("1.0", tk.END)
        self._append("=== Estados seleccionados (7) ===")
        for i, e in enumerate(self.seleccion, 1):
            self._append(f"{i}. {e}")
        self._append("\n=== Relaciones (aristas con costo en km) ===")
        for i in range(len(self.seleccion)):
            for j in range(i+1, len(self.seleccion)):
                a, b = self.seleccion[i], self.seleccion[j]
                self._append(f"{a} -- {b} : {costo(a, b)}")

    def _append(self, s: str):
        self.txt.insert(tk.END, s + "\n")
        self.txt.see(tk.END)


if __name__ == "__main__":
    App().mainloop()

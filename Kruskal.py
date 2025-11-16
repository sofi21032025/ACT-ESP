class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n
    
    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]
    
    def union(self, x, y):
        raiz_x = self.find(x)
        raiz_y = self.find(y)
        
        if raiz_x == raiz_y:
            return False
        
        if self.rango[raiz_x] < self.rango[raiz_y]:
            self.padre[raiz_x] = raiz_y
        elif self.rango[raiz_x] > self.rango[raiz_y]:
            self.padre[raiz_y] = raiz_x
        else:
            self.padre[raiz_y] = raiz_x
            self.rango[raiz_x] += 1
        
        return True

def kruskal(aristas, num_nodos):
    aristas_ordenadas = sorted(aristas, key=lambda x: x[0])
    uf = UnionFind(num_nodos)
    arbol_expansion = []
    peso_total = 0
    
    for peso, u, v in aristas_ordenadas:
        if uf.union(u, v):
            arbol_expansion.append((u, v, peso))
            peso_total += peso
    
    return arbol_expansion, peso_total

aristas = [
    (1, 0, 1),
    (2, 0, 2),
    (3, 1, 2),
    (4, 1, 3),
    (5, 2, 3),
]
nodos = ['A', 'B', 'C', 'D']

arbol, peso = kruskal(aristas, len(nodos))
for u, v, peso_arista in arbol:
    print(f"{nodos[u]} - {nodos[v]}: peso {peso_arista}")
print(f"Peso total: {peso}")
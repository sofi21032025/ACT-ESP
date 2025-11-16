def floyd_warshall(grafo, nodos):
    n = len(nodos)
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for i in range(n):
        for j in range(n):
            if grafo[i][j] != 0:
                dist[i][j] = grafo[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

INF = float('inf')
grafo = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]
nodos = ['A', 'B', 'C', 'D']

resultado = floyd_warshall(grafo, nodos)
for i, nodo_i in enumerate(nodos):
    for j, nodo_j in enumerate(nodos):
        print(f"{nodo_i} a {nodo_j}: {resultado[i][j]}")
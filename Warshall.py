def warshall(grafo, nodos):
    n = len(nodos)
    alcanzable = [[grafo[i][j] for j in range(n)] for i in range(n)]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                alcanzable[i][j] = alcanzable[i][j] or (alcanzable[i][k] and alcanzable[k][j])
    
    return alcanzable

grafo = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]
nodos = ['A', 'B', 'C', 'D']

resultado = warshall(grafo, nodos)
for i, nodo_i in enumerate(nodos):
    for j, nodo_j in enumerate(nodos):
        if resultado[i][j]:
            print(f"{nodo_i} puede alcanzar a {nodo_j}")
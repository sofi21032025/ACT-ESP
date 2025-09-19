import random
import time
from statistics import mean

def generar_calificaciones(num_alumnos: int, num_materias: int, seed: int = 42):
    random.seed(seed)
    return [random.randint(0, 100) for _ in range(num_alumnos * num_materias)]

def build_por_alumno(data_flat, num_alumnos, num_materias):
    A = []
    it = iter(data_flat)
    for _ in range(num_alumnos):
        fila = [next(it) for _ in range(num_materias)]
        A.append(fila)
    return A

def get_por_alumno(A, alumno_idx, materia_idx):
    return A[alumno_idx][materia_idx]

def build_por_materia(data_flat, num_alumnos, num_materias):
    B = [[0]*num_alumnos for _ in range(num_materias)]
    k = 0
    for a in range(num_alumnos):
        for m in range(num_materias):
            B[m][a] = data_flat[k]
            k += 1
    return B

def get_por_materia(B, alumno_idx, materia_idx):
    return B[materia_idx][alumno_idx]

def timeit(fn, repeticiones=5):
    tiempos = []
    for _ in range(repeticiones):
        t0 = time.perf_counter()
        fn()
        t1 = time.perf_counter()
        tiempos.append(t1 - t0)
    return mean(tiempos)

def benchmark_construccion(num_alumnos, num_materias):
    datos = generar_calificaciones(num_alumnos, num_materias)
    t_build_A = timeit(lambda: build_por_alumno(datos, num_alumnos, num_materias))
    t_build_B = timeit(lambda: build_por_materia(datos, num_alumnos, num_materias))
    return t_build_A, t_build_B

def benchmark_acceso(num_alumnos, num_materias, n_lookups=10000):
    datos = generar_calificaciones(num_alumnos, num_materias, seed=123)
    A = build_por_alumno(datos, num_alumnos, num_materias)
    B = build_por_materia(datos, num_alumnos, num_materias)

    pares = [(random.randrange(num_alumnos), random.randrange(num_materias)) for _ in range(n_lookups)]

    def acc_A():
        s = 0
        for a, m in pares:
            s += get_por_alumno(A, a, m)
        return s

    def acc_B():
        s = 0
        for a, m in pares:
            s += get_por_materia(B, a, m)
        return s

    t_acc_A = timeit(acc_A, repeticiones=3)
    t_acc_B = timeit(acc_B, repeticiones=3)

    return t_acc_A, t_acc_B

def demo_500x6_busqueda():
    num_alumnos, num_materias = 500, 6
    datos = generar_calificaciones(num_alumnos, num_materias, seed=99)
    A = build_por_alumno(datos, num_alumnos, num_materias)   
    B = build_por_materia(datos, num_alumnos, num_materias)  

    alumno_id = 321        
    materia_id = 5         

    a_idx = alumno_id - 1
    m_idx = materia_id - 1

    valor_A = get_por_alumno(A, a_idx, m_idx)
    valor_B = get_por_materia(B, a_idx, m_idx)

    assert valor_A == valor_B, "Los valores deben coincidir entre disposiciones"
    print(f"[BUSQUEDA] Alumno {alumno_id}, Materia {materia_id} → Calificación: {valor_A}")

def main():
    print("=== DEMO: 500 alumnos × 6 materias y búsqueda específica ===")
    demo_500x6_busqueda()

    pruebas = [
        (500, 6),
        (1000, 6),
        (500, 100),
        (10000, 6),
        (1000, 500),
        (100000, 6),  
    ]

    print("\n=== Benchmark de construcción (segundos promedio) ===")
    print(f"{'Alumnos':>8} {'Materias':>9} {'Build A(alumno)':>16} {'Build B(materia)':>17}")
    for a, m in pruebas:
        tA, tB = benchmark_construccion(a, m)
        print(f"{a:8d} {m:9d} {tA:16.6f} {tB:17.6f}")

    print("\n=== Benchmark de acceso aleatorio (segundos promedio, 10k lookups) ===")
    print(f"{'Alumnos':>8} {'Materias':>9} {'Acceso A':>12} {'Acceso B':>12}")
    for a, m in pruebas:
        lookups = 10000 if a*m <= 5_000_000 else 2000
        tA, tB = benchmark_acceso(a, m, n_lookups=lookups)
        print(f"{a:8d} {m:9d} {tA:12.6f} {tB:12.6f}")

    print("\nNota:")
    print("- Disposición A (por alumno): acceso directo A[alumno][materia].")
    print("- Disposición B (por materia): acceso directo B[materia][alumno].")
    print("- Según el patrón de acceso, una u otra puede ser ligeramente más rápida por localidad de caché.")
    print("- En Python puro (listas), las diferencias suelen ser pequeñas; lo importante es la *coherencia* del patrón de acceso.")

if __name__ == "__main__":

    main()

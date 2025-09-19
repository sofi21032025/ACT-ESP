import random

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

def demo_500x6_busqueda():
    num_alumnos, num_materias = 500, 6
    datos = generar_calificaciones(num_alumnos, num_materias, seed=99)
    A = build_por_alumno(datos, num_alumnos, num_materias)   
    B = build_por_materia(datos, num_alumnos, num_materias)  

    print("=== Calificaciones de los 500 alumnos ===")
    for i, fila in enumerate(A, start=1):
        print(f"Alumno {i}: {fila}")

    alumno_id = 321        
    materia_id = 5         

    a_idx = alumno_id - 1
    m_idx = materia_id - 1

    valor_A = get_por_alumno(A, a_idx, m_idx)
    valor_B = get_por_materia(B, a_idx, m_idx)

    assert valor_A == valor_B, "Los valores deben coincidir entre disposiciones"
    print("\n=== Búsqueda solicitada ===")
    print(f"Alumno {alumno_id}, Materia {materia_id} → Calificación: {valor_A}")

def main():
    print("=== DEMO: 500 alumnos × 6 materias y búsqueda específica ===")
    demo_500x6_busqueda()

if __name__ == "__main__":
    main()


import random
import time
from concurrent.futures import ThreadPoolExecutor

# Cálculo sequencial de Pi usando o Método de Monte Carlo
def calculate_pi_sequential(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x, y = random.random(), random.random()  # Gera coordenadas aleatórias
        if x**2 + y**2 <= 1:
            inside_circle += 1  # Verifica se o ponto está dentro do círculo
    return 4 * inside_circle / num_points  # Aproximação de Pi

# Cálculo paralelo de Pi utilizando Threads
def calculate_pi_parallel(num_points, num_threads):
    def worker(points):
        inside = 0
        for _ in range(points):
            x, y = random.random(), random.random()
            if x**2 + y**2 <= 1:
                inside += 1
        return inside

    points_per_thread = num_points // num_threads
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(worker, [points_per_thread] * num_threads)
    
    total_inside = sum(results)
    return 4 * total_inside / num_points

if __name__ == "__main__":
    NUM_POINTS = 1000000  # Número total de pontos a serem gerados
    NUM_THREADS = 4  # Número de threads para a execução paralela

    # Execução Sequencial
    start_time = time.time()
    pi_seq = calculate_pi_sequential(NUM_POINTS)
    seq_time = time.time() - start_time
    print(f"Sequencial: Pi = {pi_seq}, Tempo = {seq_time:.4f} segundos")

    # Execução Paralela
    start_time = time.time()
    pi_par = calculate_pi_parallel(NUM_POINTS, NUM_THREADS)
    par_time = time.time() - start_time
    print(f"Paralelo: Pi = {pi_par}, Tempo = {par_time:.4f} segundos")

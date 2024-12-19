import socket
import time

def distributed_server(host, port, num_points, num_clients):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Servidor aguardando conexões em {host}:{port}...")

    connections = []
    total_inside = 0

    # Aceita conexões de clientes
    while len(connections) < num_clients:
        conn, addr = server_socket.accept()
        print(f"Conexão recebida de {addr}")
        connections.append(conn)

    points_per_client = num_points // len(connections)
    remaining_points = num_points % len(connections)

    start_time = time.time()

    # Envia os pontos para os clientes
    for i, conn in enumerate(connections):
        points_to_send = points_per_client + (1 if i < remaining_points else 0)
        conn.sendall(str(points_to_send).encode())

    # Recebe os resultados dos clientes
    for conn in connections:
        try:
            data = conn.recv(1024)
            total_inside += int(data.decode())
        except ValueError:
            print(f"Dado inválido recebido.")
        finally:
            conn.close()

    end_time = time.time()
    server_socket.close()

    execution_time = end_time - start_time
    return 4 * total_inside / num_points, execution_time

if __name__ == "__main__":
    NUM_POINTS = 1000000  # Número total de pontos
    NUM_CLIENTS = 2  # Número de clientes esperados
    pi, execution_time = distributed_server('localhost', 5000, NUM_POINTS, NUM_CLIENTS)
    print(f"Resultado Distribuido: Pi = {pi}, Tempo = {execution_time:.4f} segundos")

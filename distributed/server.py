import socket

def distributed_server(host, port, num_points, num_clients):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Servidor aguardando conexões em {host}:{port}...")

    connections = []
    total_inside = 0
    clients = 0

    # Aceita conexões de clientes
    while clients < num_clients:
        conn, addr = server_socket.accept()
        print(f"Conexão recebida de {addr}")
        connections.append(conn)
        clients += 1

    points_per_client = num_points // len(connections)

    # Envia os pontos para os clientes
    for conn in connections:
        conn.sendall(str(points_per_client).encode())

    # Recebe os resultados dos clientes
    for conn in connections:
        data = conn.recv(1024)
        total_inside += int(data.decode())
        conn.close()

    server_socket.close()
    return 4 * total_inside / num_points

if __name__ == "__main__":
    NUM_POINTS = 1000000  # Número total de pontos
    NUM_CLIENTS = 2  # Número de clientes esperados
    print(f"Resultado Distribuído: Pi = {distributed_server('localhost', 5000, NUM_POINTS, NUM_CLIENTS)}")

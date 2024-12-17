import socket
import random

def distributed_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))  # Conecta ao servidor

    # Recebe o número de pontos a serem calculados
    points = int(client_socket.recv(1024).decode())
    inside_circle = 0

    # Calcula os pontos dentro do círculo
    for _ in range(points):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1

    # Envia o resultado para o servidor
    client_socket.sendall(str(inside_circle).encode())
    client_socket.close()

if __name__ == "__main__":
    distributed_client('localhost', 5000)

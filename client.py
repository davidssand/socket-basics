import socket
import threading

PORT = 2001
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"

# Define a conexão
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", PORT))

# Escuta e exibe mensagens vindas do servidor
def handle_receive():
    while 1:
        print(client.recv(1000).decode(FORMAT))

# Iniciar thread para escutar mensagens
thread = threading.Thread(target=handle_receive)
thread.start()

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)

# Envia ao servidor mensagens do teclado
message = ""
while 1:
    print(message)
    message = input()
    if message:
        send(message)

import socket 
import threading

PORT = 2001
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"

# Define a conexão
server = socket.socket()
server.bind(("", PORT))
clients = list()


# Define estrutura de dados para o cliente
class Client():
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

    def __repr__(self):
        return f"Cliente {self.addr}"


# Lida com requests de clientes
def handle_request(current_client):
    print(f"Nova conexão: {current_client.addr}")

    connected = True
    while connected:
        msg = current_client.conn.recv(1000).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False

        current_client.conn.send("Mensagem recebida".encode(FORMAT))
        other_client = [client for client in clients if not(client.addr == current_client.addr)]
        if not other_client:
            print("Destinatário não encontrado")
            continue

        other_client[0].conn.send(f"Mensagem recebida de {current_client}: {msg}".encode(FORMAT))
        print(f"{current_client} enviou '{msg}' a {other_client}")

    current_client.conn.close()
        

# Inicializa o servidor e escuta clientes
def start():
    server.listen()
    while True:
        client = Client(*server.accept())
        thread = threading.Thread(target=handle_request, args=(client,))
        thread.start()
        clients.append(client)
        print(f"== Número de conexões ativas == {threading.activeCount() - 1}")


print("Servidor inicializado")
start()
import socket
import threading

host = "127.0.0.1"
port = 55557

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print("Сервер запущен!")

clients = []
nicknames = []


def broadcast(message, source_client):
    for client in clients:
        if client is not source_client:
            client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast("{} отсоединился!".format(nickname).encode("utf-8"), client)
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = server.accept()
        print("Соединение с {}".format(str(address)))

        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(f"Имя: {nickname}")
        broadcast(f"{nickname} подсоединился!".encode("utf-8"), client)
        client.send("Соединение с сервером!".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()

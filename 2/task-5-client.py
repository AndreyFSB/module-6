import socket
import threading

nickname = input("Выбери имя: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55557))
client.send(nickname.encode("utf-8"))


def receive():
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            print(message)
        except Exeption as e:
            print("Ошибка {er}! Закрываю соединение!")
            client.close()
            break


def write():
    while True:
        message = "{}: {}".format(nickname, input(""))
        client.send(message.encode("utf-8"))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

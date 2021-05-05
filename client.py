import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def get_ans():
    message = client.recv(2408).decode(FORMAT)
    print(f'{message} \n')


def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2408).decode(FORMAT))


send('Hello')

while True:
    msg = input()
    send(msg)
    if msg == DISCONNECT_MESSAGE:
        break
    else:
        values = input()
        send(values)
        get_ans()

import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    msg_len = conn.recv(HEADER).decode(FORMAT)
    msg_len = int(msg_len)
    msg = conn.recv(msg_len).decode(FORMAT)
    print(f'{addr} {msg}')

    connected = True
    while connected:
        conn.send('''[WELCOME] press 1 for Addition\n press 2 for Subtraction\n press !DISCONNECT for closing 
        connection'''.encode(FORMAT))

        msg_len = conn.recv(HEADER).decode(FORMAT)
        msg_len = int(msg_len)
        message = conn.recv(msg_len).decode(FORMAT)

        if message == DISCONNECT_MESSAGE:
            conn.send('Thank you'.encode(FORMAT))
            connected = False
        else:

            conn.send('Give input'.encode(FORMAT))
            val_len = conn.recv(HEADER).decode(FORMAT)
            val_len = int(val_len)
            val = conn.recv(val_len).decode(FORMAT)
            conn.send('''[INPUT] received\n'''.encode(FORMAT))
            a, b = (val.split(' '))

            if message == '1':
                result = int(a) + int(b)
                conn.send(str(result).encode(FORMAT))
            else:
                result = int(a) - int(b)
                conn.send(str(result).encode(FORMAT))

    conn.close()


def start():
    while True:
        server.listen()
        conn, addr = server.accept()
        handle_client(conn, addr)


print("[STARTING] server is starting")
start()

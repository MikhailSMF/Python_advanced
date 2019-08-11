import socket

if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('127.0.0.1', 7777))
    sock.listen(5)

    print(f'Server started')

    while True:
        client, address = sock.accept()
        client_host, client_port = address
        print(f'Client connected {client_host}:{client_port}')

        bytes_request = client.recv(1024)
        print(f'Client send {bytes_request.decode()}')

        client.send(bytes_request)
        client.close()

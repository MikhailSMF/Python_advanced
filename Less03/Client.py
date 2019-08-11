import json
import socket
from argparse import ArgumentParser


config = {
    'host': '127.0.0.1',
    'port': 7777,
    'buffer': 1024
}

parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str, required=False,
    help='Sets config file path'
)

parser.add_argument(
    '-ht', '--host', type=str, required=False,
    help='Sets server host'
)

parser.add_argument(
    '-p', '--port', type=str, required=False,
    help='Sets server port'
)

args = parser.parse_args()


if args.config:
    with open(args.config) as file:
        file_config = json.load(file)
        config.update(file_config or {})

if args.host:
    config['host'] = args.host

if args.port:
    config['port'] = args.port

if __name__ == '__main__':
    sock = socket.socket()
    sock.connect((config.get('host'), config.get('port')))
    print(f'Client was started')

    data = input('Enter data: ')
    sock.send(data.encode())
    print(f'Client send data')
    bytes_response = sock.recv(config.get('buffer'))
    print(bytes_response.decode())

    sock.close()

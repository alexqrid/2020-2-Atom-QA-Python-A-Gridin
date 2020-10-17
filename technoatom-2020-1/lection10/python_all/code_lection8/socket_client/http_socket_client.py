import socket

target_host = "127.0.0.1"
target_port = 5000
params = '/user/1'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.1)

client.connect((target_host, target_port))

request = f'GET {params} HTTP/1.1\r\nHost:{target_host}\r\n\r\n'
client.send(request.encode())

total_data = []

while True:
    data = client.recv(4096)
    if data:
        total_data.append(data.decode())
    else:
        break

data = ''.join(total_data).splitlines()
print(data[-1])

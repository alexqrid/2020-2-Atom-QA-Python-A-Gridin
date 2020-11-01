import socket

target_host = "127.0.0.1"
target_port = 1050
params = '/check_socket/yar'

# создаём объект клиентского сокета
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# выставляем ожидание для сокета
client.settimeout(0.1)

# устанавливаем соединение
client.connect((target_host, target_port))

# создаем и выполняем запрос
request = f'GET {params} HTTP/1.1\r\nHost:{target_host}\r\n\r\n'
client.send(request.encode())

total_data = []

while True:
    # читаем данные из сокета до тех пор пока они там есть
    data = client.recv(4096)
    if data:
        total_data.append(data.decode())
    else:
        break

data = ''.join(total_data).splitlines()
print(data[-1])

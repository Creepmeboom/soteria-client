import socket
T_PORT = 60
TCP_IP = '127.0.0.1'
BUF_SIZE = 1024
MSG = "hello Karl"
k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
k.connect((TCP_IP, T_PORT))

encoded = bytes(MSG, "utf-8")

k.send(encoded)
data = k.recv(BUF_SIZE)
k.close

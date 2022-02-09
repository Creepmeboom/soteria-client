import time
import socket
import base64
from lib.jsonconfigs import configClass
config = configClass()
import json
T_PORT = 23666
TCP_IP = '5.252.226.29'
BUF_SIZE = 1024

listen_port = 23666
listen_ip = '5.252.226.29'
buf_size = 1024
sso = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        sso.bind((listen_ip, listen_port))
        print("Bind Successful!")
        break
    except:
        print("Awaiting Port to be free...")
        time.sleep(1)
sso.listen(1)
incomm, rmaddr = sso.accept()
data = incomm.recv(buf_size)
print(f"Encoded Income: {data.decode('utf-8')}")
data = base64.b64decode(data, altchars=None)
print(f"Decoded Income: {data.decode('utf-8')}")
jdata = json.loads(data.decode('utf-8'))
if jdata['auth_token'] == "983245629836538465329":
    print(f"connection from {rmaddr} authorized!")
    answer_enc = bytes("AUTH_OK", "utf-8")
else:
    print(f"connection from {rmaddr} unauthorized!")
    answer_enc = bytes("AUTH_FAIL", "utf-8")
incomm.send(answer_enc)
incomm.close()
sso.close()
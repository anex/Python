import socket

HOST = '192.168.213.122'
PORT = 5038
s = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)

#.bind((HOST, PORT))
#.listen(1)
#onn, addr = s.accept()

#rint 'C', addr

s.connect((HOST,  PORT))

params = ["Action: login", 
    "Events: off", 
    "Username: admin", 
    "Secret: 123321..."]

s.send("\r\n".join(params) + "\r\n")

# receive login response
data = ""
while "\r\n" not in data:
    data += s.recv(1024)

s.send("Action: status\r\n\r\n")

# receive action response
data = ""
while "\r\n" not in data:
    data += s.recv(1024)
print repr(data)

s.send("Action: Logoff\r\n\r\n")
s.close()

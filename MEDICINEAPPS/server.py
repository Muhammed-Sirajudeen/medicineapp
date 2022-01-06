import socket

s=socket.socket()
print('socket created')
s.bind(('192.168.42.211',9999))

s.listen(3)

print("waiting for connection")

while True:
    c,addr=s.accept()
    print("connected with",addr)

    c.send('welcome to the disaco')

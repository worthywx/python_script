from socket import *

tc = socket(AF_INET, SOCK_STREAM)
tc.connect(('127.0.0.1', 23343))

while True:
    data = raw_input('> ')
    if not data:
        break
    tc.send(data)
    data = tc.recv(1024)
    if not data:
        break
    print data
tc.close()

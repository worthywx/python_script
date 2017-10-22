from socket import *
from time import ctime

HOST=''
PORT=23343
ADDR=(HOST, PORT)
BUFSIZE=1024

ts = socket(AF_INET, SOCK_STREAM)
ts.bind(ADDR)
ts.listen(5)

while True:
	print 'waiting for connecting......'
	tc, addr = ts.accept()
	print '...connected from', addr
	while True:
		data = tc.recv(BUFSIZE)
		if not data:
			break
		tc.send('[%s] %s' % (ctime(), data))
	tc.close()
ts.close()

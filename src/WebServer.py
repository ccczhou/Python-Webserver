'''
Created on Feb 25, 2012

@author: Colin
'''

import socket

host = ''
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

print 'listening'

conn, addr = sock.accept()
print 'Connection from', addr

data = conn.recv(1024)
print data
conn.close()
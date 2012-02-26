'''
Created on Feb 25, 2012

@author: Colin
'''

import socket
import os

host = ''
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(1)

print 'listening'

while 1:
    conn, addr = sock.accept()
    print 'Connection from', addr

    sockFile = conn.makefile('rw', 0)
    
    webpage = 'HTTP/1.0 200 OK\n\n'
    webpage += '<html><head><title>FileDirectory</title></head>'
    webpage +='<body>cwd:' + os.getcwd() + '<br/><br/>'
    for entry in os.listdir(os.getcwd()):
        webpage += entry +'<br/>'
    webpage += '</body></html>'
    
    print webpage
    sockFile.write(webpage)
    sockFile.close()
    conn.close()
    
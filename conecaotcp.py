#!/usr/bin/python

import sys,socket

servidor="173.45.93.20"

porta=80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if s.connect_ex((servidor, porta)) == 0:

                print s.recv(1024)

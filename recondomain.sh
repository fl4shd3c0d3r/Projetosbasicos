#!/bin/bash
for palavra in $(cat lista.txt)
do
resposta=$(curl -s -o  /dev/null -w "%{http_code}" $1/$palavra/)
if [ $resposta == "200" ]
then
echo "diretorio encontrado: $palavra"
fi
resposta2=$(curl -s -o  /dev/null -w "%{http_code}" $1/$palavra)
if  [ $resposta2 == "200" ]
then
echo "arquivo encontrado: $palavra"
fi
done


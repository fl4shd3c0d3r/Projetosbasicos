#!/bin/bash
echo "Digite a URL – Ex: sitealvo.com.br"
read url
echo "Aguarde, estamos analisando a index da URL  informado…"
wget $url
grep href index.html | cut -d "/" -f3 | grep "\." | cut -d '"' -f1 | grep -v "<a href="  | grep -v "<li" >feito
for url in $(cat feito);do host $url; done |grep "has address" 

# Apaga as linhas duplicadas, dominios com o mesmo IP”
awk '! ($0 in a) {a[$0];print}'> feito
rm index.html
rm feito

echo “O Teste foi Finalizado !”


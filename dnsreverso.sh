#!/bin/bash
for ip in $(seq 16 23);
do
host $1.$ip
done

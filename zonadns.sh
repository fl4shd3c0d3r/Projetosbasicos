#!/bin/bash
for serve in $(host -t ns $1 | cut -d " " -f 4);
do
host -l $1 $serve | grep "has address"
done


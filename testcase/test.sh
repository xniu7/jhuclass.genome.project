#!/bin/bash
i=0
j=0
while [ "$i" -lt 2 ]
do
  while [ "$j" -lt 3 ]
  do
    echo $i, $j
    j=$(($j+1))
  done
  j=0
  i=$(($i+1))
done

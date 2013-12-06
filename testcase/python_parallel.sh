#!/bin/bash
t_num=9 seq_len=1000000 exp=8
while [ $t_num -gt 1 ]; do
   while [ $seq_len -gt 1 ]; do
	while [ $exp -gt 1 ]; do
	   echo "-------------------------------------------------"
	   ../tools/test_parallel.py $t_num $seq_len $exp
	   echo "thread num=$t_num, sequence length=$seq_len exponent=$exp"
   	let "exp=$exp/2"
	done
   let "seq_len=$seq_len/100"
   exp=8
   done
let "t_num=$t_num/3"
seq_len=1000000
done

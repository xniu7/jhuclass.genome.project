#!/bin/bash
temp_file=./res_py_pa.txt
echo "" > $temp_file
t_num=9 seq_len=1000000 exp=8
while [ $t_num -gt 1 ]; do
   while [ $seq_len -gt 1 ]; do
	while [ $exp -gt 1 ]; do
	   echo "-------------------------------------------------" >> $temp_file
	   ../tools/test_parallel.py $t_num $seq_len $exp >> $temp_file
	   echo "thread num=$t_num, sequence length=$seq_len exponent=$exp" >> $temp_file
   	let "exp=$exp/2"
	done
   let "seq_len=$seq_len/100"
   exp=8
   done
let "t_num=$t_num/3"
seq_len=1000000
done
cat $temp_file

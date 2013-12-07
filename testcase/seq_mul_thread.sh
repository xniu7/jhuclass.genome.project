#!/bin/bash
hdstream_path="/home/hduser/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar"
code_abs_path="/home/hduser/code/mapred"
data_abs_path="/home/hduser/data/mapred"
dfs_path="/user/hduser"
thread_num=2
temp_file=./res_seq_mul_th.txt
large_sample=100000

echo "" > $temp_file

if [ "$#" -eq 1 ]; then
   echo "================================="
   echo "starting process $1"
   echo "================================="
   echo "process $1" >> $temp_file
   echo "---------------------------------">> $temp_file
   while [ $thread_num -le 8 ]; do
   	../pdc3/pDC3.py $thread_num sequential < $1 >> $temp_file
   	../pdc3/pDC3.py $thread_num multiproc < $1 >> $temp_file
   	../pdc3/pDC3.py $thread_num threadpool < $1 >> $temp_file
	let "thread_num=$thread_num*2"
   done
   thread_num=2
   echo "---------------------------------">> $temp_file
else
   file_path="../sample"
   file_name=10
   while [ $file_name -le $large_sample ]; do
        echo "================================="
	echo "starting process $file_name"
        echo "================================="
	echo "process $file_name" >> $temp_file
	echo "---------------------------------" >> $temp_file
	while [ $thread_num -le 8 ]; do
           ../pdc3/pDC3.py $thread_num sequential < $file_path/$file_name >> $temp_file
           ../pdc3/pDC3.py $thread_num multiproc < $file_path/$file_name >> $temp_file
           ../pdc3/pDC3.py $thread_num threadpool < $file_path/$file_name >> $temp_file
           let "thread_num=$thread_num*2"
        done
        thread_num=2
	echo "---------------------------------">> $temp_file
   let "file_name=$file_name*10"
   done
fi
cat $temp_file

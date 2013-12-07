#!/bin/bash

#the hadoop streaming jar path
hdstream_path="/home/hduser/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar"
#the mapred code path of our program, same as '../mapred' but we need absolute path
code_abs_path="/home/hduser/code/mapred"
#the mapred sa output path, you need to create it first by yourself
data_abs_path="/home/hduser/data/mapred"
#the hdfs path of your hadoop file system. be careful choose the path, because in our example, we will delete /user/hduser/genome* for each compuation
dfs_path="/user/hduser"

dc=3
thread_num=10
run_type=multiproc
temp_file=./res_dc_pdc_hd.txt
large_sample=100000

echo "" > $temp_file

if [ "$#" -eq 1 ]; then
   echo "================================="
   echo "starting process $1"
   echo "================================="
   echo "process $1" >> $temp_file
   echo "---------------------------------">> $temp_file
   ../mapred/hadoop_run.sh $dc $1 $code_abs_path $data_abs_path $dfs_path $hdstream_path >> $temp_file
   ../dc3/dc.py < $1 >> $temp_file
   ../pdc3/pDC3.py $thread_num $run_type < $1 >> $temp_file
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
	../mapred/hadoop_run.sh $dc $file_path/$file_name $code_abs_path $data_abs_path $dfs_path $hdstream_path >> $temp_file
	../dc3/dc.py < $file_path/$file_name >> $temp_file
	../pdc3/pDC3.py $thread_num $run_type < $file_path/$file_name >> $temp_file
	echo "---------------------------------">> $temp_file
   let "file_name=$file_name*10"
   done
fi
cat $temp_file

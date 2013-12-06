#!/bin/bash

# path config
dfs_dir="/user/hduser" data_dir="/home/hduser/data/mapred"
dfs_input=$dfs_dir/genome_input input=$data_dir/genome_input
dfs_output=$dfs_dir/genome_output output=$data_dir/genome_output
dfs_rec_file=$dfs_dir/genome_rec rec_file=$data_dir/genome_rec
dfs_temp_file=$dfs_dir/genome_temp
code_dir="/home/hduser/code/mapred"
hd_stream_dir="/home/hduser/hadoop/contrib/streaming/"

cat $2 > $input # copy given data to input

./preproc.py <  $input  >  $rec_file # preprocessing data

hadoop dfs -rmr $dfs_dir/* # delete outdated files in dfs
hadoop dfs -put $rec_file $dfs_rec_file # copy data to dfs

START=$(date +%s.%N) # time start

max_name=0 total_size=1 counter=0

# if names are not unique, continue
until [ $max_name -eq $total_size ]; do
   # first mapred job
   hadoop dfs -rmr $dfs_temp_file
   hadoop jar $hd_stream_dir/hadoop-*streaming*.jar -cmdenv dc=$1 -mapper $code_dir/mapper.py -reducer $code_dir/reducer.py -input $dfs_rec_file -output $dfs_temp_file -jobconf mapred.map.tasks=1 mapred.reduce.tasks=1
   # second mapred job
   hadoop dfs -rmr $dfs_rec_file
   hadoop jar $hd_stream_dir/hadoop-*streaming*.jar -cmdenv dc=$1 -mapper $code_dir/mapper2.py -reducer $code_dir/reducer2.py -input $dfs_temp_file -output $dfs_rec_file -jobconf mapred.map.tasks=1 mapred.reduce.tasks=1
   
   # get max_name, total_size from the first and second line
   hadoop dfs -cat $dfs_rec_file/part* | head -2 > $rec_file
   max_name=$(awk 'NR==1 {print $1}' $rec_file)
   total_size=$(awk 'NR==2 {print $1}' $rec_file)
   let counter+=1 #recursive deepth
done

# get SA from names
hadoop dfs -cat $dfs_rec_file/part* | $code_dir/getSA.py $counter > $output

END=$(date +%s.%N) # time end
DIFF=$(echo "$END - $START" | bc) #time span
echo -e "dc=" $dc "\tmapred with hdfs time is:\t" $DIFF
#echo $counter


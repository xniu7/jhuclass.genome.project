#!/bin/bash

export "dc=$1" #environment needed by python script

# path config
data_dir="/home/hduser/data/mapred"
input=$data_dir/genome_input
output=$data_dir/genome_output
rec_file=$data_dir/genome_rec
temp_file=$data_dir/geome_temp
code_dir="/home/hduser/code/mapred"

cat $2 > $input # copy given data to input

./preproc.py <  $input  >  $rec_file # preprocessing data

START=$(date +%s.%N) # time start

max_name=0 total_size=1 counter=0

# if names are not unique, continue
until [ $max_name -eq $total_size ]; do
   # first mapred job
   cat $rec_file | $code_dir/mapper.py |sort -n | $code_dir/reducer.py > $temp_file
   # second mapred job
   cat $temp_file | $code_dir/mapper2.py | sort -n | $code_dir/reducer2.py > $rec_file
   
   max_name=$(awk 'NR==1 {print $1}' $rec_file) #get max_name from first line
   total_size=$(awk 'NR==2 {print $1}' $rec_file) #get total_size from second line

   let counter+=1 #recursive deepth
done

# get SA from names
cat $rec_file | $code_dir/getSA.py $counter > $output 

END=$(date +%s.%N) # time end
DIFF=$(echo "$END - $START" | bc) # time span
echo -e "dc=" $dc "\tmapred without hdfs time is:\t" $DIFF
#echo $counter

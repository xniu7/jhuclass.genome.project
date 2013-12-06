#!/bin/bash

export "dc=$1"

data_dir="/home/nx/Documents/classes/genomic/project/data/mapred"
input=$data_dir/genome_input
output=$data_dir/genome_output
rec_file=$data_dir/genome_rec
temp_file=$data_dir/geome_temp
code_dir="/home/nx/Documents/classes/genomic/project/code/mapred"

cat $2 > $input

./preproc.py <  $input  >  $rec_file

max_name=0 total_size=1 counter=0

until [ $max_name -eq $total_size ]; do

   cat $rec_file | $code_dir/mapper.py |sort -n | $code_dir/reducer.py > $temp_file
   cat $temp_file | $code_dir/mapper2.py | sort -n | $code_dir/reducer2.py > $rec_file
   
   max_name=$(awk 'NR==1 {print $1}' $rec_file)
   total_size=$(awk 'NR==2 {print $1}' $rec_file)

   let counter+=1
done

cat $rec_file | $code_dir/getSA.py $counter > $output
#echo $counter

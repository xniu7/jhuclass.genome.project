In mapred dir, we have two run.sh:
* ```./hadoop_run.sh 3 ~/data/sample . . /user/hduser ~/hadoop/contrib/streaming/hadoop-*streaming*.jar``` run mapreduce on hdfs
* ```./nohadoop_run.sh 3 ~/data/sample . .``` run mapreduce like job on local file system

Args:
* the first arg is the number of dc, for example, dc=3 means div is 3
* the second arg is the genome reference file
* the third arg is the mapred code dir
* the fourth arg is the output file dir (dir should be created before)
* the fifth arg is the dfs dir (dfs only)
* the sixth arg is th hadoop streaming jar (dfs only)

Format of genome reference file
* fasta file. file name should end with the .fa
* genome file. other file names, in this file, there is only one line with dna sequence. 

Important: ```chmod +x *.py```

In mapred dir, we have two run.sh:
* ```./hadoop_run.sh 3 ../sample/10 /home/hduser/code/mapred /home/hduser/data/mapred /user/hduser ~/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar``` run mapreduce on hdfs
* ```./nohadoop_run.sh 3 ../sample/10 . .``` run mapreduce like job on local file system

Args: (notice that in hdfs, arg 3 and arg 4 should be absolut path)
* the first arg is the number of dc, for example, dc=3 means div is 3
* the second arg is the genome reference file
* the third arg is the mapred code dir 
* the fourth arg is the output file dir (dir should be created before)
* the fifth arg is the dfs dir (dfs only)
* the sixth arg is th hadoop streaming jar (dfs only)

Format of genome reference file
* the file should contain only one line sequence with a,c,g,t,n characters
* if input is fasta file. use fasta2sequence tool first in ```../tool/fasta2sequence.py``` 

sh ~/code/genome/delete.sh
~/hadoop/bin/hadoop jar ~/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -cmdenv totalsize=11 -mapper ~/code/genome/mapper.py -reducer ~/code/genome/reducer.py -input /user/hduser/genome_input -output /user/hduser/genome_output_tmp1
~/hadoop/bin/hadoop jar ~/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -mapper ~/code/genome/mapper2.py -reducer ~/code/genome/reducer2.py -input /user/hduser/genome_output_tmp1 -output /user/hduser/genome_output -jobconf mapred.reduce.tasks=1

* ```./genTestSample.sh``` generating random dna sequence in ../sample

* Important: (make sure you have hadoop environment and config the right path in dc3_pdc3_hadoop.sh) ```./dc3_pdc3_hadoop.sh ../sample/10``` run comparision test of dc3 vs pdc3 vs mapreduce. if no arg : the test will run on sample data from 10 to 100000(can be changed), if given a specific sequence path, the test will run on the sepecific data. the result is saved in ```res_dc_pdc_hd.txt```

* Important: (make sure you have hadoop environment and config the right path in hadoop_nohadoop.sh) ```./hadoop_nohadoop.sh ../sample/10``` run comparision test of mapreduce job on hdfs with mapreduce like job on local file system. if no arg : the test will run on sample data from 10 to 100000(can be changed), if given a specific sequence path, the test will run on the sepecific data. the result is saved in ```res_hd_nohd.txt```

* ```./seq_mul_thread.sh ../sample/10``` run comparision test of pdc3 with different run types. if no arg : the test will run on sample data from 10 to 100000(can be changed), if given a specific sequence path, the test will run on the sepecific data. the result is saved in ```res_seq_mul_th.txt```

* ```./python_parallel.sh``` run comparision test of different python parallel libraries. the result is saved in ```res_py_pa.txt```

* ```./test-sample-all.sh``` run all test on sample sequences. sequence length from 10 to 100000, you may increase the length by change ```large_sample=100000``` in ```dc3_pdc3_hadoop.sh```, ```hadoop_nohadoop.sh``` and ```seq_mul_thread.sh```

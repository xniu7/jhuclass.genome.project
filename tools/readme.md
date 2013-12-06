Two executable python script: ```chmod +x *.py```

```./genData.py 1000 > ./1000.txt``` generate 1000 random nt sequence, save in 1000.txt. The output has only one line with a nt sequence.

```./test_parallel.py 10 1000000 4```  test python parallel speed by different libraries. 
* First arg is thread_num, second arg is length of a sequence, third arg is the computation exponent (2 means x^2, 3 means x^3). 
* The output has three lines, sequential time means run with out threading, multiprocess means run with multiprocess library, threading means run with threading library

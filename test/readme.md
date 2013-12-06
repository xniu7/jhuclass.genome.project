```./test_parallel.py 10 1000000 4```  test python parallel speed by different libraries. 
* First arg is thread_num, second arg is length of a sequence, third arg is the computation exponent (2 means x^2, 3 means x^3). 
* The output has three lines, sequential time means run with out threading, multiprocess means run with multiprocess library, threading means run with threading library

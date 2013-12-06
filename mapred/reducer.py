#!/usr/bin/env python

import sys
import os

# load file and output
def load_output():
    
    current_seg = None #current segment
    name=0             #current name

    # input comes from STDIN
    for line in sys.stdin:
        
        # remove leading and trailing whitespace
        line = line.strip()
        # parse the input we got from mapper.py
        segment, pos = line.split('\t')
        # same segments have same name. 
        if not current_seg or current_seg!=segment: 
        	name += 1
        	current_seg=segment
        # output
        ''' 10	1   25
            7	2   43
            1   3   49
            ...
        '''
        print '%s\t%s\t%s' % (pos,name,segment)

if __name__=="__main__":
    load_output()

#!/usr/bin/env python

import sys

''' 0	0   4
    1	3   8
    2   6   7
'''
# read file
def load():
    readlist = []
    max_name = 0
    # input comes from STDIN
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # parse the input we got from mapper.py
        l_pos, g_pos, name  = line.split('\t')
        # convert count (currently a string) to int
        if max_name < int(name): max_name = int(name)
        readlist.append(name)
    return readlist,max_name

''' 9
    11
    4 8 7 5 3 3 2 1 9 9 6
'''
# output with our file format for recursive computation
def output(readlist, max_name):
    print max_name
    print len(readlist)
    print ' '.join(readlist)

if __name__=="__main__":
    readlist, max_name = load()
    output(readlist, max_name)




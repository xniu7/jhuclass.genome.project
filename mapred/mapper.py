#!/usr/bin/env python
import os
import sys
import math

#change the number of segement, default is 3
dc = int(os.environ["dc"]) if os.environ.get("dc") else 3

#read file, get max_name, dna sequence
def load():
    line_num = 0
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        read = line.strip()
        if line_num==0:
            max_name = int(read)
        # sequence start from the third line
        if line_num>1:            
            readlist = read.split(' ')
        # increase counters
        line_num+=1
    return readlist,max_name

''' for dna "cattattagga"
    segment is cat att tta ...
               214 144 441
    in case 1114 we do not kown if it is 11,1,4 or 1,11,4
    we get a value of each segment, for example:
        214 ==> 2*5*5+1*5+4*0, this value is unique
'''
def getValue(pos,readlist,max_name):
    value = 0
    for i in xrange(dc):
        if i+pos < len(readlist) :
            value += int(math.pow(max_name,dc-1-i))*int(readlist[i+pos])
    return value

''' 214 0        59 0
    144 1  ==>   49 1 
    441 2       121 2
    ...         ...
'''
def output(readlist,max_name):
    for pos in xrange(len(readlist)):
        value = getValue(pos,readlist,max_name)
        print '%s\t%s' % (value, pos)

if __name__=="__main__":
    readlist,max_name = load()
    assert len(readlist)>0
    assert max_name>0
    output(readlist,max_name)

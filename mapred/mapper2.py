#!/usr/bin/env python

import sys
import os

#change the number of segement, default is 3
dc = int(os.environ["dc"]) if os.environ.get("dc") else 3


''' i = 0,1,2, dc=3
    n0=0
    n1=(total_size+2)/3
    n2=(total_size+1)/3
'''
# initiate gap. if dc==3, size=11: gap = [0,4,4]
def initGap(total_size,i):
    if i==0: return 0
    else   : return (total_size+dc-i)/dc

''' if dc==3:
    10  1       gap[10%3]+10/3=4+3=7
    7   2   ==> gap[ 7%3]+ 7/3=4+2=6
    ...
'''
# old position ==> new position
def transform(pos,total_size):
    # if dc==3, size=11: gap = [0,4,4]
    gap = [ initGap(total_size,i) for i in xrange(dc)]
    # accumulation: new_gap =[0,4,8]
    for i in xrange(1,len(gap)):
        gap[i] = gap[i]+gap[i-1]

    # if pos==10 return gap[10%3]+10/3=4+3=7
    return gap[pos%dc]+pos/dc

''' 10  1
    7   2
    1   3
    ...
'''
# read file
def load():
    read_list = []
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into words
        strs = line.split()
        global_pos=int(strs[0]);name=strs[1];
        read_list.append((global_pos,name))
    return read_list

''' 7   10  1
    6	7   2
    4   1   3
    ...
'''
# output
def output(read_list):
    for tup in read_list:
        global_pos = tup[0];name = tup[1]
        R12_pos = transform(global_pos,len(read_list))
        print '%d\t%s\t%s' % (R12_pos,global_pos,name)

if __name__=="__main__":
    read_list = load()
    assert len(read_list)>0
    output(read_list)




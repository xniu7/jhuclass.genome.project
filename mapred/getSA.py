#!/usr/bin/env python

import sys
import os

dc=int(os.environ["dc"])

''' if dc=3, size=11
    0   ==> 0
    1   ==> 4
    2   ==> 4
'''
def mapping(total_size,i):
    if i==0: return 0
    else   : return (total_size+dc-i)/dc

''' restore position recursively
    pos     rec_times
    9       2
    3       1
    1       0
'''
def trans(pos_i,rec_times,gap):
    if rec_times==0: return pos_i
    else :
	pos_j=gap[pos_i%dc]+pos_i/dc
	return trans(pos_j,rec_times-1,gap)
    
# get last mapred output file
def load():
    line_num=0
    for line in sys.stdin:
        if line_num>1:
            read = line.strip()
            readlist = read.split(' ')
        line_num+=1
    return readlist

# transform the mapred output result to name array
def getName(readlist,rec_times):
    size = len(readlist)
    gap = [ mapping(size,i) for i in xrange(dc)]
    for i in xrange(1,len(gap)):
        gap[i] = gap[i]+gap[i-1]
    namelist=[]
    for pos_i in xrange(size):
        pos_j = trans(pos_i,rec_times,gap)
        namelist.append(int(readlist[pos_j]))
    return namelist
       
'''       0 ,1, 2,3,4, 5,6,7,8,9,10
     Name:5 ,4,11,9,3,10,8,2,7,6,1
          0 ,1,2 ,3,4,5 ,6,7,8,9,10 
     SA  :10,7,4 ,1,0,9 ,8,6,3,5,2
'''
# SA[Name[pos]-1]=pos
def name2SA(namelist):
    SA = [None for i in xrange(len(namelist))]
    for pos in xrange(len(namelist)):
        name = namelist[pos]
        SA[name-1]=pos    
    return SA

def getSA():
    assert len(sys.argv)>1
    rec_times=int(sys.argv[1])
    readlist = load()
    namelist = getName(readlist,rec_times)
    SA = name2SA(namelist)
    return SA

if __name__=="__main__":
    print getSA()

#!/usr/bin/env python
import sys
import getter
import merger
from operator import itemgetter
import re
import time
import radixSort
import gc

def dna2int(dna):
   if   dna =='a' or dna=='A': return 1   
   elif dna =='c' or dna=='C': return 2
   elif dna =='g' or dna=='G': return 3
   elif dna =='n' or dna=='N': return 4
   elif dna =='t' or dna=='T': return 5

''' format dna:
    capitalize dna
    delete all characters beyond number and letter
    "dna"=>[d,n,a]
'''
def dnaFormat(dna):
    # capitalize dna
    dna = dna.upper()
    # delete all characters beyond number and letter
    dna_re = re.compile('\W')
    dna = dna_re.sub('',dna)
    # "dna"=>[d,n,a]
    dna = [dna2int(t) for t in dna]
    #dna = [t for t in dna]
    return dna

# parallel DC3
def pDC3(T,append_len,threadNum,runType,deep):
    # recursive time
    deep += 1
    # [2,1,4,4,1,4,4,1,3,3,1,0,0,0],in case [1,0,0] is missed
    for i in xrange(append_len): T.append(0)
    # algo<line 1> S:[([1,4,4],1),...,([1,0,0],10),([0,0,0],11),([0],13)]
    S = getter.getS(T,threadNum,runType)    
    # algo<line 2> sort S by item(0), S:[([0],13),([0,0,0],11),...,([4,4,1],5)]
    S=sorted(S, key=itemgetter(0))
    # algo<line 3> name(S)
    ''' P=[(name,pos)],     P:[(1,13),...,(4,7),(5,1),(5,4)...,(7,2),(7,5)]
        max_name=7,     names:  1    ,..., 4   , 5   , 5   ..., 7   , 7 
    '''
    P,max_name = getter.getP(S)
    # algo<line 4> if names in P are not unique
    if max_name <len(P):
        # algo<line 5> sort P (1,4,7,...,2,5,8),P:[(5,1),(5,4),...,(6,8),(2,11)]
        P=sorted(P, key=lambda p: (p[1]%3,p[1]/3))
        # algo<line 6> recursively compute pDC3([5,5,4,3,1,7,7,6,2])
        SA12 = pDC3([pair[0] for pair in P],append_len,threadNum,runType,deep)
        # algo<line 7>
        ''' P[4]=(1,13),P[8]=(2,11),P[3]=(3,10)...
            SA12   :[ 4    , 8    , 3    , 2   , 1   , 0,7,6,5 ]
            P[SA12]:[(1,13),(2,11),(3,10),(4,7),(5,4),(5,1),...]
            newP   :[(1,13),(2,11),(3,10),(4,7),(5,4),(6,1),...]
        '''
        P = getter.getUniqueP(P,SA12,threadNum,runType)
        #P = [(j+1,P[SA12[j]][1]) for j in xrange(len(SA12))]
    # algo<line 8> permute P (1,2,4,5,...), P:[(6,1),(9,2),(5,4),...,(1,13)]
    #P=sorted(P, key=itemgetter(1))
    P = radixSort.sort(P, 1)
    # algo<line 9,10,11> get S0,S1,S2.
    ''' S0:[(T[i],T[i+1],c1    ,c2,i),...] i%3==0; (c1,i+1),(c2,i+2) in P
        S0:[(m   ,i     ,6     ,9 ,0),...] i  = 0; (6 ,0+1),(9 ,0+2) in P
        S0:[(s   ,i     ,5     ,8 ,3),...] i  = 3; (5 ,3+1),(8 ,3+2) in P
        
        S1:[(c0  ,T[i]  ,       c1,i),...] i%3==1; (c0,i  ),(c1,i+1) in P
        S1:[(6   ,i     ,       9 ,1),...] i  = 1; (6 ,1  ),(9 ,1+1) in P

        S2:[(c0  ,T[i]  ,T[i+2],c2,i),...] i%3==2; (c0,i  ),(c2,i+2) in P
        S2:[(9   ,s     ,s     ,5 ,2),...] i  = 2; (9 ,2  ),(5 ,2+2) in P
    '''
    S0,S1,S2 = getter.getS012(T,P,threadNum,runType)
    # algo<line 12> merge S0, S1, S2 by comparison function
    ''' s12 in (S1 or S2), s0 in S0, s1 in S1, s2 in S2
            s12     <=   s12'       : if  c0             <= c0'
        (6,i,  9,1) < (9,s,s,5,2)   :     6              <  9
            s0      <=   s0'        : if (T[i],c1)       <=(T[i'],c1')
        (m,i,6,9,0) < (s,i,5,8,3)   :    (m   ,6 )       < (s    ,5  )
            s0      <=   s1'        : if (T[i],c1)       <=(T[i'],c1')
        (m,i,6,9,0) > (6,i,  9,1)   :    (m   ,6)        > (i    ,9  )
            s0      <=   s2'        : if (T[i],T[i+1],c2)<=(T[i'],T[i'+1],c2')
        (s,i,5,8,3) < (9,s,s,5,2)   :    (s   ,i     ,8) < (s    ,s      ,5  )
    '''
    # SA=[11, 10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
    SA=merger.merge(S0,S1,S2)
    # pop appendix [11,10,7,4,...] => [10,7,4,...]
    while(len(SA)>(len(T)-append_len)):SA.pop(0)
    return SA                

if __name__ == "__main__":
    assert len(sys.argv)>2
    threadNum = int(sys.argv[1])
    assert threadNum>0
    runType = sys.argv[2] # 'simple','multiproc','threadpool'
    assert runType=='sequential' or runType=='multiproc' or runType=='threadpool'
    if runType=='sequential':threadNum=1
    append_len = 3   # the number of zeros append in the end of dna
    dna = sys.stdin.readline()   # get dna string
    dna = dnaFormat(dna)    # format dna
    t1=time.time()
    # get suffix array by pDC3 algo
    SA = pDC3(dna,append_len,threadNum,runType,0)
    t2=time.time()
    # output
    #print SA
    print "run %s time with %s thread:\t%s" % (runType,threadNum,t2-t1)
    
    # in case threadpool throw interpreter shutdown warning
    sys.stdout.close()

import sys
import threading
from multiprocessing import Pool
import time
import math

# get threadNum, pos_num and exponent from command line
assert len(sys.argv)>3
threadNum=int(sys.argv[1])
pos_num=int(sys.argv[2])
exponent=int(sys.argv[3])
assert threadNum>0 and pos_num>0 and exponent>0

# computation is more complex with higher exponent
def f(pos):
     return int(math.pow(pos,exponent))

# allocate computation process to threads
def f_pool(start):
    S=[]
    for pos in xrange(start,pos_num,threadNum):
        S.append(f(pos))
    return S

# sequential computation class
class MySimple:
    def getSimple(self):
        S=[[] for i in xrange(threadNum)]
        for pos in xrange(pos_num):
            mod = pos%threadNum
            S[mod].append(f(pos))
        return S

# multiprocess computation class
class MyPool:
    def getPool(self):
        pool = Pool(processes=threadNum)
        S = pool.map(f_pool, xrange(threadNum))
        return S

# threading computation class
class MyThread(threading.Thread):
    def __init__(self,id,pos_range,S):
        threading.Thread.__init__(self)
        self.id=id
        self.S=S
        self.pos_range=pos_range

    def run(self):
        for pos in self.pos_range:
            self.S[self.id].append(f(pos))

# sequential test
def testSimple():
    t1 = time.time()
    mySimple = MySimple()
    S = mySimple.getSimple()
    t2 = time.time()
    #print S
    return t2-t1

# multiprocessing test
def testPool():
    t1 = time.time()
    myPool = MyPool()
    S = myPool.getPool()
    t2 = time.time()
    #print S
    return t2-t1

# threading test
def testThread():
    t1=time.time()
    S=[[] for i in xrange(threadNum)]
    threads = []    
    for i in xrange(threadNum):
        threads.append(MyThread(i,xrange(i,pos_num,threadNum),S))
    [t.start() for t in threads]
    [t.join() for t in threads]
    t2=time.time()
    #print S
    return t2-t1

if __name__=="__main__":
    print "sequential time:\t%s" % testSimple()
    print "multiprocess time:\t%s" % testPool()
    print "threading time: \t%s" % testThread()

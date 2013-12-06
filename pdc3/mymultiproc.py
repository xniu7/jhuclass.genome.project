from multiprocessing import Pool

def unwrap_self_getS(arg, **kwarg):
    return GetS.threadFunc(*arg, **kwarg)

def unwrap_self_getS012(arg, **kwarg):
    return GetS012.threadFunc(*arg, **kwarg)

def unwrap_self_getUniqueP(arg, **kwarg):
    return GetUniqueP.threadFunc(*arg, **kwarg)

class GetS:
    def __init__(self,T,threadNum):
        self.T = T
        self.threadNum = threadNum
        
    def threadFunc(self,pos):
        if pos%3!=0:
            return (self.T[pos:pos+3],pos)
    
    def get(self):
        pool = Pool(processes=self.threadNum)
        pos_range=[]
        for t in xrange(len(self.T)): 
            if t%3!=0: pos_range.append(t)
        S = pool.map(unwrap_self_getS, zip([self]*len(pos_range),pos_range))
        return S
    
class GetS012():
    def __init__(self,T,P,threadNum):
        self.T = T
        self.P = P
        self.pos_range_01=[]
        self.pos_range_2 =[]
        self.div = 3
        for p in xrange(1,len(self.P)): 
            if self.P[p-1][1]%3==1: self.pos_range_01.append(p)
            else                  : self.pos_range_2 .append(p)
        self.threadNum = threadNum
    
    def get(self):
        assert self.div==3
        pool = Pool(processes=self.threadNum)
        S = pool.map(unwrap_self_getS012, zip([self]*self.div,xrange(self.div)))
        return S[0],S[1],S[2]

    def threadFunc(self,mod):
        S=[]        
        if   mod==0:
            for i in xrange(len(self.pos_range_01)):
                pos = self.pos_range_01[i]
                S.append(self.s0(pos))
        elif mod==1:
            for i in xrange(len(self.pos_range_01)):
                pos = self.pos_range_01[i]
                S.append(self.s1(pos))
        elif mod==2:
            for i in xrange(len(self.pos_range_2 )):
                pos = self.pos_range_2 [i]
                S.append(self.s2(pos))
        return S
    
    def s0(self,pos):
        assert pos>0 and self.P[pos-1][1]%3==1
        i0 = self.P[pos-1][1]-1
        s0=(self.T[i0],self.T[i0+1],self.P[pos-1][0],self.P[pos][0],i0)
        return s0

    def s1(self,pos):
        assert pos>0 and self.P[pos-1][1]%3==1
        i1 = self.P[pos-1][1]
        s1=(self.P[pos-1][0],self.T[i1],self.P[pos][0],i1)
        return s1
    
    def s2(self,pos):
        assert pos>0 and self.P[pos-1][1]%3==2
        i2 = self.P[pos-1][1]
        s2=(self.P[pos-1][0],self.T[i2],self.T[i2+1],self.P[pos][0],i2)
        return s2
    
class GetUniqueP():
    def __init__(self,P,SA12,threadNum):
        self.P = P
        self.SA12 = SA12
        self.threadNum = threadNum
        self.uniqueP = []
        
    def get(self):
        pool = Pool(processes=self.threadNum)
        pos_range=[]
        for pos in xrange(len(self.SA12)): 
            pos_range.append(pos)
        uniqueP = pool.map(unwrap_self_getUniqueP, zip([self]*len(pos_range),pos_range))
        return uniqueP
    
    def threadFunc(self,SA12_pos):
        unique_name = SA12_pos+1
        P_pos= self.SA12[SA12_pos]
        return (unique_name,self.P[P_pos][1])

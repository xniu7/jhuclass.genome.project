import threadpool

class GetS:
    def __init__(self,T,threadNum):
        self.T = T
        self.threadNum = threadNum
        self.S = []

    def get(self):
        pool = threadpool.ThreadPool(self.threadNum)
        reqs = threadpool.makeRequests(self.threadFunc,xrange(len(self.T)))
        [pool.putRequest(req) for req in reqs]
        pool.wait()
        return self.S

    def threadFunc(self,pos):
        if pos%3!=0:
            self.S.append((self.T[pos:pos+3],pos))

class GetS012():
    def __init__(self,T,P,threadNum):
        self.T = T
        self.P = P
        self.S0,self.S1,self.S2 = [],[],[]
        self.threadNum = threadNum

    def get(self):
        pool = threadpool.ThreadPool(self.threadNum)
        reqs = threadpool.makeRequests(self.threadFunc,xrange(1,len(self.P)))
        [pool.putRequest(req) for req in reqs]
        pool.wait()
        return self.S0,self.S1,self.S2
    
    def threadFunc(self,pos):
        assert pos>0
        if self.P[pos-1][1]%3==1:
            i0 = self.P[pos-1][1]-1
            self.S0.append((self.T[i0],self.T[i0+1],self.P[pos-1][0],self.P[pos][0],i0))
            i1 = self.P[pos-1][1]
            self.S1.append((self.P[pos-1][0],self.T[i1],self.P[pos][0],i1))
        elif self.P[pos-1][1]%3==2:
            i2 = self.P[pos-1][1]
            self.S2.append((self.P[pos-1][0],self.T[i2],self.T[i2+1],self.P[pos][0],i2))

class GetUniqueP():
    def __init__(self,P,SA12,threadNum):
        self.P = P
        self.SA12 = SA12
        self.threadNum = threadNum
        self.uniqueP = []

    def get(self):
        pool = threadpool.ThreadPool(self.threadNum)
        reqs = threadpool.makeRequests(self.threadFunc,xrange(len(self.SA12)))
        [pool.putRequest(req) for req in reqs]
        pool.wait()
        return self.uniqueP

    def threadFunc(self,SA12_pos):
        unique_name = SA12_pos+1
        P_pos= self.SA12[SA12_pos]
        self.uniqueP.append((unique_name,self.P[P_pos][1]))

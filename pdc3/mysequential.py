class GetS:
    def __init__(self,T,_):
        self.T = T
        
    def simpleFunc(self,pos):
        if pos%3!=0:
            return (self.T[pos:pos+3],pos)
    
    def get(self):
        S=[]
        for pos in xrange(len(self.T)):
            if pos%3!=0:
                S.append(self.simpleFunc(pos))
        return S
    
class GetS012():
    def __init__(self,T,P,_):
        self.T = T
        self.P = P
    
    def get(self):
        S0,S1,S2=[],[],[]
        for pos in xrange(1,len(self.P)):
             self.simpleFunc(pos,S0,S1,S2)
        return S0,S1,S2

    def simpleFunc(self,pos,S0,S1,S2):
        assert pos>0
        if self.P[pos-1][1]%3==1:
            i0 = self.P[pos-1][1]-1
            S0.append((self.T[i0],self.T[i0+1],self.P[pos-1][0],self.P[pos][0],i0))
            i1 = self.P[pos-1][1]
            S1.append((self.P[pos-1][0],self.T[i1],self.P[pos][0],i1))
        elif self.P[pos-1][1]%3==2:
            i2 = self.P[pos-1][1]
            S2.append((self.P[pos-1][0],self.T[i2],self.T[i2+1],self.P[pos][0],i2))
    
class GetUniqueP():
    def __init__(self,P,SA12,_):
        self.P = P
        self.SA12 = SA12
        self.uniqueP = []
        
    def get(self):
        for pos in xrange(len(self.SA12)):
            self.simpleFunc(pos)
        return self.uniqueP

    def simpleFunc(self,SA12_pos):
        unique_name = SA12_pos+1
        P_pos= self.SA12[SA12_pos]
        self.uniqueP.append((unique_name,self.P[P_pos][1]))

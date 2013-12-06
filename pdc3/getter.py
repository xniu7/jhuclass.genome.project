import mysequential
import mythreadpool
import mymultiproc

# all of my simple, mythreadpool, mymultiproc
# implement the function GetS(),GetUniqueP(),GetS012()
# we use this file to choose the run type

# get S by 3 different types
def getS(T,threadNum,runType):
    if runType=='sequential': threadGetS = mysequential.GetS(T,threadNum)
    elif runType=='threadpool': threadGetS = mythreadpool.GetS(T,threadNum)
    elif runType=='multiproc': threadGetS = mymultiproc.GetS(T,threadNum)
    S = threadGetS.get()    
    return S

# get P only in sequential way
def getP(S):
    P=[]
    name=0
    for i in xrange(len(S)):
        if i==0:
            current_t3=S[i][0]
            name+=1
        elif current_t3!=S[i][0]:
            current_t3=S[i][0]
            name+=1
        P.append((name,S[i][1]))
    return P,name

# get unique P by 3 different types
def getUniqueP(P,SA12,threadNum,runType):
    if runType=='sequential': threadGetUniP = mysequential.GetUniqueP(P,SA12,threadNum)
    elif runType=='threadpool': threadGetUniP = mythreadpool.GetUniqueP(P,SA12,threadNum)
    elif runType=='multiproc': threadGetUniP = mymultiproc.GetUniqueP(P,SA12,threadNum)
    P = threadGetUniP.get()
    return P

# get S0,S1,S2 by 3 different types
def getS012(T,P,threadNum,runType):
    if runType=='sequential': threadGetS012 = mysequential.GetS012(T,P,threadNum)
    elif runType=='threadpool': threadGetS012 = mythreadpool.GetS012(T,P,threadNum)
    elif runType=='multiproc': threadGetS012 = mymultiproc.GetS012(T,P,threadNum)
    S0,S1,S2 = threadGetS012.get()
    return S0,S1,S2

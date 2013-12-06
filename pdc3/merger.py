from operator import itemgetter

# compare (a1,a2) with (b1,b2)
def leq(a1,a2,b1,b2):
   return a1<b1 or ( a1==b1 and a2<=b2)

# compare (a1,a2,a3) with (b1,b2,b3)
def leq3(a1,a2,a3,b1,b2,b3):
   return (a1<b1 or (a1==b1 and leq(a2,a3,b2,b3)))

# pop S, and get the last element of poped tuple
def pop(S):
   s = S.pop(0)
   return s[len(s)-1] 

# step1 sort S0,S1,S2 seperately
# step2 compare the smallest element of S0 with that of S1 and S2
# step3 pick the smallest one, continue step 2 until no element left 
def merge(S0,S1,S2):
    SA=[]

    S0=sorted(S0, key =itemgetter(0,2))
    S1=sorted(S1, key =itemgetter(0))
    S2=sorted(S2, key =itemgetter(0))
    while S0 or S1 or S2:
        if S0 and ((S1 and not S2) or ((S1 and S2) and S1[0][0]<S2[0][0])):
            if leq(S0[0][0],S0[0][2],S1[0][1],S1[0][2]):
                SA.append(pop(S0))
            else:
                SA.append(pop(S1))
        elif S0 and ((not S1 and S2) or ((S1 and S2) and (S1[0][0]>=S2[0][0]))):
            if leq3(S0[0][0],S0[0][1],S0[0][3],S2[0][1],S2[0][2],S2[0][3]):
                SA.append(pop(S0))
            else:
                SA.append(pop(S2))
        elif not S0 and S1 and S2:
            if S1[0][0]<S2[0][0]:
                SA.append(pop(S1))
            else:
                SA.append(pop(S2))
        else:
            if   S0: SA.append(pop(S0))
            elif S1: SA.append(pop(S1))
            elif S2: SA.append(pop(S2))
    return SA

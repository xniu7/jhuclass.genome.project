import sys
import time

def leq(a1,a2,b1,b2):
   return a1<b1 or ( a1==b1 and a2<=b2)

def leq3(a1,a2,a3,b1,b2,b3):
   return (a1<b1 or (a1==b1 and leq(a2,a3,b2,b3)))

def radixPass(a,b,r,n,K):
   c = [0 for i in xrange(K+1)]
   for i in xrange(n): c[r[a[i]]]+=1   
   for i in xrange(K+1): 
      if i==0: sum=0
      t = c[i]; c[i] = sum; sum += t   
   for i in xrange(n):      
      b[c[r[a[i]]]] = a[i]
      c[r[a[i]]]+=1

def GetI(SA12t,n0):
   return SA12t * 3 + 1 if SA12t < n0 else (SA12t - n0) * 3 + 2

def suffixArray(s, SA, n, K):
   n0,n1,n2=(n+2)/3,(n+1)/3,n/3
   n02=n0+n2
   
   s12 = getS12(n,n0,n1,n02)
   SA12 = radixRank(s12,s,n02,K)
#   print SA12
   s12,SA12 = getS12Rank(n0,n02,s,s12,SA12)
   
#   print s12,SA12
   s0=getS0(n0,n02,SA12)
   SA0=getSA0(s0,n0,s,K)
   
   merge(n,n0,n1,n02,SA12,SA0,SA,s,s12)

def getS12(n,n0,n1,n02):
   s12 = []
   for i in xrange(n+(n0-n1)):
      if i%3!=0 : s12.append(i)        
   while(len(s12)<n02+3) : s12.append(0)
   return s12

def getS12Rank(n0,n02,s,s12,SA12):
   name=0
   c0,c1,c2 = -1,-1,-1
   for i in xrange(n02):
      if s[SA12[i]] != c0 or s[SA12[i]+1] != c1 or s[SA12[i]+2] != c2 :
         name+=1
         c0,c1,c2 = s[SA12[i]], s[SA12[i]+1], s[SA12[i]+2]
      if SA12[i] % 3 == 1: s12[SA12[i]/3]      = name
      else               : s12[SA12[i]/3 + n0] = name
      
   if name<n02 :
      suffixArray(s12, SA12, n02, name)
      for i in xrange(n02) : s12[SA12[i]] = i + 1
   else :
      for i in xrange(n02) : SA12[s12[i] - 1] = i
   return s12,SA12

   
   
def radixRank(s12,s,n02,K):
   SA12 = [0 for i in xrange(n02+3)]
   radixPass(s12 , SA12, s[2:], n02, K)
   radixPass(SA12, s12,  s[1:], n02, K)
   radixPass(s12 , SA12, s    , n02, K)
   return SA12

def getSA0(s0,n0,s,K):   
   SA0 = [0 for i in xrange(n0)]
   radixPass(s0, SA0, s, n0, K)
   return SA0

def getS0(n0,n02,SA12):
   s0 = [0 for i in xrange(n0)]
   for i in  xrange(n02):
      if i==0: j=0
      if (SA12[i] < n0) :         
         s0[j] = 3*SA12[i]
         j+=1
   return s0
         
def merge(n,n0,n1,n02,SA12,SA0,SA,s,s12):
   k=0
   while(k<n):
      if k==0: p=0; t=n0-n1
      i = GetI(SA12[t],n0)
      j = SA0[p]
      if leq(s[i], s12[SA12[t] + n0], s[j], s12[j/3]) if SA12[t]<n0 else leq3(s[i],s[i+1],s12[SA12[t]-n0+1], s[j],s[j+1],s12[j/3+n0]):
         SA[k] = i; t+=1
         if t==n02:
            while(p<n0):
               k+=1
               SA[k] = SA0[p]
               p+=1    
      else    :
         SA[k] = j; p+=1
         if p==n0:
            while(t<n02):
               k+=1
               SA[k] = GetI(SA12[t],n0)
               t+=1              
      k+=1

def dna2int(dna):
   if   dna =='a' or dna=='A': return 1
   elif dna =='t' or dna=='T': return 5
   elif dna =='c' or dna=='C': return 2
   elif dna =='g' or dna=='G': return 3
   elif dna =='n' or dna=='N': return 4
   

def getInput(input):
   input = [ dna2int(t) for t in input]
   input.append(0)
   input.append(0)
   input.append(0)
   return input

#input= [2,1,4,4,1,4,4,1,3,3,1,0,0,0]
#input= [3,3,2,1,5,5,4,0,0,0]
input = sys.stdin.read().rstrip()
n=len(input)
input = getInput(input)
SA = [0 for i in xrange(n)]
K=5
t1=time.time()
suffixArray(input,SA,n,K)
t2=time.time()
print SA
print t2-t1

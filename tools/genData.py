#!/usr/bin/env python
import sys
import random

# randomly generate a dna string with given length
def genDNA(length):
   dna=[]
   for i in xrange(length):
      rand = random.randint(0,4)
      if rand ==0 : dna.append('A')
      if rand ==1 : dna.append('C')
      if rand ==2 : dna.append('G')
      if rand ==3 : dna.append('T')
      if rand ==4 : dna.append('N')
   return dna

if __name__=="__main__":
   assert len(sys.argv)>1
   length=int(sys.argv[1])
   assert length>0
   dna = genDNA(length)
   print ''.join(dna)

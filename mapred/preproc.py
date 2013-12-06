#!/usr/bin/env python
import sys
import re

#mapping
def dna2int(dna):
   if   dna =='a' or dna=='A': return 1   
   elif dna =='c' or dna=='C': return 2
   elif dna =='g' or dna=='G': return 3
   elif dna =='t' or dna=='T': return 4
   else: return 5

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
   return dna

# store dna in a list
def pDC3Format(dna):
   dna = dnaFormat(dna)
   # "dna"=>[d,n,a]
   dna = [dna2int(t) for t in dna]
   return dna

''' first line is the number of names
    second line is the dna length
    third line is the dna sequence
'''
def mapredFormat():
   line = sys.stdin.readline()
   dna = dnaFormat(line)
   dna = [str(dna2int(t)) for t in dna]
   print 5  # the base of dna a,c,g,t,n
   print len(dna)
   print ' '.join(dna)

if __name__=="__main__":
   mapredFormat()

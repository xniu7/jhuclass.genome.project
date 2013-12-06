#!/usr/bin/env python
import sys

def decodeFasta(fasta):
    datas = fasta.split('\n')
    res = []
    dna = ""
    for data in datas:
        if ">" in data :
            if len(dna)>0: res.append(dna)
            dna= ""
            res.append(data)
        else : dna += data
    if len(dna)>0: res.append(dna)
    return res

if __name__=="__main__":
    fasta = sys.stdin.read()
    print ''.join(decodeFasta)

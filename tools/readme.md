Two executable python script: ```chmod +x *.py```

```./genData.py 1000 > ./1000.txt``` generate 1000 random nt sequence, save in 1000.txt. The output has only one line with a nt sequence.

```./fasta2sequence.py < sample.fa > sample.txt``` concatenate all dna sequence together and delete the '>xxxx'

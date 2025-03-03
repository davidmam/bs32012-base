# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:52:37 2019

@author: Noah
"""
from Bio import SeqIO

infile = 'felissilvestris.fasta'
outfile = 'felissilvestrisnew.fasta' 
startpos = 659
sequence = SeqIO.read(infile, "fasta")
endpos = len(sequence)
print(len(sequence))
sequence = sequence[startpos-1:endpos+1] + sequence[1:startpos]
print(len(sequence))
with open(outfile, "w") as output_handle:
    SeqIO.write(sequence, output_handle, 'fasta')
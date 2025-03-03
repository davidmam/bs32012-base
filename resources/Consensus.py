# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:21:02 2019

@author: Noah
"""

filename = input('Alignment file: ') # gets the name of the alignment file
seq1 = '>' + input('Please enter your first accession no.: ') #gets the accession of the first sequence
seq2 = '>' + input('Please enter your second accession no.: ')# gets the accession of the second sequence
outfile = input('Where do you want to save the file to? ') # get the output file name
data = {'1':'', '2':''}

with open(filename, 'r') as fh: #open the alignment file and find the two sequences
    line = fh.readline()
    for f in ['1','2']:
        while line and not (line.startswith(seq1) or line.startswith(seq2)):
            line = fh.readline()
        line = fh.readline()
        while line and not line.startswith('>'):
            data[f] += line.strip()
            line = fh.readline()
with open(outfile, 'w') as fh: # reads both sequences, writing out the base when it is the same, or N where it is different.
    for base1, base2 in zip(data['1'], data['2']):
        if base1 == base2 and base1 != '-':
            print(base1,end='',file=fh)
        else:
            print('N',end='',file=fh)

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:41:16 2019

@author: Noah
"""
import glob
from os import mkdir
import sys

def getgaps(pos, ref):
    """This takes a position in the original sequence and outputs the position in the aligned sequence which includes the gaps in the count."""
    workpos = 0
    gaps = 0
    for f in ref:
        if f == '-':
            gaps += 1 #this adds 1 to the position for each gap there is in the sequence.
        else:
            workpos += 1
        if workpos == pos:
            break
    return gaps

def splitalignment(filename): #Extracts the aligned sequences from the fasta file so they can be processed.
    """this takes a fasta file containing alignments and outputs a dictionary with the accession no. as key and the sequence in string format as value."""
    sequences = {}
    seqlist = []
    with open(filename,'r') as alignment:
        for line in alignment:
            if line[0] == '>': #this means that the line is a fasta header!
                seqname = line[1:].split('/')[0].split('.')[0] #this retrieves the sequence ID without version number (the .1 at the end)
                seqlist.append(seqname.upper())
                sequences[seqname.upper()] = [] #creates a list to store the retrieved lines for this sequence ID in
            else:
                sequences[seqname.upper()].append(line.strip()) #each line is added to the list
    for f in seqlist:
        sequences[f] = ''.join(sequences[f]) #the lists are converted to strings
    return sequences

infile = 'Species_alignment.fa' # filename to process by default (if called with no arguments, ie 'python3 Convert_to_alignment.py')
if len(sys.argv) >1: # If called as 'python3 Convert_to_alignment.py filename' will read the data from filename instead of Species_alignment.fa
    infile=sys.argv[1]
    print(f'processing {infile}') 
sequences = splitalignment(infile) # get the sequences from the file
newdirect = 'gappedrestrict' # create a new folder to put the results in
mkdir(newdirect) #
extension = '.restrict' # set the extension to look for 
filelist = [f for f in glob.glob("*" + extension)] #retrieves the filenames for all files from the folder having the file extension 'extension' and stores them
files = [f[0:-(len(extension))] for f in filelist if f[0:-(len(extension))].upper() in sequences] #stores the filenames without extension in a list, ie the first part of the name so usually the accession number. Only keeps filenames that are for an accession in the sequence list read earler.

print('processing ',files)    
for file in files: # This indented block processes each file one at a time.
    print('Going through file {}'.format(file + extension))
    
    with open(file + '.restrict','r') as fhin:
        with open(newdirect + '/' + file + 'new.restrict','w') as fhout:
            linein = fhin.readline()
            while len(linein) <= 3 or linein.strip()[0]  == '#' : #this skips all the header lines and just prints them without changing anything
                print(linein, end = '', file = fhout)
                linein = fhin.readline()
            linein = '\t'.join(linein.strip().split()) #the line containing column headings is then printed in tab delimited format
            print(linein, file = fhout)
            for line in fhin: # processes the rest of the file
                if len(line) <= 3 or line.strip()[0]  == '#' : #this skips all the header/empty lines and just prints them without changing anything
                    print(line, end = '', file = fhout)
                else: #This is the data to realign. This block finds the data in the line and gets a new value for the positions and substituting this for the original position.
                    line = line.strip().split() #this splits the line into each value
                    gapcount = getgaps(int(line[0]), sequences[file.upper()])
                    for position in [0, 1, 5, 6, 7, 8]: #these are the columns containing a position in the sequence and thus need to be updated
                        if len(line) > position and line[position] != '.': #cells with no value just have a . in them, this ignores them
                            line[position] = str(int(line[position]) + gapcount) #this overwrites each position with its position in the aligned sequence
                    line = '\t'.join(line) #the newly edited line is then printed in tab delimited format
                    print(line, file = fhout)

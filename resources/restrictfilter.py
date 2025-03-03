# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:46:20 2019

@author: Chris
"""

''' Script for reading restriction sites and finding common and unique sites
    python restrictfilter.py <infile1> <infile2> <statsoutfile> <tag>
    
    produces 3 files:
        infile1.tag.filtered
        infile2.tag.filtered
        statsoutfile

'''
import sys
#set default values for input data
fileA = "AccessionA"
fileB = "AccessionB"
statsfile = 'stats.txt'
tag = ''

if len(sys.argv) > 4: # if enough values are given on the command line
    fileA = sys.argv[1]
    fileB = sys.argv[2]
    statsfile = sys.argv[3]
    tag = sys.argv[4]
    
    
def checkline(line):
    """This checks whether the line contains data or not"""
    if line.startswith('#') or line.startswith('\n') or not line:
        return False
    else:
        return True                   

fha = open(fileA) # open the files for reading (the source)
fhb = open(fileB)
ofha = open(fileA+tag+".filtered", 'w') #open new files to put the results in
ofhb = open(fileB+tag+".filtered", 'w')
ofstats = open(statsfile, 'w')
print("Enzyme",fileA, fileB, "Common", sep="\t", file=ofstats) #print header to the stats file
enzstats= {'A':{}, 'B':{}, 'C':{}} #Create a dictionary to hold the stats.

lineA = fha.readline() #read in the first line from each source file
lineB = fhb.readline()

while not checkline(lineA): #if the line is a header line, just print it out and read the next line until a non-header line is found. (first sequence)
    print(lineA, file=ofha, end='')
    lineA = fha.readline()


while not checkline(lineB): #repeat for file B
    print(lineB, file=ofhb, end='')
    lineB = fhb.readline()

print(lineA, file=ofha) #Print the column header for file A and read the next line
lineA = fha.readline()
print(lineB, file=ofhb) #Print the column header for file B and read the next line
lineB = fhb.readline()

# now we are at the start of the data.
dataA = lineA.split('\t')
dataB = lineB.split('\t')
while checkline(lineA) or checkline(lineB): # Read in the data till all data is read in
    if checkline(lineA) and checkline(lineB) and int(dataA[0]) == int(dataB[0]) : # If A and B are the same,add to the enzyme stats for the same and read a new line from both.
        enzstats['C'][dataA[3]] = enzstats['C'].get(dataA[3],0)+1
        lineA = fha.readline()
        lineB = fhb.readline()
        dataA = lineA.split('\t')
        dataB = lineB.split('\t')
    elif checkline(lineA) and (not checkline(lineB) or int(dataA[0]) < int(dataB[0])): #Finds a unique site in A. Writes to the A file and reads the next line in A
        # A is unique so save to file and move A on
        print(lineA, file=ofha, end='')
        enzstats['A'][dataA[3]] = enzstats['A'].get(dataA[3],0)+1
        lineA = fha.readline()
        dataA = lineA.split('\t')
    elif checkline(lineB): #Finds a unique site in B. Writes to the BA file and reads the next line in B
        # B is unique so save to file and move B on
        print(lineB, file=ofhb, end='')
        enzstats['B'][dataB[3]] = enzstats['B'].get(dataB[3],0)+1
        lineB = fhb.readline()
        dataB = lineB.split('\t')
#All done so close the files        
fha.close()
fhb.close()
ofha.close()
ofhb.close()

enzlist = set(list(enzstats['A'].keys())+list(enzstats['B'].keys())+list(enzstats['C'].keys()))
for e in enzlist: # organise and print the stats to the stats file
    print(e, enzstats['A'].get(e,0), enzstats['B'].get(e,0), 
          enzstats['C'].get(e,0), sep='\t', file=ofstats)

ofstats.close()        

#!/cluster/dtu/miniconda3/envs/BS32010/bin/python

from Bio import Entrez, SeqIO
import sys,os

sequence = sys.argv[1]

print('retrieving sequence ID', sequence)

Entrez.email='{}@dundee.ac.uk'.format(os.environ['USER'])

with Entrez.efetch(db='nucleotide', retmode='text', rettype='gbwithparts', id=sequence) as sh:
    seqrecord = SeqIO.read(sh, "gb")

SeqIO.write(seqrecord, open('{}.fasta'.format(seqrecord.id),'w'), 'fasta')



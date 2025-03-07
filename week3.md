# Week 3

## Targets
* A restriction enzyme map for each sequence/species which matches the curated alignment.
* A script that can identify the differences between two restriction maps
* Read and understand how [Primer3](http://primer3.sourceforge.net) works

This week continues from [Week 2](week2.md). When you have the output from your restriction map comparison script you need to turn that into an input for Primer3.

### Looking for PCR primers with Primer 3

You will have a list of candidate restriction enzyme sites (hopefully - if not we'll have to look for SNPs instead). You will need to run Primer3 to look for primer pairs around each of those sites.

Primer3 has a lot of configuration parameters. The key ones that will need to be set are:

* The background sequence in which the PCR pairs should be found.
* the region which must be included in any amplified fragment
* the minimum/maximum size of an amplified fragment
* the min/max annealing temperature (Tm) for the PCR primers.
* 
#### Primer 3 on the cluster

Primer3 has all the commands/options set in an input file which it reads from STDIN (look back at the Unix Shell lesson) and prints the results to the screen (STDOUT) so you will run it like:

```
$ primer3 < inputfile > outputfile
```

#### To add your sequence to Primer3 input file

Generate your consensus sequence with the Consensus.py script

    $ python3 ../bs32012-2023/resources/Consensus.py
    Alignment file: Species_Alignment.fa
    Please enter your first accession no.: AJ421471
    Please enter your second accession no.: KR019013
    Where do you want to save the file to? consensus.fa
    (BS32012) [dmamartin@c6420-2-4 work]$ more consensus.fa
    GTTAATGTAGCTTAATAAAAAGCAAAGCACTGAAAATGCTTAGATGAGCTTCCTNGCTCCATAAACACAAAGGTTTGGTC
    CTNGCCTTTTTATTGTTTNGTAGCAAGTTTACACATGCAAGACTCCCCTNTCCAGTGAGAATGCCCTTAATATCNNNNNN

on the login node:

* Open the example file in nano
* Find the SEQUENCE_TEMPLATE line
* move the cursor to the first base of the sequence
* Press ENTER then CTRL-K to remove the sequence
* Move the cursor back to just after the =
* read in the consensus sequence using CTRL-R. This will add it on one line.
* Ensure you have edited the other parameters correctly.
* Save the file with a new filename

* run primer3 with `primer3_core --output=outputfilename inputfile`
 
#### Example files for Primer3

To follow soon.

#### How to proceed

It is up to you to decide how to proceed with this - run each site difference as a separate file, or run it all as one big job and separate out the sites later.

Leading in to week 4 you should be:

* writing a script to generate Primer3 input files from the difference map.
* writing a script to process the primer3 output 

#### Primer 3 in Benchling

You can upload your sequence file (the consensus file) to Benchling and run Primer 3 there.
 

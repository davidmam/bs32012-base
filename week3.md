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

Primer3 has all the commands/options set in an input file which it reads from STDIN (look back at the Unix Shell lesson) and prints the results to the screen (STDOUT) so you will run it like:

```
$ primer3 < inputfile > outputfile
```
#### Example files for Primer3

To follow soon.

#### How to proceed

It is up to you to decide how to proceed with this - run each site difference as a separate file, or run it all as one big job and separate out the sites later.

Leading in to week 4 you should be:

* writing a script to generate Primer3 input files from the difference map.
* writing a script to process the primer3 output 
# Week 2

## Main targets

By the end of this week you should have:
* a curated multiple alignment of the mitochondrial sequences
* Ability to read in data from a file, manipulate it and write it out in Python. (You'll need this for curating the multiple alignment)

### Curating the multiple alignment.
When you have collected all the mitochondrial genome sequences ([week 1 target](week1.md))you will need to do the following:

1. Assess them for quality - reject any that are not complete and/or which have areas of uncertainty (multiple `N`s).
1. Perform a multiple alignment using an appropriate web service in [Jalview](http://www.jalview.org)
1. Examine the alignment. Note that Mitochondria have a *circular* genome. What impact does that have on the sequence alignment and what can you do about it?
1. Make the adjustments you need and then save that multiple alignment as your working copy.
  
Once you have a curated alignment we can run the [EMBOSS]{http://emboss.org) program `restrict` on each of the sequences from the *curated* alignment. The EMBOSS programs (and Primer 3 which we will use later) are installed on the teaching server at ts-ug.lifesci.dundee.ac.uk. This can be accessed via Xming or any SSH client from within the univeristy network. This will give us output that looks like:
```
# Program: restrict
# Rundate: Thu 14 Jan 2016 10:18:30
# Commandline: restrict
#    [-sequence] preds.fa:KP202275
# Report_format: table
# Report_file: kp202275.restrict
########################################

#=======================================
#
# Sequence: KP202275     from: 1   to: 16735
# HitCount: 9185
#
# Minimum cuts per enzyme: 1
# Maximum cuts per enzyme: 2000000000
# Minimum length of recognition site: 4
# Blunt ends allowed
# Sticky ends allowed
# DNA is linear
# Ambiguities allowed
#
#=======================================

  Start     End  Strand Enzyme_name Restriction_site 5prime 3prime 5primerev 3primerev
      2       5       + MseI        TTAA                  2      4         .         .
      9      12       + SetI        ASST                 12      8         .         .
      9      12       + CviJI       RGCY                 10     10         .         .
      9      12       + AluBI       AGCT                 10     10         .         .
     11      14       + MspJI       CNNR                 23     27         .         .
     12      15       + MseI        TTAA                 12     14         .         .
     17      20       + MspJI       CNNR                 29     33         .         .
     17      20       + FaiI        YATR                 18     18         .         .
     19      22       + FaiI        YATR                 20     20         .         .
     26      38       + SgeI        CNNGNNNNNNNNN        38     14         .         .
     26      29       + MspJI       CNNR                 38     42         .         .
     17      29       - SgeI        CNNGNNNNNNNNN        40     16         .         .
     26      29       - MspJI       CNNR                 12     16         .         .
     31      37       + TscAI       CASTGNN              37     28         .         .
     33      36       + MspJI       CNNR                 45     49         .         .
     31      35       - BtsIMutI    CAGTG                30     28         .         .
...
```

#### Other useful EMBOSS programs

`seqret` will extract sequences from a database or a file. When run with the option `-ossingle` it will write each of the retrieved sequences to a separate file. You get more information on any EMBOSS program with the options `-help` and `-verbose`.


### Dealing with the output from `restrict`

The output from restrict is quite challenging to deal with. Reading it into a program is straightforward as it is a simple table. The challenge arises from two things:

1. EMBOSS strips all the gaps out of the sequences before it runs restrict so the *Start* and *End* columns refer to an ungapped sequence.
2. Our alignment has gaps in (not many though there are some). You will have to correct for the gaps so that each restriction enzyme site refers to a column in the aligned sequence.
3. You will then use the aligned restriction site data to compare the restriction maps from two sequences.

### How to approach this:
I would suggest that you decide as a group what the format for storing your restriction maps for the aligned sequences should be. Then half the class should work together to produce the script that generates that data from the restrict output. The other half of the class should work together to write the script that will find restriction sites that appear in only one of two sequences when given that data.

This will be the major intellectual challenge for weeks 2 and 3.

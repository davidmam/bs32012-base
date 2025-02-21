# Lab books and code repositories

## Lab books
Your lab book is your day to day journal.  Bioinformatics is a more challenging area to keep a journal but we do expect you to do so and to the same standard as if you were in a wet lab.
Each thing you do should be recorded. You do not need to include raw data, but should include summary results and conclusions.

As for any experiment, each entry in your lab book should include:
* Date, title
* aim of what you are intending to do
* Method/process - this should be a record of what you are doing. It should include any key parameters, web addresses etc.
* results: An over view of results. Filenames and where they were saved. Github commit/tag references. 
* conclusions

There may be multiple method/results or method/results/conclusions blocks in any one experiment. It is a journal and shows what you have done and your engagement. **It will be assessed**

#### Example entry
```
30 January 2016 Database searching at NCBI

Aim: Identify suitable mitochindrial genome sequences

Workflow: Accessed http://www.ncbi.nlm.nih.gov/nuccore with Chrome from lab PC

Search term       Results
pink-footed Otter      457 sequence hits

Selected sequences U12345, M23456, gi:09876543 for download as these showed a complete mitochondrial genome (16,543 bp) for the organism with no ambiguous bases   

Added these references to the file sequence_list.md and a description of the animal to pinkfoototter.md. Github commit: 01234567

Conclusions: I have identified sufficient pink foot otter species. Will move on to find duck tailed beaver sequences.

```
#### Another example

```
19th January 2016. Learning Python.

Aim: to learn python

Workflow:
Accessed http://trypython.org
Worked through the first three sections with no problem.
Conclusion;
No problems so far, will progress onto section 4 which looks a bit more challenging.
```

Each day/experiment/investigation episode should be noted in the table of contents at the beginning.

## Coding and Github commits

A few guidelines for working on code and commiting to Github.

### Coding standards.
* Please only commit code that is interpreted without errors. It may not work or be complete but should at least be read by Python without syntax errors. Sometimes that is difficult but you can always put the code into comments or a multi-line string and commit with a message that it needs looking at.
* Use comments in the code. 
  * In particular, if you have something that you know is broken, comment it with ## FIX ME ## and a description of the error 
  * if you create a function but haven't got round to filling in the details, use ## TO DO ## with a descripttion of what needs to be done
* Don't overuse comments in the code. You should describe things that are not immediately obvious, or your aims for that block of code, not line by line behaviour.
* Many small commits (where you are changing a few files) are better than one big commit that changes many files. If you save up commits to the end of the day then you may have to do a lot of merging with other folk's commits.
* Don't micro-commit. Try to complete a 'unit of work' so that it is a distinct change. ie. 'added function xyz, tested and works on test data' rather than a commit for each line. This will usually be an hour or so work, or all the changes needed for a particular file or so on.
* If there is conflict, talk to each other and discuss and agree the best way forward. (And don't forget to note these discussions in your lab journal)
* All files should have a doc string. All functions should have a doc string. All files should be documented in a README.md in each directory with details of what the file is and instructions on how to use it.
* Improve each others work. If the instructions are not clear, improve them. You may not be the greatest coder, but you can always improve the documentation.
* Be open. Don't hog an bit of code. Let everyone make a contribution. Agree what you want to achieve then divide the tasks.
* Python coding:
  * indent with 4 spaces, not tab
  * Use UPPER case for constants
  * use lower case for function names
  * Use Title Case for Classes
  * Use constants, not literals in your code. ie define `PI=3.1415965` at the top of the code and use `PI` as you need it.
  * Keep functions short. If they start getting long, create sub-functions so the code is readable.
  * make your code robust - ie use `try:...except:` blocks and check input.
   
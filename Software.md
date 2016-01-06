# Software environment for the BS32011 Bioinformatics project

The following software are required for the project:

1. [Jalview](http://www.jalview.org). This will be accessed via the web and run theough Java Webstart. No specific installation is necessary.
1. [Python](http://www.python.org) is the programming language of choice. At this level of complexity it does not matter whether we use Python 2.7 or 3.4 but if you are installing it yourself, choose Python 3.4. We will use Spyder, the IDE provided by the [Anaconda](http://www.continuum.io) distribution. In addition we can use either stand-alone python scripts or [Jupyter notebooks](http://jupyter.org) for developing code. This is installed on the student desktop and on the teaching lab.
1. [Git](http://git-scm.com) is a version control system that allows collaborative working and synchronisation of work between individuals and between computers. It is installed on the student desktop as part of the [git-bash](https://git-for-windows.github.io/) distribution and on the teaching lab as the standalone client. 
1. [Unix bash shell](https://en.wikipedia.org/wiki/Bash_(Unix_shell) ) is a command line that allows running of programs and manipulation of data. This is installed as git-bash on the student desktop and is the standard terminal on the teaching server (and mac OS X). 
1. [Primer3](http://primer3.sourceforge.net) is a program used for predicting PCR primer pairs. This is installed on the teaching lab server. It can be installed on Windows and run from a command line but this has not been tested by me. (It may well run from a USB stick so you could use it in the IT suites - again, not tested).
1. The [EMBOSS](http://www.emboss.org) suite of programs is a collection of predominantly command line applications for manipulating molecular biology data. They perform functions such as restriction enzyme digest mapping. It is installed on the teaching lab server and is run from the command line (Bash shell/terminal)

## Installing software on your own machine

Follow the [recommendations given for installation of software](http://widdowquinn.github.io/2016-01-11-dundee/) for a [Software Carpentry](http://www.softwarecarpentry.org) workshop.
This will ensure that you have the core Python, Git and shell software.

For EMBOSS and Primer 3 you can follow the instructions on the specific websites. However, as the actual runnign of these programs is only a small part of the project, it may be better to focus effort on getting the scripts to work and run them on the teaching server rather than your own machine.

# Account registration

### Github
Create an account at [Github](http://www.github.com). You will use this to keey your work in sync.

### Life Sciences Computing
Register your university ID for a Life Sciences account at the [Life Sciences Portal](https://lsd.lifesci.dundee.ac.uk/register/internal). You will need this to access the teaching server.
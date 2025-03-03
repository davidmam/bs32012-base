# run as sortmyfiles.sh restrict_filename_to_sort
# $1 is the filename that was given on the command line (restrict_filename_to_sort)
mv $1 $1.orig #renames the file to add .orig to the filename so myfile.restrict is renamed to myfile.restrict.orig
head -n 26 $1.orig > $1 # get the first 26 lines of the renamed file and put them into a new file with the original file name
tail -n +27 $1.orig | head -n -10 | sort -n >> $1 # take all the lines from line 27 except the last 10 and sort them numerically (by the first column) and append them to the header in $1 
tail -n 10 $1.orig >> $1 # Append the last bit of the file to the data in $1

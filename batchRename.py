#!/usr/bin/python
# -*- coding: utf-8 -*-

import os       # for getting files from directory
import sys      # for accessing command line arguments
import pandas as pd	#Pandas should be handy here
# Command line arguments
assert len(sys.argv)<4, "batchrename takes at most 1 command line argument\n"+\
                        "Use: python batchrename.py [folder_name]"

if len(sys.argv) == 1:
    folder_name = "."     
    print "Use: python batchrename.py [folder_name]"
    print "Using default path: . (current folder)"
elif len(sys.argv) == 2:
    folder_name = sys.argv[1]   # First command line argument is folder

# translation table (TODO make better by importing a csv or tsv and pulling column one to be original name and column 2 to be final name, store as a dictionary I think and reference accordingly)
# potential second TODO, use a regex to identify a prefix and use that for the renaming
input_file_list  = ['file1.txt','file2.txt','file3.txt'] #The bracketed fields of this and the next line would be replaced by the csv or tsv column,
output_file_list = ['textfile_1.txt','textfile_2.txt','textfile_3.txt'] #in the future these would both be lists of RegExp prefixs

# make sure slash appears at end of folder name
os.path.join(folder_name, '')

# get every file in folder
files_list = os.listdir(folder_name)
for f in files_list: # iterate over all files in files_list
    if f.endswith(suffix): # prompt user or make an argument to decide suffix 
        if f in in_list: # TODO this line needs some work
            print f + ' becomes ' + out_list[in_list.index(f)] # TODO
os.rename(folder_name+f, folder_name+out_list[in_list.index(f)]) #TODO

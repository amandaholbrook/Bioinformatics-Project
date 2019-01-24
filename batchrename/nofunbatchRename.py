#!/usr/bin/python
# -*- coding: utf-8 -*-

#this program will rename the fiels in a given directory based on input from a csv file

import os       # for getting files from directory
import sys      # for accessing command line arguments
import pandas as pd	#Pandas should be handy here
# Command line arguments
assert len(sys.argv)<4, "batchrename takes at most 1 command line argument\n"+\
                        "Use: python batchrename.py [folder_name]"

if len(sys.argv) == 1:
	folder_name = "./"
	print ("Use: python batchrename.py [folder_name]")
	print ("Using default path: . (current folder)")
elif len(sys.argv) == 2:
	folder_name = sys.argv[1]   # First command line argument is folder

csv = "RenameIndex.csv"

table = pd.read_csv(csv, names = ['old_name', 'new_name'])

table['old_name'] = table['old_name'].astype(str)

print(table)

# get every file in folder
files_list = os.listdir(folder_name)
for f in files_list: # iterate over all files in files_list

	if "_" in f:
		split = f.split('_')
		id = split[0]
		suffix = ""
		for i in range(1, len(split)):
			suffix += "_" + split[i]
	else:
		continue

	if table['old_name'].str.contains(id).any():

		print (f + ' becomes ' + table.at[table.old_name[table.old_name == id].index.values.astype(int)[0], 'new_name'] + suffix)

		os.rename(folder_name + f, folder_name + table.at[table.new_name[table.old_name == id].index.values.astype(int)[0], 'new_name'] + suffix)

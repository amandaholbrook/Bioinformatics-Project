#!/usr/bin/python
# -*- coding: utf-8 -*-

####################################################
## NAME: batchRename
## DESC: a function to rename the files in a given
## directory based on input from a csv file
## AUTHOR: Amanda Holbrook
## COPYRIGHT: 2019, batchRename
## VERSION: 1.0.0
####################################################

import os       # for getting files from directory
import sys      # for accessing command line arguments
#import pandas as pd	#Pandas should be handy here


def rename(folder_name, csv):

	table = pd.read_csv(csv, names = ['old_name', 'new_name'])

	table['old_name'] = table['old_name'].astype(str)

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
			#print (f + ' becomes ' + table.at[table.old_name[table.old_name == id].index.values.astype(int)[0], 'new_name'] + suffix)
			os.rename(folder_name + f, folder_name + table.at[table.new_name[table.old_name == id].index.values.astype(int)[0], 'new_name'] + suffix)

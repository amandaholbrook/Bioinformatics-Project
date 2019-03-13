#!/usr/bin/python

###############################################
## NAME: fastaFormatter
## DESC: a function to format the given fasta
## file to ensure it can be read correctly
## AUTHOR: Amanda Holbrook
## COPYRIGHT: 2019, fastaFormatter
## VERSION: 1.0.0
###############################################

import sys, os

def format(fastafile, formattedfasta, marker, directory):
	first="TRUE"
	out = open(directory + formattedfasta, 'w')
	f = open(fastafile)
	for lines in f:
		if(lines.startswith(marker)): #finds marker
			id = lines
			seq=""
			if(first=="TRUE"):
				out.write(marker + id)
				first="FALSE"
			else:
				out.write('\n')
				out.write(id)
		else:
			out.write(lines.strip())

	f.close()
	out.close()

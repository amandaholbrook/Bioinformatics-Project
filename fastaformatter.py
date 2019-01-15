#this program will make sure the fasta file is correctly formatted

import sys, os

def format(fastafile, formattedfasta):

	first="TRUE"

	out = open(formattedfasta, 'w')
	f = open(fastafile)
	for lines in f:
		if(lines[0][0] == ">"): #finds marker
			if(first=="FALSE"):
				out.write(id)
				out.write('\n')
				out.write(seq.strip())
				out.write('\n')
			first="FALSE" #grabbing id on the first time through
			line = lines.split()
			id = line[0]
			seq=""
		else:
			seq+=lines.rstrip()
	f.close()
	out.close()

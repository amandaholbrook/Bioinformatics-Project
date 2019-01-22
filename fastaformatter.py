#this program will make sure the fasta file is correctly formatted

import sys, os

def format(fastafile, formattedfasta, marker):
	first="TRUE"
	out = open(formattedfasta, 'w')
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
				out.write(marker + id)
		else:
			out.write(lines.strip())

	f.close()
	out.close()

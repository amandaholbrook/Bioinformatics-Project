#this program will make sure the fasta file is correctly formatted

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

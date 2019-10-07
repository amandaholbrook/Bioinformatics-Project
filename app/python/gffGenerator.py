#!/usr/bin/python

#####################################
## NAME: gffGenerator
## DESC: a function to create a GFF
## file from a given fasta file
## AUTHOR: Amanda Holbrook
## COPYRIGHT: 2019, gffGenerator
## VERSION: 1.0.0
#####################################

import os, sys

def createGFF(stepping, marker, formattedfasta, gff, verbose, results):

	stepping = int(stepping)
	first="TRUE"
	f = open(formattedfasta, 'r', encoding='utf-8')
	out = open(results + gff, "w", encoding='utf-8')
	for lines in f:
		if(lines.startswith(marker)): #checking for new sequence identifier
			line = lines.split() #splits the current line up into strings
			id = line[0].replace(marker, "") #sets the first string as new id
			seq="" #initiates a new seq
			if verbose:
				print("importing sequence", id, "....")

		else:
			seq=lines.rstrip()
			

			length = len(seq)

			region = (id + "\t" + "RefSeq" + "\t" + "region" + "\t" +  "1" +  "\t" + str(length)\
				+ "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=" + id + "_region" + ";Name=" + id + "\n")
			out.write(region) #prints for full region

			print()
			for x in range(1, length, stepping): #prints incrementing by preset step
				n = x + stepping - 1
				#print(x)
				#print(n)
				if(n > len(seq)):
					n = len(seq)
				line1 = (id + "\t" + "RefSeq" + "\t" + "gene" + "\t" + str(x) +  "\t" + str(n)\
					+ "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=" + id + "_" + str(x) + "_gene" + ";Name=" + id + "_" + str(x) + "\n")
				line2 = (id + "\t" + "RefSeq" + "\t" + "mRNA" + "\t" + str(x) +  "\t" + str(n)\
					+ "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=" + id + "_" + str(x) + "mRNA" + ";Name=" + id + "_" + str(x) + "\n")
				out.write(line1) # gene
				out.write(line2) # MRNA

	out.close()
	f.close()

# pseudocode
# within above

# out.write() first time only
	# id  \t  "RefSeq"  \t  "region"  \t  1  \t  length  \t  .  \t  +/-  \t  .  \t  info  \n

# out.write() range 1-length, increment by  50?
	# id  \t  "RefSeq"  \t  "gene"  \t  x \t  x+50  \t  .  \t  +/-  \t  .  \t  ID=id_x  \n
	# id  \t  "RefSeq"  \t  "CDS"  \t  x  \t  x+50  \t  0  \t  +/-  \t  .  \t  ID=id_x  \n

# new line for each new sequence

# info = ID=id_position
# for id remove symbols, >

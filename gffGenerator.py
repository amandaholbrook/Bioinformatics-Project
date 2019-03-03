import os, sys

def createGFF(stepping, marker, formattedfasta, gff, verbose, f_directory):

	first="TRUE"
	f = open(f_directory + formattedfasta)
	out = open(gff, "w")
	for lines in f:
		if(lines.startswith(marker)): #checking for new sequence identifier
			line = lines.split() #splits the current line up into strings
			id = line[0].replace(marker, "") #sets the first string as new id
			seq="" #initiates a new seq
			if verbose:
				print("importing sequence", id, "....")

		else:
			seq=lines.rstrip()


			region = (id + "\t" + "RefSeq" + "\t" + "region" + "\t" +  "1" +  "\t" + str(len(seq))\
				+ "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=" + id + "_region" + ";Name=" + id + "\n")
			out.write(region) #prints for full region


			for x in range(1, len(seq), stepping): #prints incrementing by preset step
				next = x + stepping -1
				if(next > len(seq)):
					next = len(seq)
				line1 = (id + "\t" + "RefSeq" + "\t" + "gene" + "\t" + str(x) +  "\t" + str(next)\
					+ "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=" + id + "_" + str(x) + "_gene" + ";Name=" + id + "_" + str(x) + "\n")
				line2 = (id + "\t" + "RefSeq" + "\t" + "mRNA" + "\t" + str(x) +  "\t" + str(next)\
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

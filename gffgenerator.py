import os, sys

def createGFF(stepping, marker, file, gff):

	first = "TRUE"

	f = open(file)
	for lines in f:
		if(lines[0][0] == ">"): #checking for new sequence identifier
			if(first == "FALSE"): #doesn't run first time through
				tmp = (id + "\t" + "RefSeq" + "\t" + "region" + "\t" +  "1" +  "\t" + str(len(seq))\
					+ "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=" + id + ";Name=" + id + "\n")
				gff.write(tmp)
				for x in range(1, len(seq), stepping):
					line1 = (id + "\t" + "RefSeq" + "\t" + "gene" + "\t" + str(x) +  "\t" + str(x + 50)\
						+ "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=" + id + "_" + str(x) + ";Name=" + id + "_" + str(x) + "\n")
					line2 = (id + "\t" + "RefSeq" + "\t" + "mRNA" + "\t" + str(x) +  "\t" + str(x + 50)\
						+ "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=" + id + "_" + str(x) + ";Name=" + id + "_" + str(x) + "\n")
					gff.write(line1)
					gff.write(line2)
			first = "FALSE"
			line = lines.split() #splits the current line up into strings
			id = line[0].replace(marker, "") #sets the first string as new id
			seq="" #initiates a new seq
			print("importing sequence", id, "....\n")
		else:
			seq+=lines.rstrip() #fills sequence without whites

	gff.close()
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

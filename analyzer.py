print ("Amanda Holbrook")

import os, sys

file = sys.argv[1]
f = open(file)

out = open('out.txt', 'w')
first = "TRUE"
stepping=50
rem= ">"

for lines in f:
	if(lines[0][0] == ">"): #checking for new sequence identifier
		if(first == "FALSE"): #doesn't run first time through
			tmp = (id + "\t" + "RefSeq" + "\t" + "region" + "\t" +  "1" +  "\t" + str(len(seq))\
				+ "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=" + id + ";Name=" + id + "\n")
			out.write(tmp)
			for x in range(1, len(seq), stepping):
				line1 = (id + "\t" + "RefSeq" + "\t" + "gene" + "\t" + str(x) +  "\t" + str(x + 50)\
					+ "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=" + id + "_" + str(x) + ";Name=" + id + "_" + str(x) + "\n")
				line2 = (id + "\t" + "RefSeq" + "\t" + "mRNA" + "\t" + str(x) +  "\t" + str(x + 50)\
					+ "\t" + "." + "\t" + "+" + "\t" + "." + "\t" + "ID=" + id + "_" + str(x) + ";Name=" + id + "_" + str(x) + "\n")
				out.write(line1)
				out.write(line2)
		first = "FALSE"
		line = lines.split() #splits the current line up into strings
		id = line[0].replace(rem, "") #sets the first string as new id
		seq="" #initiates a new seq
		print("importing sequence", id, "....")
	else:
		seq+=lines.rstrip() #fills sequence without whites

out.close()
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

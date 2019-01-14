from gffgenerator import createGFF
import sys, os

print("\nA Bioinformatics Project")
print("Written by: \tAmanda Holbrook")
print("\t\tColin Kruse\n\n")

file = sys.argv[1] #input file

filename = file[0:file.find('.')] #grabbing file name w/o extension

gff = open(filename + '.gff', 'w') #new gff file to be created, w/ old filename
stepping = 50 #interval for gff sequence
marker = ">" #marker for new sequence

print("Step 1: Creating gff file.\n")
createGFF(stepping, marker, file, gff)

print("Step 2: Counts at each location.\n")
print("Merge files and analyze.\n")

print("Step 3: Differential counts per region.\n")
print("Matrix dissection (DREME).\n")

print("Step 4: Binding Matrix.\n")

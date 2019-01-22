from gffgenerator import createGFF
from fastaformatter import format
import sys, os, argparse

print("\nA Bioinformatics Project")
print("Written by: \tAmanda Holbrook")
print("\t\tColin Kruse\n\n")

parser = argparse.ArgumentParser()
parser.add_argument('-s', action = "store", dest = 'step', help='input the increment number')
parser.add_argument('-f', action = "store", dest = 'infile', help='input genome file in fasta format')
parser.add_argument('-o', action = "store", dest = 'output', help='input string for output file prefix')
parser.add_argument('-a', action = "store", dest = 'four', help='fourth choice')

results = parser.parse_args()
print('step= ', results.step)
print('file= ', results.infile)
print('output= ', results.output)
print('four= ', results.four)

fastafile = results.infile #fasta file

filename = fastafile[0:fastafile.find('.')] #grabbing file name w/o extension

formattedfasta = 'formatted_' + fastafile

gff = filename + '.gff' #new gff file to be created, w/ old filename
stepping = 50 #interval for gff sequence
marker = ">" #marker for new sequence

print("Step 1: Make sure fasta is properly formatted.\n")
format(fastafile, formattedfasta, marker)

print("Step 2: Creating gff file.\n")
createGFF(stepping, marker, formattedfasta, gff)

print("Step 3: Counts at each location.\n")
print("Merge files and analyze.\n")

print("Step 4: Differential counts per region.\n")
print("Matrix dissection (DREME).\n")

print("Step 5: Binding Matrix.\n")

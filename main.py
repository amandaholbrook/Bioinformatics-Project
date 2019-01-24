from gffGenerator import createGFF
from fastaFormatter import format
from batchRename import rename
import sys, os, argparse

print("\nA Bioinformatics Project")
print("Written by: \tAmanda Holbrook")
print("\t\tColin Kruse\n\n")

parser = argparse.ArgumentParser()
parser.add_argument('-s', action = "store", dest = 'step', default = 50, help='input the increment number')
parser.add_argument('-f', action = "store", dest = 'fasta_file', help='input genome file in fasta format')
parser.add_argument('-c', action = "store", dest = 'csv', help='input csv file for remaning files')
parser.add_argument('-d', action = "store", dest = 'directory', default = '\.', help='input directory for renaming files')

results = parser.parse_args()

print('Command Line Arguments:')
print('step= ', results.step)
print('fasta_file= ', results.fasta_file)
print('csv= ', results.csv)
print('directory= ', results.directory)
print('\n\n')

fasta_file = results.fasta_file #original fasta file
step = results.step #increment for gff file
csv = results.csv #csv for renaming files in directory
directory = results.directory #directory for renaming files

filename = fasta_file[0:fasta_file.find('.')] #grabbing file name w/o extension
formatted_fasta = 'formatted_' + fasta_file

gff = filename + '.gff' #new gff file to be created, w/ old filename
marker = ">" #marker for new sequence

print("Step 1: Make sure fasta is properly formatted.\n")
format(fasta_file, formatted_fasta, marker)

print("Step 2: Creating gff file.\n")
createGFF(step, marker, formatted_fasta, gff)

print("Step 3: Counts at each location.\n")
print("Merge files and analyze.\n")

print("Step 4: Differential counts per region.\n")
print("Matrix dissection (DREME).\n")

print("Step 5: Binding Matrix.\n")

print("Another Step: Renaming files in directory\n")
#rename(folder_name, csv)

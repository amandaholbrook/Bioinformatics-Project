from gffGenerator import createGFF
from fastaFormatter import format
from batchRename import rename
import sys, os, argparse, subprocess

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

assert fasta_file != None, "Please enter a fasta file (option -f)"

filename = fasta_file[0:fasta_file.find('.')] #grabbing file name w/o extension
formatted_fasta = 'formatted_' + fasta_file

gff = filename + '.gff' #new gff file to be created, w/ old filename
marker = ">" #marker for new sequence

print("Make sure fasta is properly formatted.\n")
format(fasta_file, formatted_fasta, marker)

print("Creating gff file.\n")
createGFF(step, marker, formatted_fasta, gff)
#Here we will use GffCompare to merge this GFF with a
#user-provided one (if they provide it)
#filename1 = gff
#filename2 = gff_given
#args = "gffcompare/gffcompare.exe -config " + filename1 + filename2
#subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)

#LOWEST PRIORITY:If we get EVERYTHING else done we'll
#add on something here to add descriptors to the the
#regions that don't code for genes.

print("Get counts at each location.\n")
#Here we will use BWA (burrows wheeler aligner) to align
#reads to fasta/GFF file. Then we will use HTseq-count to
#convert alignments to counts

print("Merge files and analyze. (Optional)\n")
#Here we will use the rename script you made (if the user
#provided one)

#if csv != "None":
print("Renaming files in directory. (Optional)\n")
#rename(folder_name, csv)

print("Merging columns.\n")
#Then we will merge columns using the merge counts script you made
#merge(mergedfile, column, filetype, path)

print("Differential counts per region.\n")
#here we will run an R script (I can provide you with the
#basic script that isn't properly automated yet anytime) to
#produce differential counts for regions of interest. this will
#be the primary output

print("Binding Matrix/Matrix dissection (DREME). (Add On)\n")
#This is the add on, we'll see if we get to this.  Ideally
#we will pull all the sequences of regions that are significant
#based on step 4 (and the IDs we created) and we'll run motif
#analysis on them. This will be one of the primary outputs from the pipeline

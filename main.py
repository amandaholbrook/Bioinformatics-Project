#!/usr/bin/python

####################################
## A Bioinformatics Project
## High throughput sequencing data
## analysis pipeline development
###################################
## Author: Amanda Holbrook
##	 & Colin Kruse
## Copyright: 2019, NAME_HERE
## Version: 1.0.0
## Email: amandajoee@gmail.com
###################################

from gffGenerator import createGFF
from fastaFormatter import format
from batchRename import rename
import sys, os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-step', action = "store", dest = 'step', default = 50, help='input the increment number')
parser.add_argument('-fasta', action = "store", dest = 'fasta_file', help='input genome file in fasta format')
parser.add_argument('-csv', action = "store", dest = 'csv', help='input csv file for remaning files')
parser.add_argument('-fdir', action = "store", dest = 'f_directory', help='input directory for fasta file')
parser.add_argument('-rdir', action = "store", dest = 'r_directory', help='input directory for renaming files')
parser.add_argument('-mdir', action = "store", dest = 'm_directory', help='input directory for merging read count files')
parser.add_argument('-verbose', action = "store_true", dest = 'verbose', help='include to print details')
parser.add_argument('-merge', action = "store", dest = 'mergedfile', default = "merged.out", help='input name for merged file')
parser.add_argument('-read', action = "store", dest = 'read_type', help='input read type to merge by (Unstranded, Stranded, Reverse')
parser.add_argument('-ext', action = "store", dest = 'file_type', default = ".tab", help='input extension for files to merge')
parser.add_argument('-max', action = "store", dest = 'max_threads', default = 2, help='max threads for BWA')

results = parser.parse_args()

fasta_file = results.fasta_file #original fasta file
step = results.step #increment for gff file
csv = results.csv #csv for renaming files in directory
f_directory = results.f_directory #directory for fasta file
r_directory = results.r_directory #directory for renaming files
m_directory = results.m_directory #directory for merging read files
verbose = results.verbose #printing more details
mergedfile = results.mergedfile #name for mergedfile
filetype = results.file_type #file extension of files to merge
read_type = results.read_type #read type to merge by
max_threads = results.max_threads #max threads for BWA

if verbose:
        print("\nA Bioinformatics Project")
        print("Written by: \tAmanda Holbrook")
        print("\t\tColin Kruse\n\n")

assert fasta_file != None, "Please enter a fasta file (option -fasta)"
assert f_directory != None, "Please enter directory for fasta file (option -fdir)"

if csv != None:
	assert r_directory != None, "Please provide a directory of files to rename (option -rdir)"

if read_type != None:
	assert m_directory != None, "Please provide a directory of read count files (option -mdir)"


#creating name for formatted fasta file
filename = fasta_file[0:fasta_file.find('.')] #grabbing file name w/o extension
formatted_fasta = 'formatted_' + fasta_file
fasta_file = f_directory + fasta_file

#creating name for new gff file
gff = f_directory + filename + '.gff' #new gff file to be created, w/ old filename
marker = ">" #marker for new sequence

#formatting the given fasta file
if verbose:
	print("Formatting fasta file ....")
format(fasta_file, formatted_fasta, marker, f_directory)
if verbose:
	print("Done.\n")

#generating a GFF gile from the formatted fasta file
if verbose:
	print("Generating a gff file ....")
createGFF(step, marker, formatted_fasta, gff, verbose, f_directory)
if verbose:
	print("Done.\n")


#SKIP FOR NOW
#Here we will use gffMerge to merge this GFF with a
#user-provided one (if they provide it)
#filename1 = gff
#filename2 = gff_given
#args = "gffMerge -f " + filename1 + " " + filename2
#os.system(args)

#LOWEST PRIORITY:If we get EVERYTHING else done we'll
#add on something here to add descriptors to the the
#regions that don't code for genes.


#using BWA and HTseq-count to get counts
if verbose:
	print("Getting counts at each location ....")

#BWA index
#args2 = "bwa index [-a bwtsw|is] input_reference.fasta index_prefix"
#os.system(args2)
#BWA mem
#args3 =
#os.system(args3)

#feature-counts
#args4 = "featureCounts -T #ofcores -a YOURGFFFILE -o NAMEOFINPUTFILE_counts OUTPUTOFALIGNMENT"
#os.system(args4)

if verbose:
	print("Done.\n")

#renaming files if csv was given
if csv != None:
	if verbose:
		print("Renaming files in directory ....")
	rename(r_directory, csv)
	if verbose:
		print("Done.\n")

#combining counts if read_type was given
if read_type != None:
	if verbose:
		print("Merging files by ", read_type, "reads ....")
	merge(mergedfile, read_type, filetype, m_directory)
	if verbose:
		print("Done.\n")


#takes previous found counts and produces differential counts
if verbose:
	print("Producing differential counts per region ....")

#R script
#args 4 = ""
#os.system(args4)

if verbose:
        print("Done.\n")

#here we will run an R script (I can provide you with the
#basic script that isn't properly automated yet anytime) to
#produce differential counts for regions of interest. this will
#be the primary output


if verbose:
	print("Binding Matrix/Matrix dissection (DREME). (Add On)\n")
#This is the add on, we'll see if we get to this.  Ideally
#we will pull all the sequences of regions that are significant
#based on step 4 (and the IDs we created) and we'll run motif
#analysis on them. This will be one of the primary outputs from the pipeline

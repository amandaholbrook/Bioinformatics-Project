from analyzer import createGFF
import sys, os

file = sys.argv[1] #input file

filename = file[0:file.find('.')] #grabbing file name w/o extension

gff = open(filename + '.gff', 'w') #new gff file to be created, w/ old filename
stepping = 50 #interval for gff sequence
marker = ">" #marker for new sequence

createGFF(stepping, marker, file, gff)

print("Amanda Holbrook")
import sys, os
import pandas as pd

def merge(mergedfile, column, filetype, path)

	first = True
	out = open(mergedfile, 'w')
	header_list = ['Gene']
	dfend = pd.DataFrame(columns = header_list)
	filelist = os.listdir(path)

	for x in filelist:
		if x.endswith(filetype):
			with open(path + x) as f:
				df = pd.read_table(f, names = ['Gene', '2', '3', '4'])
				col = len(df.columns)
				if (col != 4) == True:
					print("Not enough columns in file " , x)
					sys.exit()
				n = len(df.index)
				if (n < 4) == True:
					print("Not enough rows in file ", x)
					sys.exit()
				df2 = df.tail(n-4)
				if first==True:
					dfend['Gene'] = df2['Gene']
					first=False
				if (dfend['Gene'] == df2['Gene']).any==False:
					print("The row names do not match.")
					sys.exit()
				rowname = x.split(".")[0]
				dfend[rowname] = df2[column]

	print(dfend)
	dfend.to_csv(out, sep = '\t')

	print("Files Merged.")

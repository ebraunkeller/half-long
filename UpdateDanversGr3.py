# UpdateDanversGr3.py pivots the crosstab writing assessment file to create fields named "Subtest" and "Score"
# invoke by python UpdateDanversGr3.py  <inputfilename full path>, <outputfilename full path>
#
# filename must be .csv format
import csv
import pickle
import sys
import os
import logging
import string

# These are the fixed columns for grade 3

fixedcol = [
['ACCESS','BOY','','']       ,
['DAZE','BOY',8,5]           ,
['VOCAB','BOY',5,4]          ,
['COMP','BOY',5,4]           ,
['TOTAL','BOY',5,4]          ,
['DRA','BOY',28,24]          ,
['DRA ACC','BOY',' ',90]     ,
['DRA COMP','BOY',' ',13]    ,
['DAZE','MOY',11,7]          ,
['L-Z LEVEL','MOY',15,14]  ,
['L-Z ACC','MOY',' ',90]     ,
['L-Z COMP','MOY',' ',2]     ,
['VOCAB','EOY',5,4]          ,
['COMP','EOY',5,4]           ,
['TOTAL','EOY',5,4]          ,
['L-Z LEVEL','EOY',16,17]  ,
['L-Z ACC','EOY','',90]      ,
['L-Z COMP','EOY',' ',2]
]

#These are the exceptions for Grade 3
#BOY letter grade M or higher in DRA is at benchmark

#BOY letter grade L in DRA is below benchmark - icolnum=7
LZ_col_boy = ['L-Z LEVEL','BOY',string.uppercase.index('M'), string.uppercase.index('L')]

#MOY any number is well below icolnum 11
DRA_col_moy = ['DRA','MOY',2000,1000]

#EOY - any number is well below - icolnum 17
DRA_col_eoy = ['DRA','EOY',2000,1000]

print "Copyright 2014-2015 BKLSchoolVision"
print "Begin processing Grade 3 file..."

InFileName = sys.argv[1]
outFileName = sys.argv[2]
#no output file exists if true
#New = True
 
#if os.path.exists(outFileName): New = False

Icsvfile = open(InFileName) 
reader = csv.reader(Icsvfile)
#skip the first 7 rows - all part of the header
for i in range(7):next(reader)
output=[]
with open(outFileName,'a+b') as csvfile:
		wr= csv.writer(csvfile,delimiter=',')
	# Write the header
	#
		wr.writerow(['SASID','Year','Score','Assessment','Period','A','B'])
		for row in reader:
			icolnum=0
			for col in row:
				if(icolnum==0):
					name =col
					icolnum+=1
				elif(icolnum==1):
					SASID=col
					icolnum+=1
				else:
					score=col
					try:
						if(col.isalpha()): score=string.uppercase.index(col)
					except:
						score = None
					output=[SASID,'SY2016',score]
					if(icolnum==7 and col.isalpha()):output.extend(LZ_col_boy)
					elif(icolnum==11 and col.isdigit()): output.extend(DRA_col_moy)
					elif(icolnum==17 and col.isdigit()): output.extend(DRA_col_eoy)
					elif icolnum <= len(fixedcol):
						output.extend(fixedcol[icolnum-2])
						wr.writerow(output) # skip the new column that they added
					icolnum+=1

csvfile.close()
print "Processing completed..."
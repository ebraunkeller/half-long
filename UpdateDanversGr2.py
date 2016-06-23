# UpdateDanversGr2.py pivots the crosstab writing assessment file to create fields named "Subtest" and "Score"
# invoke by python UpdateDanversGr2.py  <inputfilename full path>, <outputfilename full path>
#
# filename must be .csv format
import csv
import pickle
import sys
import os
import logging
import string

# These are the fixed columns for grade 2

fixedcol = [
['DIBELS CLS','BOY',54,35]         ,
['DIBELS WWR','BOY',16,6]          ,
['DIBELS ORF','BOY',52,37]         ,
['DIBELS ORF ACC','BOY',90,81]     ,
['VOCAB','BOY',5,4]                ,
['COMP','BOY',5,4]                 ,
['TOTAL','BOY',5,4]                ,
['DRA LEVEL','BOY',16,14]          ,
['DRA ACC','BOY',' ',90]           ,
['DRA COMP','BOY',' ',13]          ,
['DIBELS ORF','MOY',72,55]         ,
['DIBELS ORF ACC','MOY',96,91]     ,
['DRA LEVEL','MOY',20,18]          ,
['DRA ACC','MOY',' ',90]           ,
['DRA COMP','MOY',' ',13]          ,
['DIBELS ORF','EOY',87,65]         ,
['DIBELS ORF ACC','EOY',97,93]     ,
['VOCAB','EOY',5,4]                ,
['COMP','EOY',5,4]                 ,
['TOTAL','EOY',5,4]                ,
['DRA LEVEL','EOY',28,24]          ,
['DRA ACC','EOY',' ',90]           ,
['DRA COMP','EOY',' ',13]
]

# These are the exceptions for grade 2
#BOY any letter in DRA is above benchmark icolnum= 9

LZ_col_boy = ['L-Z','BOY', string.uppercase.index('A'),-1]

#MOY any letter in DRA is above benchmark icolnum = 15
LZ_col_moy = ['L-Z','MOY', string.uppercase.index('A'),-1]

#EOY any letter in DRA is above benchmark icolnum =23
LZ_col_eoy = ['L-Z','EOY', string.uppercase.index('A'),-1]



print "Copyright 2014-2015 BKLSchoolVision"
print "Begin processing Grade 2 file..."

InFileName = sys.argv[1]
outFileName = sys.argv[2]
#no output file exists if true
#New = True
 

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
		for row1 in reader:
			row=row1[:25]	# slice off the bad pieces of the file
			icolnum=0
			for col in row:
#				print col, icolnum
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
					output=[SASID,'SY2016' , score]
					if(icolnum==9 and col.isalpha()):output.extend(LZ_col_boy)
					elif(icolnum==15 and col.isalpha()):output.extend(LZ_col_moy)
					elif(icolnum==23 and col.isalpha()):output.extend(LZ_col_eoy)
					elif icolnum <= len(fixedcol):
						output.extend(fixedcol[icolnum-2])
						wr.writerow(output) # skip the new column that they added
					icolnum+=1

csvfile.close()
print "Processing completed..."
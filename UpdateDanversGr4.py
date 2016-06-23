# UpdateDanversGr4.py pivots the crosstab writing assessment file to create fields named "Subtest" and "Score"
# invoke by python UpdateDanversGr4.py  <inputfilename full path>, <outputfilename full path>
#
# filename must be .csv format
import csv
import pickle
import sys
import os
import logging
import string




# These are the fixed columns for grade 4

fixedcol = [
['DAZE','BOY',15,10]      ,
['STATE TEST',' ',' ',' '],
['COMP','BOY',5,4]        ,
['VOCAB','BOY',5,4]       ,
['TOTAL','BOY',5,4]       ,
['L-Z LEVEL','BOY',16,15],
['L-Z ACC','BOY',' ',90]  ,
['L-Z COMP','BOY',' ',2]  ,
['DAZE','MOY',17,12]      ,
['L-Z LEVEL','MOY',18,17],
['L-Z ACC','MOY',' ',90]  ,
['L-Z COMP','MOY',' ',2]  ,
['COMP','EOY',5,4]        ,
['VOCAB','EOY',5,4]       ,
['TOTAL','EOY',5,4]       ,
['L-Z LEVEL','EOY',' ',90],
['L-Z ACC','EOY',' ',90]  ,
['L-Z COMP','EOY',' ',2]
]
# These are exceptions:
# case where L-Z is replaced by DRA - all numeric scores are well below benchmark columns 7,11,17
DRA_col_boy = ['DRA','BOY', 2000,1000]
DRA_col_moy = ['DRA','MOY', 2000,1000]
DRA_col_eoy = ['DRA','EOY', 2000,1000]

print "Copyright 2014-2016 BKLSchoolVision"
print "Begin processing Grade 4 file..."

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
					output=[SASID,'SY2016', score]
					if(icolnum==7 and col.isdigit()): output.extend(DRA_col_boy)
					elif(icolnum==11 and col.isdigit()):output.extend(DRA_col_moy)
					elif(icolnum==17 and col.isdigit()):output.extend(DRA_col_eoy)
					elif icolnum <= len(fixedcol):
						output.extend(fixedcol[icolnum-2])
						wr.writerow(output) # skip the new column that they added
					icolnum+=1

csvfile.close()
print "Processing completed..."
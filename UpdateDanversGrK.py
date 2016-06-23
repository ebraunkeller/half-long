# UpdateDanversGrK.py pivots the crosstab writing assessment file to create fields named "Subtest" and "Score"
# invoke by python UpdateDanversGrK.py  <inputfilename full path>, <outputfilename full path>
#
# filename must be .csv format
import csv
import pickle
import sys
import os
import string


# These are the fixed columns for grade K

fixedcol = [
['DIBELS FSF','BOY',10,5]                ,
['DIBELS LNF','BOY',8,2]                  ,
['DIBELS FSF','MOY',30,20]               ,
['DIBELS LNF','MOY',27,15]               ,
['DIBELS PSF','MOY',20,10]               ,
['DIBELS CLS','MOY',17,8]                ,
['DIBLES WWR','MOY',' ',' ']             ,
['DIBLES LNF','EOY',40,29]               ,
['DIBELS PSF','EOY',40,25]               ,
['DIBELS CLS','EOY',18,15]               ,
['DIBELS WWR','EOY',' ',' ']             ,
['DRA LEVEL','EOY',3,2]                  ,
['DRA ACC','EOY',' ',90]                 ,
['DRA COMP','EOY',' ',13]                
]

#These are the exceptions for K:
# Any letter for DRA EOY is above benchmark icolnum=13
LZ_col_eoy = ['L-Z','EOY', string.uppercase.index('A'),-1]

print "Copyright 2014-2015 BKLSchoolVision"
print "Begin processing Grade K file..."

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
#					if(score.isalpha()): score=string.uppercase.index(col)
					output=[SASID,'SY2016', score]
					if(icolnum==12 and col.isalpha()): output.extend(LZ_col_eoy)
					elif icolnum <= len(fixedcol):
						output.extend(fixedcol[icolnum-2])
						wr.writerow(output) # skip the new column that they added
					icolnum+=1

csvfile.close()
print "Processing completed..."
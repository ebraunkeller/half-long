# UpdateDanversGr1.py pivots the crosstab writing assessment file to create fields named "Subtest" and "Score"
# invoke by python UpdateCRA.py  <inputfilename full path>, <outputfilename full path>
#
# filename must be .csv format
import csv
import pickle
import sys
import os
import string


# These are the fixed columns for grade 1

fixedcol = [
['DRA LEVEL','BOY',3,2]              ,
['DRA ACC','BOY',' ',90]             ,
['DRA COMP','BOY',' ',13]            ,
['DIBLES LNF','BOY',37,25]           ,
['DIBLES CLS','BOY',27,18]           ,
['DIBELS WWR','BOY',1,0]             ,
['WORD LIST','BOY',20,10]            ,
['DIBELS CLS','MOY',43,33]           ,
['DIBELS WWR','MOY',8,3]             ,
['DIBELS ORF','MOY',23,16]           ,
['DIBLES ACC','MOY',78,68]           ,
['DRA LEVEL', 'MOY',10,8]            ,
['DRA ACC','MOY',' ',90]                ,
['DRA COMP','MOY',' ',13]            ,
['WORD LIST', 'MOY',80,70]           ,
['DIBELS CLS','EOY',58,47]           ,
['DIBELS WWR','EOY',13,6]            ,
['DIBELS ORF','EOY',47,32]           ,
['DIBLES ACC','EOY',90,82]           ,
['WORD LIST', 'EOY',180,170]         ,
['DRA LEVEL', 'EOY',16,14]           ,
['DRA ACC','EOY',' ',90]             ,
['DRA COMP','EOY',' ',13]
]

#These are the exceptions for grade 1
#BOY any letter in DRA is above benchmark icolnum= 2

LZ_col_boy = ['L-Z','BOY', string.uppercase.index('A'),-1]

#MOY any letter in DRA is above benchmark icolnum = 13
LZ_col_moy = ['L-Z','MOY', string.uppercase.index('A'),-1]

#EOY any letter in DRA is above benchmark icolnum =22
LZ_col_eoy = ['L-Z','EOY', string.uppercase.index('A'),-1]


print "Copyright 2014-2016 BKLSchoolVision"
print "Begin processing Grade 1 file..."

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
					output=[SASID,'SY2016',score]
					if(icolnum==2 and col.isalpha()):output.extend(LZ_col_boy)
					elif(icolnum==13 and col.isalpha()):output.extend(LZ_col_moy)
					elif(icolnum==22 and col.isalpha()):output.extend(LZ_col_eoy)
					elif icolnum <= len(fixedcol):
						output.extend(fixedcol[icolnum-2])
						wr.writerow(output) # skip the new column that they added
					icolnum+=1

csvfile.close()
print "Processing completed..."
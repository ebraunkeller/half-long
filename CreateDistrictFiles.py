import csv
import pickle
import sys
import os

path ='C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\\'

Grade1 =[path+'GOGr1.csv',path+'HLGr1.csv',path+'RSGr1.csv',path+'SMGr1.csv',path+'THGr1.csv']
Grade2 =[path+'GOGr2.csv',path+'HLGr2.csv',path+'RSGr2.csv',path+'SMGr2.csv',path+'THGr2.csv']
Grade3 =[path+'GOGr3.csv',path+'HLGr3.csv',path+'RSGr3.csv',path+'SMGr3.csv',path+'THGr3.csv']
Grade4 =[path+'GOGr4.csv',path+'HLGr4.csv',path+'RSGr4.csv',path+'SMGr4.csv',path+'THGr4.csv']
Grade5 =[path+'GOGr5.csv',path+'HLGr5.csv',path+'RSGr5.csv',path+'SMGr5.csv',path+'THGr5.csv']
GradeK =[path+'GOGrK.csv',path+'HLGrK.csv',path+'RSGrK.csv',path+'SMGrK.csv',path+'THGrK.csv']

#Grade 1
with open(path+'DISGr1.csv','a+b') as outfile:
		wr= csv.writer(outfile,delimiter=',')
	# Write the header
	#
		wr.writerow(['SASID','Year','Score','Assessment','Period','A','B'])
		for fname in Grade1:
			with open(fname) as infile:
				next(infile) #remove the header
				for line in infile:
					outfile.write(line)
					print line
outfile.close()					
#Grade 2
with open(path+'DISGr2.csv','a+b') as outfile:
		wr= csv.writer(outfile,delimiter=',')
	# Write the header
	#
		wr.writerow(['SASID','Year','Score','Assessment','Period','A','B'])
		for fname in Grade2:
			with open(fname) as infile:
				next(infile) #remove the header
				for line in infile:
					outfile.write(line)
outfile.close()
#Grade 3
with open(path+'DISGr3.csv','a+b') as outfile:
		wr= csv.writer(outfile,delimiter=',')
	# Write the header
	#
		wr.writerow(['SASID','Year','Score','Assessment','Period','A','B'])
		for fname in Grade3:
			with open(fname) as infile:
				next(infile) #remove the header
				for line in infile:
					outfile.write(line)
outfile.close()					
#Grade 4
with open(path+'DISGr4.csv','a+b') as outfile:
		wr= csv.writer(outfile,delimiter=',')
	# Write the header
	#
		wr.writerow(['SASID','Year','Score','Assessment','Period','A','B'])
		for fname in Grade4:
			with open(fname) as infile:
				next(infile) #remove the header
				for line in infile:
					outfile.write(line)
outfile.close()
#Grade 5
with open(path+'DISGr5.csv','a+b') as outfile:
		wr= csv.writer(outfile,delimiter=',')
	# Write the header
	#
		wr.writerow(['SASID','Year','Score','Assessment','Period','A','B'])
		for fname in Grade5:
			with open(fname) as infile:
				next(infile) #remove the header
				for line in infile:
					outfile.write(line)
outfile.close()
#Grade K
with open(path+'DISGrK.csv','a+b') as outfile:
		wr= csv.writer(outfile,delimiter=',')
	# Write the header
	#
		wr.writerow(['SASID','Year','Score','Assessment','Period','A','B'])
		for fname in GradeK:
			with open(fname) as infile:
				next(infile) #remove the header
				for line in infile:
					outfile.write(line)
outfile.close()

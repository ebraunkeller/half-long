# Create data extract for each grade and school. Input is:
# sys.argv[1] = assessment file name
# sys.argv[2] = demographics file name
# sys.argv[3] = .tde file name
# sys.argv[4] = full path
# full path is hardwired in charstring "fullpath"

# Join the assessment file <school>Gr1.csv and the demographics file <school>Demo.csv
# by the student's SASID
import csv,sys
import os,datetime,time
import dataextract as tde
#fullpath = 'C:\Users\Elaine\Documents\BKL\Danvers\Implementation15-16\TableauFormat\\'
fullpath =sys.argv[4]
AssFile =sys.argv[1]
DemoFile = sys.argv[2]
TDEFile = sys.argv[3]
print TDEFile
TDEFileFull=fullpath+TDEFile
#os.remove(TDEFileFull)
#
tdefile = tde.Extract(TDEFileFull)
#Assessment file
fAss= open(fullpath+AssFile,'rb')
csvReaderAss = csv.reader(fAss, delimiter=',')

#Demographics file
fDemo = open(fullpath+DemoFile, 'rb')
csvReaderDemo = csv.reader(fDemo, delimiter=',')

# The table defs are different at each grade level
if tdefile.hasTable('Extract'):
	table = tdefile.openTable('Extract')
	tableDef = table.getTableDefinition()
else: 
#Create the tableDef for assessment data
	tableDef = tde.TableDefinition()
	tableDef.addColumn('SASID', tde.Type.CHAR_STRING)
	tableDef.addColumn('Year', tde.Type.CHAR_STRING)
	tableDef.addColumn('Score', tde.Type.DOUBLE)
	tableDef.addColumn('Assessment', tde.Type.CHAR_STRING)
	tableDef.addColumn('Period', tde.Type.CHAR_STRING)
	tableDef.addColumn('A', tde.Type.INTEGER)
	tableDef.addColumn('B', tde.Type.INTEGER)
# and demographic data
	tableDef.addColumn('SchoolID', tde.Type.INTEGER)
	tableDef.addColumn('First_Name', tde.Type.CHAR_STRING)
	tableDef.addColumn('Last_Name', tde.Type.CHAR_STRING)
	tableDef.addColumn('Gender', tde.Type.CHAR_STRING)
	tableDef.addColumn('Alert_other', tde.Type.CHAR_STRING)
	tableDef.addColumn('Ethnicity', tde.Type.CHAR_STRING)
	tableDef.addColumn('MA_LEPinUS', tde.Type.CHAR_STRING)
	tableDef.addColumn('MA_IncomeStatus', tde.Type.CHAR_STRING)



#Create the table in the image of the tableDef
	table = tdefile.addTable('Extract',tableDef)
	

#Step 4: Loop through the csv, grab all the data, put it into rows
#and insert the rows into the table
newrow = tde.Row(tableDef)

#Skip the first line of both files since it has the headers
csvReaderDemo.next() 

for line2 in csvReaderDemo:
	csvReaderAss.next() # first row contains header

	for line1 in csvReaderAss:
		if(line1[0]==line2[1]):			# join via SASID

#assessment data. Many assessments are blank, so we have to check add null if blank			

			newrow.setCharString(0, str(line1[0]))
			newrow.setCharString(1, str(line1[1]))
			if(line1[2].isdigit()): newrow.setDouble(2,float(line1[2]))
			else: newrow.setNull(2)
			newrow.setCharString(3,str(line1[3]))
			newrow.setCharString(4,line1[4])
			if(line1[5].isdigit()): newrow.setInteger(5, int(line1[5]))
			else: newrow.setNull(5)
			if(line1[6].isdigit()):newrow.setInteger(6,int(line1[6]))
			else: newrow.setNull(6)
# demographic data. The "Alert" field may be blank
			newrow.setInteger(7,int(line2[0]))
			newrow.setCharString(8,str(line2[3]))
			newrow.setCharString(9,str(line2[4]))
			newrow.setCharString(10,str(line2[5]))
			if(line2[6]==' '): newrow.setNull(11)
			else: newrow.setCharString(11,str(line2[6]))
			newrow.setCharString(12,str(line2[8]))
			newrow.setCharString(13,str(line2[9]))
			newrow.setCharString(14,str(line2[10]))

			table.insert(newrow)

	fAss.seek(0)


#Close the tde
tdefile.close()

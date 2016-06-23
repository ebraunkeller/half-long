#Upload the .twbx files to the appropriate folders in the Danvers google drive
# no arguments
# local file names and google drive folders are hard coded

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from apiclient import errors
from apiclient import http

def RemoveFiles(id):
	file_list2 = drive.ListFile({'q':"trashed=false and '"+id+"' in parents"}).GetList()
	for file2 in file_list2:
		if(  file2['title']=="Grade1.twbx"): file2['title']="Grade1_Old.twbx"
		elif(file2['title']=="Grade2.twbx"): file2['title']="Grade2_Old.twbx"
		elif(file2['title']=="Grade3.twbx"): file2['title']="Grade3_Old.twbx"
		elif(file2['title']=="Grade4.twbx"): file2['title']="Grade4_Old.twbx"
		elif(file2['title']=="Grade5.twbx"): file2['title']="Grade5_Old.twbx"
		elif(file2['title']=="GradeK.twbx"): file2['title']="GradeK_Old.twbx"
		file2.Upload()

gauth=GoogleAuth()
gauth.LocalWebserverAuth() #creates local webserver and auto handles authentication

drive= GoogleDrive(gauth)



#loop through all the junk in the google drive and find the correct folder. Dump a file in the folder.

file_list = drive.ListFile({'q': "trashed=false"}).GetList()
for file1 in file_list:
	if(file1['title'])=='Great Oak Tableau Folder':
		print file1['title'], file1['mimeType'],file1['id']

# Search for existing files and rename them if they are there
		RemoveFiles(file1['id'])
		
# upload the new files
		gfile = drive.CreateFile({'title':'Grade1.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\GreatOak\Grade1.twbx')
		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade2.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\GreatOak\Grade2.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'Grade3.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\GreatOak\Grade3.twbx')
		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade4.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\GreatOak\Grade4.twbx')
		gfile.Upload()

		
		gfile = drive.CreateFile({'title':'Grade5.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\GreatOak\Grade5.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'GradeK.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\GreatOak\GradeK.twbx')
		gfile.Upload()


	elif file1['title']=='Highlands Tableau Folder':
		print file1['title'], file1['mimeType'],file1['id']

# Search for existing files and rename them if they are there
		RemoveFiles(file1['id'])
		
		gfile = drive.CreateFile({'title':'Grade1.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Highlands\Grade1.twbx')
 		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade2.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Highlands\Grade2.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'Grade3.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Highlands\Grade3.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'Grade4.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Highlands\Grade4.twbx')
		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade5.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Highlands\Grade5.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'GradeK.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Highlands\GradeK.twbx')
		gfile.Upload()


	elif file1['title']=='Smith Tableau Folder':
		print file1['title'], file1['mimeType'],file1['id']
# Search for existing files and rename them if they are there
		RemoveFiles(file1['id'])
		gfile = drive.CreateFile({'title':'Grade1.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Smith\Grade1.twbx')
 		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade2.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Smith\Grade2.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'Grade3.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Smith\Grade3.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'Grade4.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Smith\Grade4.twbx')
		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade5.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Smith\Grade5.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'GradeK.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Smith\GradeK.twbx')
		gfile.Upload()

	elif file1['title']=='Thorpe Tableau Folder':
# Search for existing files and rename them if they are there
		RemoveFiles(file1['id'])
		
		print file1['title'], file1['mimeType'],file1['id']
		gfile = drive.CreateFile({'title':'Grade1.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Thorpe\Grade1.twbx')
 		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade2.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Thorpe\Grade2.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'Grade3.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Thorpe\Grade3.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'Grade4.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Thorpe\Grade4.twbx')
		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade5.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Thorpe\Grade5.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'GradeK.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Thorpe\GradeK.twbx')
		gfile.Upload()

	elif file1['title']=='Riverside Tableau folder':
		print file1['title'], file1['mimeType'],file1['id']
# Search for existing files and rename them if they are there
		RemoveFiles(file1['id'])
		
		gfile = drive.CreateFile({'title':'Grade1.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Riverside\Grade1.twbx')
 		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade2.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Riverside\Grade2.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'Grade3.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Riverside\Grade3.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'Grade4.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Riverside\Grade4.twbx')
		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade5.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Riverside\Grade5.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'GradeK.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\Riverside\GradeK.twbx')
		gfile.Upload()
		
	elif file1['title']=='District Tableau Folder':
		print file1['title'], file1['mimeType'],file1['id']
# Search for existing files and rename them if they are there
		RemoveFiles(file1['id'])
		
		gfile = drive.CreateFile({'title':'Grade1.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\District\Grade1.twbx')
 		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade2.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\District\Grade2.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'Grade3.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\District\Grade3.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'Grade4.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\District\Grade4.twbx')
		gfile.Upload()
		
		gfile = drive.CreateFile({'title':'Grade5.twbx', "parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\District\Grade5.twbx')
		gfile.Upload()

		gfile = drive.CreateFile({'title':'GradeK.twbx',"parents": [{"kind": "drive#fileLink","id": file1['id']}]})
		gfile.SetContentFile('C:\Users\Elaine\Documents\My Tableau Repository\Workbooks\Danvers\SY16\District\GradeK.twbx')
		gfile.Upload()		




from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from apiclient import errors
from apiclient import http
import sys
import logging

# logging standard out:

class LogFile(object):
    """File-like object to log text using the `logging` module."""

    def __init__(self, name=None):
        self.logger = logging.getLogger(name)

    def write(self, msg, level=logging.INFO):
        self.logger.log(level, msg)

    def flush(self):
        for handler in self.logger.handlers:
            handler.flush()

logging.basicConfig(level=logging.DEBUG, filename='Refresh.log')


# Redirect stdout and stderr
sys.stdout = LogFile('stdout')
sys.stderr = LogFile('stderr')


gauth=GoogleAuth()
gauth.LocalWebserverAuth() #creates local webserver and auto handles authentication

drive= GoogleDrive(gauth)

Danvers_files=(
	'Highlands Fifth Grade Reading Data SY15-16',
	'Highlands First Grade Reading Data SY15-16',
	'Highlands Fourth Grade Reading Data SY15-16',
	'Highlands Kindergarten Reading Data SY15-16',
	'Highlands Second Grade Reading Data SY15-16',
	'Highlands Third Grade Reading Data SY15-16',
	'GO Fifth Grade Reading Data SY15-16',
	'GO First Grade Reading Data SY15-16',
	'GO Fourth Grade Reading Data SY15-16',
	'GO Kindergarten Reading Data SY15-16',
	'GO Second Grade Reading Data SY15-16',
	'GO Third Grade Reading Data SY15-16',
	'Smith Fifth Grade Reading Data SY15-16',
	'Smith First Grade Reading Data SY15-16',
	'Smith Fourth Grade Reading Data SY15-16',
	'Smith Kindergarten Reading Data SY15-16',
	'Smith Second Grade Reading Data SY15-16',
	'Smith Third Grade Reading Data SY15-16',
	'Riverside Fifth Grade Reading Data SY15-16',
	'Riverside First Grade Reading Data SY15-16',
	'Riverside Fourth Grade Reading Data SY15-16',
	'Riverside Kindergarten Reading Data SY15-16',
	'Riverside Second Grade Reading Data SY15-16',
	'Riverside Third Grade Reading Data SY15-16',
	'Thorpe Fifth Grade Reading Data SY15-16',
	'Thorpe First Grade Reading Data SY15-16',
	'Thorpe Fourth Grade Reading Data SY15-16',
	'Thorpe Kindergarten Reading Data SY15-16',
	'Thorpe Second Grade Reading Data SY15-16',
	'Thorpe Third Grade Reading Data SY15-16')

	
#print Danvers_files

file_list = drive.ListFile({'q': "trashed=false"}).GetList()

for file1 in file_list:
	if(file1['title'] in Danvers_files):
		First = file1['title'][:1]
		if( First=='G'):   subdir ='GO'
		elif(First=='S'):  subdir ='SM'
		elif(First=='R'):  subdir ='RS'
		elif(First=='T'):  subdir ='TH'
		elif(First=='H'):  subdir ='HL'
		FileName = '../RawData15-16/'+subdir+'/'+file1['title']+'.csv'
		print 'downloading file...' , FileName
		file1.GetContentFile(FileName,mimetype='text/csv')




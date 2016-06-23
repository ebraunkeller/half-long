# Replaces the data extract

# arg[1] = .twbx file full path
# sys.argv[2]= new extract file full path
# invoke python RemoveFile.py <file1> <file2>

import tempfile
import zipfile
import shutil
import os,sys


def remove_from_zip(zipfname, *filenames):
    tempdir = tempfile.mkdtemp()
    try:
        tempname = os.path.join(tempdir, 'new.zip')
        with zipfile.ZipFile(zipfname, 'r') as zipread:
            with zipfile.ZipFile(tempname, 'w') as zipwrite:
                for item in zipread.infolist():
                    if item.filename not in filenames:
                        data = zipread.read(item.filename)
                        zipwrite.writestr(item, data)
        shutil.move(tempname, zipfname)
    finally:
        shutil.rmtree(tempdir)
		
# main		

TWBX_file = sys.argv[1]
Extract_file = sys.argv[2]
#check for existence of Extract_file and abort if not found
if(os.path.isfile(Extract_file)):
	z=zipfile.ZipFile(TWBX_file,'r')
	names =z.namelist()
	for name in names:
		if (name.startswith('Data/')): 
			new_name =name
			print new_name
		
	remove_from_zip(TWBX_file, new_name) #delete the old data file
	with zipfile.ZipFile(TWBX_file, 'a') as z:
		z.write(Extract_file,new_name) #add in the new data file in the path
		z.close()
else: print 'File not found', Extract_file
	
	

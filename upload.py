#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()

import os


print '''

<form enctype='multipart/form-data' method='post'>
<b>Location:</b>&nbsp;&nbsp;&nbsp;<input type="file" name='filename'/>
<input type='submit' value='Upload'/>
</form>

'''

form=cgi.FieldStorage()

fileitem=form['filename']

if fileitem.filename :

	fn=os.path.basename(fileitem.filename)

	open('/tmp/'+fn,'wb').write(fileitem.file.read())

	message='the file"'+fn+'"was uploaded successfully'

else:

	message='No file uploaded'

print message

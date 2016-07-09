#!/usr/bin/python2


import cgi

print 'content-type:text/html'

print ''

print '''
<!DOCTYPE html>
<html>
<head>
<style>
.but{
	background:blue;
	color:white;
	text-align:center;
	text-decoration:none;
	border-radius:4px;
	border:2px groove blue;
	padding:4px;
}
</style>
</head>
<body>

<div>
<h2 style="color:grey;">Ekeka:</h2>
<form method="post">
<b>CIFS Mode:</b><br /><br />
<p><b>Common Internet File System</b> is a standard way for service <br />
of file storage using <b>Samba Server</b>.It is a non-encrypted method of <br />Ekeka.
</p>

<form method="post">
<input type="radio" name="mode" value="start"/>Create a Bucket<br /><br />
<input type="radio" name="mode" value="stop"/>Extend a Bucket<br /><br />
<input class="but" type="submit" value="Proceed"/>

</form>
</div>
</body>
</html>
'''


conf=cgi.FormContent()
if conf['mode'][0]=="start":
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/startsamba.py\">\n"

elif conf['mode'][0]=="stop":
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/extend.py\">\n"




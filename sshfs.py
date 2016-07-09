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
<b>SSHFS Mode:</b><br /><br />
<p><b>Secure Shell File System</b> is a method for service <br />
of file storage.It is an encrypted method of Ekeka and require<br />
authentication for starting the service.
</p>

<form method="post">
<input type="radio" name="mode" value="start"/>Create a Basket<br /><br />
<input type="radio" name="mode" value="stop"/>Extend a Basket<br /><br />
<input type="radio" name="mode" value="snap"/>Create Snapshot<br /><br />
<input type="radio" name="mode" value="get"/>Get Snapshot<br /><br />
<input class="but" type="submit" value="Proceed"/>

</form>
</div>
</body>
</html>
'''


conf=cgi.FormContent()
if conf['mode'][0]=="start":
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/startsshfs.py\">\n"

elif conf['mode'][0]=="stop":
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/extend.py\">\n"

elif conf['mode'][0]=="snap":
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/snap.py\">\n"

elif conf['mode'][0]=="get":
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/getsnap.py\">\n"



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
Which mode you want to prefer?<br /><br />

<input type="radio" name="proto" value="nfs"/>NFS mode<br /><br />
<input type="radio" name="proto" value="sshfs"/>SSHFS mode<br /><br />

<input class="but" type="submit" value="Next"/>

</form>
</div>
</body>
</html>
'''

conf=cgi.FormContent()
if conf['proto'][0]=="nfs":
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/nfs.py\">\n"

elif conf['proto'][0]=="sshfs":
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/sshfs.py\">\n"





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
<h2 style="color:grey;">Eureka:</h2>
<form method="post">
<b>ISCSI mode:</b><br /><br />
<p><b>ISCSI</b> is a method for service 
of block storage.<br />It is a non-encrypted method of Eureka.
</p>

<form method="post">
<input type="radio" name="mode" value="start"/>Create Block<br /><br />
<input type="radio" name="mode" value="stop"/>Extend Block<br /><br />
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
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/startiscsi.py\">\n"

elif conf['mode'][0]=="stop":
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/extend.py\">\n"

elif conf['mode'][0]=="snap":
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/snap.py\">\n"

elif conf['mode'][0]=="get":
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/getsnap.py\">\n"


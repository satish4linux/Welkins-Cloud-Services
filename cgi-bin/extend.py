#!/usr/bin/python2


import cgi
import commands


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
<b>Extend your Basket:</b><br /><br />
<table>
<tr>
<td><b>Enter basket name:</b></td>
<td><input type="text" name="obj_n" value=""/> </td></tr>
<tr>
<td><b>Enter size to extend(in GB):</b></td>
<td><input type="number" name="size" value=""/></td></tr>
<br />
<tr>
<td><input class="but" type="submit" value="Extend"/></td></tr>
</table>
</form>
</div>
</body>
</html>
'''


conf=cgi.FormContent()
name=conf['obj_n'][0]
size=conf['size'][0]


a=commands.getstatusoutput('sudo lvextend --size +{}G /dev/cloud/{}'.format(size,name))
b=commands.getstatusoutput('sudo resize2fs /dev/cloud/{}'.format(name))

if a[0]==0 and b[0]==0:
	print "<b>Successfully Extended!!</b>"

else:

	print "Extension Failed"




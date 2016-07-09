#!/usr/bin/python2


import cgi
import commands


print 'content-type:text/html'

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
.opt{
	background:grey;
	width:200px;
	color:white;
	border:2px groove grey;
	padding:4px;

}
</style>
</head>
<body>

<div>
<h2 style="color:grey;">Thunder:</h2>
<form method="post">
<b>Choose Your Service:</b><br /><br />
<table>
<tr>
<td><b>Select your choice :</b></td>
<td><select name='service'>
<option class="opt" value=''>------select------</option>
<option class="opt" value='http'>Web Server</option>
<option class="opt" value='ftp'>FTP Server</option>
<option class="opt" value='nfs'>NFS Server</option>
<option class="opt" value='nis'>NIS Server</option>
<option class="opt" value='iscsi'>ISCSI Server</option>
</select></td></tr>
<tr>
<td><input class='but' type='submit' value='submit'/>
</table>
</form>
<br /><b>(Use 'root' as user and 'redhat' as password)</b>
</div>
</body>
</html>
'''

take=cgi.FormContent()

service=take['service'][0]

if service=='http':
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://172.17.0.4:4200\">\n"
elif service=='ftp':
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=https://172.17.0.42:4200\">\n"
elif service=='nfs':
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=https://172.17.0.42:4200\">\n"
elif service=='nis':
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=https://172.17.0.42:4200\">\n"
elif service=='iscsi':
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=https://172.17.0.42:4200\">\n"




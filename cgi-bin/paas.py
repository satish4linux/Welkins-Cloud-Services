#!/usr/bin/python2


import cgi
import commands


print 'content-type:text/html'

print ''

import mysql.connector as mariadb


db=mariadb.connect(user='root',password='redhat',database='welkins')

cursor=db.cursor()

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
<h2 style="color:grey;">Typhoon:</h2>
<form method="post">
<b>Choose Your Platform:</b><br /><br />
<table>
<tr>
<td><b>Select your choice :</b></td>
<td><select name='platform'>
<option class="opt" value=''>------select------</option>
<option class="opt" value='python'>Python</option>
<option class="opt" value='shellscpt'>Shell Scripting</option>
</select></td></tr>
<tr>
<td><input class='but' type='submit' value='submit'/>
</table>
</form>
<br /><b>(Use 'admin' as user and 'redhat' as password)</b>
</div>
</body>
</html>
'''
user=commands.getstatusoutput('cat /var/www/html/user_log')

take=cgi.FormContent()

platform=take['platform'][0]

cursor.execute("INSERT into paas VALUES (%s,%s,'active')",(user[1],platform))

db.commit()

db.close()

if platform=='python':

	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com:12343\">\n"

elif platform=='shellscpt':
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com:12344\">\n"


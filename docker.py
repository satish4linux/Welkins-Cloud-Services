#!/usr/bin/python2


import cgi
import commands
import random


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
<h2 style="color:grey;">Tahoma:</h2>
<form method="post">
<b>Your Requirements:</b><br /><br />
<table>
<tr>
<td><b>Name of Container :</b></td>
<td><input type="text" name="cont" value=""/></td></tr>
<tr>
<td><b>No. of Containers:</b></td>
<td><input type="number" name="quant" value=""/></td>
</tr>
<tr>
<td><input class='but' type='submit' value='submit'/>
</table>
</form>
</div>
</body>
</html>
'''

user=commands.getstatusoutput('cat /var/www/html/user_log')

caas=cgi.FormContent()

cont=caas['cont'][0]
quant=caas['quant'][0]

i=1

while i<=int(quant) :
	port=str(random.randint(8000,15000))
	commands.getstatusoutput('sudo docker run -itd --name {1}{0} -v /root/Desktop:/{1}{0} -p {2}:4200 magical'.format(i,cont,port))
	ipm=commands.getstatusoutput('sudo docker inspect {1}{0} | grep IPAddress '.format(i,cont))
	splits=ipm[1].split(' ')
	ip=splits[len(splits) -1]
	s=ip.strip('",')

	print '<b>IPAddress : {0}</b>&nbsp;&nbsp;&nbsp;&nbsp;<a href=http://www.welkins.com:{1} style="text-decoration:none;color:red;"><b>Click Here</b></a><br />\n'.format(s,port)
	print "<b>Username :admin<br /> Password :'redhat'</b><br /><br />\n"
	
	commands.getstatusoutput('sudo docker exec  -t {0}{1} python /caas.py'.format(cont,quant))
	
	cursor.execute("INSERT into caas VALUES (%s,%s,'active')",(user[1],cont+quant))

	db.commit()

	db.close()
	
	i+=1



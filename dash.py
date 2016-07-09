#!/usr/bin/python2


import cgi
import commands
import cgitb
cgitb.enable()
import mysql.connector as mariadb

print 'content-type:text/html'

print ''

user=commands.getstatusoutput('cat /var/www/html/user_log')
name=user[1]

db=mariadb.connect(user='root',password='redhat',database='welkins')
cursor=db.cursor()


cursor.execute("SELECT count(software) FROM saas WHERE user=%s and state='active' ",(name,))

row1=cursor.fetchall()


for i in row1:
	software=i[0]

cursor.close()

cursor=db.cursor()
cursor.execute("SELECT count(obj_n) FROM obj WHERE user=%s and state='active' ",(name,))

row1=cursor.fetchall()


for j in row1:
	obj=j[0]

cursor.close()

cursor=db.cursor()
cursor.execute("SELECT count(blk_n) FROM blk WHERE user=%s and state='active' ",(name,))

row1=cursor.fetchall()


for k in row1:
	blk=k[0]

cursor.close()

cursor=db.cursor()
cursor.execute("SELECT count(name) FROM iaas WHERE user=%s and state='active' ",(name,))

row1=cursor.fetchall()


for l in row1:
	os=l[0]

cursor.close()

cursor=db.cursor()
cursor.execute("SELECT count(platform) FROM paas WHERE user=%s and state='active' ",(name,))

row1=cursor.fetchall()


for m in row1:
	platform=m[0]

cursor.close()

cursor=db.cursor()
cursor.execute("SELECT count(cont_n) FROM caas WHERE user=%s and state='active' ",(name,))

row1=cursor.fetchall()


for n in row1:
	container=n[0]

cursor.close()

db.close()

print '''
<!DOCTYPE html>
<html>
<head>
<style>
.back
{
background:url('http://www.welkins.com/bg2.jpg') repeat-x;
height:30px;
width:200px;
color:white;
v-align:center;
padding:5px;
}
</style>
</head>
<body>
<div style='width:900px;height:450px'>
<h3 style='color:black;'>Your Current Session:</h3>
<br/><br/>
<font class='back'><b>Softwares in use:</b></font><span style='color:blue;font-size:25px;'><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'''+str(software)+'''</b></span>
<br/><br/>
<font class="back"><b>Object Storages in use:</b></font><span style="color:blue;font-size:25px;"><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'''+str(obj)+'''</b></span>
<br/><br/>
<font class="back"><b>Block Storages in use:</b></font><span style="color:blue;font-size:25px;"><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'''+str(blk)+'''</b></span>
<br/><br/>
<font class="back"><b>Operating Systems in use:</b></font><span style="color:blue;font-size:25px;"><b>&nbsp;&nbsp;&nbsp;'''+str(os)+'''</b></span>
<br/><br/>
<font class="back"><b>IDEs in use:</b></font><span style="color:blue;font-size:25px;"><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'''+str(platform)+'''</b></span>
<br/><br/>
<font class="back"><b>Containers in use:</b></font><span style="color:blue;font-size:25px;"><b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'''+str(container)+'''</b></span>
<br/><br/>
</div>
</body>
'''


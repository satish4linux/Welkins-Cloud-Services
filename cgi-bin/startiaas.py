#!/usr/bin/python2


import cgi
import commands
import os
import cgitb
cgitb.enable()


print 'content-type:text/html'

print ''

import mysql.connector as mariadb


db=mariadb.connect(user='root',password='redhat',database='welkins')

cursor=db.cursor()

user=commands.getstatusoutput('cat /var/www/html/user_log')


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

.opt{
	background:grey;
	width:170px;
	color:white;
	border:2px groove grey;
	padding:4px;
}
</style>
</head>
<body>

<div>
<h2 style="color:grey;">Katrina:</h2>
<form method="post" enctype="multipart/form-data" >
<b>Your Requirements:</b><br /><br />
<table>
<tr>
<td><b>Name of Instance:</b></td>
<td><input type="text" name="name" value=""/> </td></tr>
<tr>
<td><b>Memory Size(in Mb):</b></td>
<td><input type="text" name="mem" value=""/></td></tr>
<tr>
<td><b>No. of CPUs:</b></td>
<td><input type="text" name="cpu" value=""/></td></tr>
<tr>
<td><b>Disk Name:</b></td>
<td><input type="text" name="dname" value=""/></td></tr>
<tr>
<td><b>Disk Size:</b></td>
<td><input type="text" name="disk" value=""/></td></tr>
<tr>
<td><b>OS Type:</b></td>
<td><select name='os'>
<option class="opt" value=''>------select------</option>
<option class="opt" value='linux'>Linux</option>
<option class="opt" value='windows'>Windows</option>
</select></td></tr>
<tr>
<td><b>OS Variant:</b></td>
<td><select name='os_var'>
<option class="opt" value=''>------select------</option>
<option class="opt" value='rhel7'>Red Hat</option>

<option class="opt" value='win'>Windows 10</option>
</select></td></tr>
<br />
<tr>
<td><input class="but" type="submit" value="Launch"/></td></tr>
</table>
</form>
</div>
</body>
</html>

'''

conf=cgi.FieldStorage()

name=conf.getvalue('name')
mem=conf.getvalue('mem')
cpu=conf.getvalue('cpu')
dname=conf.getvalue('dname')
disk=conf.getvalue('disk')
os=conf.getvalue('os')
os_var=conf.getvalue('os_var')


if os=="linux":

	commands.getstatusoutput('sudo  ln /var/lib/libvirt/images/red.img /var/lib/libvirt/images/{}.img'.format(dname))

	x=commands.getstatusoutput('sudo virt-install --import --hvm --name {} --memory {} --vcpus {} --disk /var/lib/libvirt/images/{}.img,size={} --graphics vnc,listen=0.0.0.0,port=5999 --noautoconsole'.format(name,mem,cpu,dname,disk))


	if x[0] == 0:
		print "Successfull!!!"

		cursor.execute("INSERT into caas VALUES (%s,%s,'active')",(user[1],name))

		db.commit()

		db.close()


		print "<br/><br/><a href='http://www.welkins.com/vnc/index.html?ip=192.168.43.50&port=5555' target='_blank' style='color:red;text-decoration:none;'><b>Get Console</b></a>"

elif os=="windows":

	commands.getstatusoutput('sudo  ln /var/lib/libvirt/images/win.qcow2 /var/lib/libvirt/images/{}.img'.format(dname))

	x=commands.getstatusoutput('sudo virt-install --import --hvm --name {} --memory {} --vcpus {} --disk /var/lib/libvirt/images/{}.img,size={} --graphics vnc,listen=0.0.0.0,port=5999 --noautoconsole'.format(name,mem,cpu,dname,disk))


	if x[0] == 0:
		print "Successfull!!!"

		cursor.execute("INSERT into caas VALUES (%s,%s,'active')",(user[1],name))

		db.commit()

		db.close()


		print "<br/><br/><a href='http://www.welkins.com/vnc/index.html?ip=192.168.43.50&port=5555' target='_blank' style='color:red;text-decoration:none;'><b>Get Console</b></a>"







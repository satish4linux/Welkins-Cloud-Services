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
}
</style>
</head>
<body>

<div>
<h2 style="color:grey;">Ekeka:</h2>
<form method="post">
<b>CIFS mode:</b><br /><br />
<table>
<tr>
<td><b>Enter size of Basket:</b></td>
<td><input type="text" name="size" value=""/> </td></tr>
<tr>
<td><b>Enter Basket name:</b></td>
<td><input type="text" name="obj_n" value=""/></td></tr>
<tr>
<td><b>Enable Snapshot</b></td>
<td><input type="checkbox" name="snap" value=""/></td></tr>
<br />
<tr>
<td><input class="but" type="submit" value="Launch"/></td></tr>
</table>
</form>
</div>
</body>
</html>
'''
user=commands.getstatusoutput('cat /var/www/html/user_log')

conf=cgi.FormContent()
size=conf['size'][0]
name=conf['obj_n'][0]
passwd='redhat'
commands.getstatusoutput('sudo lvcreate --size {0} --name {1} /dev/cloud'.format(size,name))
commands.getstatusoutput('sleep 1')
commands.getstatusoutput('sudo mkfs.ext4 /dev/cloud/{}'.format(name))
commands.getstatusoutput('sleep 1')
commands.getstatusoutput('sudo mkdir /media/{}'.format(name))
commands.getstatusoutput('sudo mount /dev/cloud/{0} /media/{0}'.format(name))
commands.getstatusoutput('sleep 1')
commands.getstatusoutput('sudo chmod o+w /media/{}'.format(name))

x=open('/etc/samba/smb.conf',mode='a')
x.write('\n\t['+name+']\n')
x.write('\tpath=/media/'+name+'\n')
x.write('\twritable=yes\n')
x.close()
commands.getstatusoutput('sudo useradd -s /sbin/nologin   {}'.format(name))
commands.getstatusoutput('sudo echo -e {1}\{1} | sudo smbpasswd -a {0}'.format(name,passwd))
commands.getstatusoutput('sleep 3')
commands.getstatusoutput('sudo systemctl restart smb')

commands.getstatusoutput('sudo touch /{}.sh'.format(name))
commands.getstatusoutput('sudo chmod 777 /{}.sh'.format(name))
x=open('/{}.sh'.format(name),mode='w')
x.write('#!/usr/bin/bash\n\n')
x.write('yum install cifs-utils -y\n')
x.write('mkdir /media/'+name+'\n')
x.write('mount -o username='+name+' //www.welkins.com/'+name+'  /media/'+name+'\n')
x.close()
commands.getstatusoutput('sudo tar -cvf /{0}.tar /{0}.sh'.format(name))
commands.getstatusoutput('sudo mv /{}.tar /var/www/html/'.format(name))

cursor.execute("INSERT into obj VALUES (%s,%s,'active')",(user[1],name))

db.commit()

db.close()

print "Successfull!!!"
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/{}.tar\">\n".format(name)


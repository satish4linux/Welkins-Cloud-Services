#!/usr/bin/python2


import cgi
import commands


print 'content-type:text/html'

print ''

user=commands.getstatusoutput('sudo cat /var/www/html/user_log')

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
<b>Get your Snapshot:</b><br /><br />
<table>
<tr>
<td><b>Enter snapshot name:</b></td>
<td><input type="text" name="obj_n" value=""/> </td></tr>

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

commands.getstatusoutput('sudo mkfs.ext4 /dev/cloud/{}'.format(name))
commands.getstatusoutput('sleep 3')
commands.getstatusoutput('sudo mkdir /media/{}'.format(name))
commands.getstatusoutput('sudo mount /dev/cloud/{0} /media/{1}'.format(name,name))
commands.getstatusoutput('sleep 3')
commands.getstatusoutput('sudo echo "/media/{}   *(rw,no_root_squash)" >> /etc/exports'.format(name))
det=commands.getstatusoutput('sudo systemctl restart nfs-server')
commands.getstatusoutput('sudo touch /{}.sh'.format(user[1]))
commands.getstatusoutput('sudo chmod 777 /{}.sh'.format(user[1]))
x=open('/{}.sh'.format(name),mode='w')
x.write('#!/usr/bin/bash\n\n')
x.write('mkdir /media/'+user[1]+'\n')
x.write('mount www.welkins.com:/media/'+name+' /media/'+user[1]+'\n')
x.write
x.close()
a=commands.getstatusoutput('sudo tar -cvf /{0}.tar /{0}.sh'.format(name))
b=commands.getstatusoutput('sudo mv /{}.tar /var/www/html/'.format(name))

if a[0]==0 and b[0]==0:
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/{}.tar\">\n".format(name)

else:

	print "Connection Failed"




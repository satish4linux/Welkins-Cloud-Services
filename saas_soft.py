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


<h2 style="color:grey;">Halola:</h2>
<b>Get a Software:</b><br /><br /><br />
<form method="post">
<input type="radio" name="software" value="firefox"><img src="http://www.welkins.com/unnamed(2).png" width="100px" height="100px"/>&nbsp;&nbsp;&nbsp;
<input type="radio" name="software" value="vlc"><img src="http://www.welkins.com/unnamed.png" width="100px" height="100px"/>&nbsp;&nbsp;&nbsp;
<input type="radio" name="software" value="gedit"><img src="http://www.welkins.com/unnamed(3).png" width="100px" height="100px"/>&nbsp;&nbsp;&nbsp;
<input type="radio" name="software" value="vnc"><img src="http://www.welkins.com/unnamed(1).png" width="100px" height="100px"/><br /><br />
<input class="but" type="submit" value="Launch"/>
</form>
</body>
</html>
'''

user=commands.getstatusoutput('cat /var/www/html/user_log')
name=user[1]

soft=cgi.FormContent()
software=soft['software'][0]

#inserting into the database

cursor.execute("INSERT into saas VALUES (%s,%s,'active')",(name,software))

db.commit()

db.close()

if software=="firefox":

	commands.getstatusoutput('sudo touch /{}.sh'.format(software))
	commands.getstatusoutput('sudo chmod 777 /{}.sh'.format(software))
	x=open('/{}.sh'.format(software),mode='w')
	x.write('#!/usr/bin/bash\n\n')
	x.write('ssh -X '+name+'@www.welkins.com firefox\n')
	x.write('sleep 3\n')
	x.close()
	commands.getstatusoutput('sudo tar -cvf /{0}.tar /{0}.sh'.format(software))
	commands.getstatusoutput('sudo mv /{}.tar /var/www/html/'.format(software))


	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/{}.tar\">\n".format(software)

elif software=="vlc":

	commands.getstatusoutput('sudo touch /{}.sh'.format(software))
	commands.getstatusoutput('sudo chmod 777 /{}.sh'.format(software))
	x=open('/{}.sh'.format(software),mode='w')
	x.write('#!/usr/bin/bash\n\n')
	x.write('ssh -X '+name+'@www.welkins.com vlc\n')
	x.write('sleep 3\n')
	x.close()
	commands.getstatusoutput('sudo tar -cvf /{0}.tar /{0}.sh'.format(software))
	commands.getstatusoutput('sudo mv /{}.tar /var/www/html/'.format(software))


	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/{}.tar\">\n".format(software)

elif software=="gedit":

	commands.getstatusoutput('sudo touch /{}.sh'.format(software))
	commands.getstatusoutput('sudo chmod 777 /{}.sh'.format(software))
	x=open('/{}.sh'.format(software),mode='w')
	x.write('#!/usr/bin/bash\n\n')
	x.write('ssh -X '+name+'@www.welkins.com gedit\n')
	x.write('sleep 3\n')
	x.close()
	commands.getstatusoutput('sudo tar -cvf /{0}.tar /{0}.sh'.format(software))
	commands.getstatusoutput('sudo mv /{}.tar /var/www/html/'.format(software))


	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/{}.tar\">\n".format(software)

elif software=="vnc":

	commands.getstatusoutput('sudo touch /{}.sh'.format(software))
	commands.getstatusoutput('sudo chmod 777 /{}.sh'.format(software))
	x=open('/{}.sh'.format(software),mode='w')
	x.write('#!/usr/bin/bash\n\n')
	x.write('ssh -X '+name+'@www.welkins.com vncviewer\n')
	x.write('sleep 3\n')
	x.close()
	commands.getstatusoutput('sudo tar -cvf /{0}.tar /{0}.sh'.format(software))
	commands.getstatusoutput('sudo mv /{}.tar /var/www/html/'.format(software))


	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/{}.tar\">\n".format(software)



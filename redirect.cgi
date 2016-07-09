#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()


detail=cgi.FormContent()
user=detail['user'][0]
password=detail['password'][0]

print "content-type:text/html"

print ""

x=open('/var/www/html/user_log',mode='w')
x.write('{}'.format(user))
x.close()

import mysql.connector as mariadb


db=mariadb.connect(user='root',password='redhat',database='welkins')

cursor=db.cursor()


cursor.execute("SELECT password FROM login WHERE user=%s",(user,))

row=cursor.fetchall()

cursor.close()
db.close()



for i in row:
	passwd=i[0]
		

if passwd==password :

	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/dashboard.py\">\n"

else:
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/login.py\">\n"




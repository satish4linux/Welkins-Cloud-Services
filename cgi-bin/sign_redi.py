#!/usr/bin/python

import cgi

import commands
import cgitb
cgitb.enable()

import mysql.connector as mariadb
db=mariadb.connect(user='root',password='redhat',database='welkins')

cursor=db.cursor()
#getting data from the above registration form

detail=cgi.FormContent()


f_name=detail['f_name'][0]
l_name=detail['l_name'][0]
user=detail['user'][0]
password=detail['password'][0]
email=detail['email'][0]
contact=detail['contact'][0]


x=open('/var/www/html/user_log',mode='w')
x.write('{}'.format(user))
x.close()

print "content-type:text/html"

print ""

#inserting into the database

cursor.execute("INSERT into login VALUES (%s,%s,%s,%s,%s,%s)",	(f_name,l_name,user,password,email,contact))

db.commit()

db.close()

#creating user in the cloud server

commands.getstatusoutput('sudo useradd {}'.format(user))
commands.getstatusoutput('sudo echo {} | sudo passwd {} --stdin'.format(password,user))


print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/dashboard.py\">\n"




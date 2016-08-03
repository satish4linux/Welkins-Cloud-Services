#!/usr/bin/python

import cgi,sys
import cgitb
cgitb.enable()
from pymongo import Connection
from pymongo.errors import ConnectionFailure

try:
	c=Connection(host='192.168.43.50',port=27017)
	print "Connected Successfully"

except ConnectionFailure, e:
	sys.stderr.write("Connection Failure : %s" %e)
	sys.exit(1)

print "content-type:text/html"

print ""

detail=cgi.FormContent()

roll=detail['roll'][0]

name=detail['name'][0]

password=detail['pass'][0]

user_1={
	'name':name,
	'roll':roll,
	'pass':password
}



#!/usr/bin/python

import Cookie
import cgi
import cgitb
cgitb.enable()

#create the cookie

c=Cookie.SimpleCookie()

#assign a value

c['user']='shiv'

#set the expires time

c['user']['expires']=1*1*3*60*60



print "content-type:text/html"

print ""

print c

#!/usr/bin/python


import os,cgi
import cgitb
cgitb.enable()

print "content-type:text/html"

print ""

form=cgi.FieldStorage()

fileitem=form['filename']
name=form.getvalue('name')
detail=form.getvalue('detail')

print fileitem.filename

print name

print detail


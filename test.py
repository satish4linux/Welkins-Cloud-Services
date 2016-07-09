#!/usr/bin/python2


import cgi
import commands


print "content-type:text/html"

print ""

commands.getstatusoutput('sudo docker run -it --name sat /root/Desktop:/sat shellindb')
x=open('/etc/sysconfig/shellinaboxd',mode='a')


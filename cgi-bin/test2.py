#!/usr/bin/python2


import cgi
import cgitb
import commands
cgitb.enable()


print "content-type:text/html"

print ""

name='dpk1'
mem='1024'
cpu='1'
dname='dpk1'
disk='6G'
os='linux'
os_var='rhel7'


commands.getstatusoutput('sudo touch /{}.img'.format(dname))
commands.getstatusoutput('sleep 3')
x=commands.getstatusoutput('sudo virt-install --name {} --memory {} --vcpus {} --os-type {} --os-var {} --cdrom /root/Desktop/images/rhel-server-7.2-x86_64-dvd.iso --disk /root/Desktop/sat/redhat.img,size={}'.format(name,mem,cpu,os,os_var,disk))
commands.getstatusoutput('sleep 3')

if x==0:
	print "Successfull!!!"
else:
	print "not"




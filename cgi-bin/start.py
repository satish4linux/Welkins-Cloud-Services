#!/usr/bin/python

import commands

print "content-type:text/html"

print ""

commands.getstatusoutput('sudo virsh start windows')

print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/cgi-bin/gallery.py\">\n"

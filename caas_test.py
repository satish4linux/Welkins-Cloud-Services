#!/usr/bin/python

import os
import commands


print "content-type:text/html"

print ""

cont='sat'
quant='2'
commands.getstatusoutput('sudo docker run -itd --name {1}{0} -v /root/Desktop:/{1}{0} magical'.format(quant,cont))

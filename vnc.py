#!/usr/bin/python2

import cgi
import commands

commands.getstatusoutput('sshpass -p redhat ssh -X root@192.168.43.18 vncviewer')

raw_input()

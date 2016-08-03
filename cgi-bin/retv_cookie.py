#!/usr/bin/python

import cgi
import os
import Cookie

print "content-type:text/html"

print ""

if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=Cookie.SimpleCookie()
	c.load(cookie_string)

	try:
		data=c['user'].value

		print "cookie data: "+data+"<br />"
	
	except KeyError:

		print "The cookie was not set or has been expired"



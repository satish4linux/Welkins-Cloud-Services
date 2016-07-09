#!/usr/bin/python

import cgi

print "content-type:text/html"

print ""

print '''
<!DOCTYPE html>
<html>
<head>
<style>
.but{
	background:blue;
	color:white;
	text-align:center;
	text-decoration:none;
	border-radius:4px;
	border:2px groove blue;
	padding:4px;
}
</style>
</head>
<body>
<div>
<h2 style="color:grey;">Halola</h2>
<p><b>Halola</b> is that service of WCS where you can get a <b>software<br />
on demand</b> ,anytime,anywhere.We care about your interest<br /> and try to
provide those softwares which you need almost<br /> everyday.
</p>
<br /><br/>
<a class="but" href="http://www.welkins.com/cgi-bin/dash.py"><b>Go to Dashboard</b></a>&nbsp;&nbsp;
<a class="but" href="http://www.welkins.com/cgi-bin/saas_soft.py"><b>Proceed >>></b></a>
</div>
</body>
</html>
'''















#!/usr/bin/python2


import cgi

print 'content-type:text/html'

print ''

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
	padding:10px;
}
</style>
</head>
<body>

<div>
<h2 style="color:grey;">Katrina:</h2>
<b>Welcome to Katrina Services!!!</b>
<br /><br />
<br /><br />
<a class="but" href="http://www.welkins.com/cgi-bin/gallery.py"><b>Visit OS Gallery</b></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a class="but" href="http://www.welkins.com/cgi-bin/startiaas.py"><b>Launch Custom OS</b></a>
</div>
</body>
</html>
'''


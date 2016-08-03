#!/usr/bin/python


import cgi
import cgitb
cgitb.enable()


print "content-type:text/html"

print ""

print '''

<!DOCTYPE html>
<html>
<head>
<style>
iframe#fset{
	width:300px;
	height:300px;
	border:3px groove grey;
	border-radius:4px;
	z-index:1;
	box-shadow:0px 0px 10px black;
}
div#frame{
	position:relative;
	float:left;
	margin:20px;
	z-index:0;
}
</style>
</head>
<body>

<div id='frame'>
<div id='os'>
<iframe id="fset" src="http://192.168.43.50/vnc/index.html?ip=192.168.43.50&port=7778"></iframe>
</div>
<div id='os_detail'><center><br />
<a href="http://www.welkins.com/cgi-bin/start.py"><img src='http://www.welkins.com/play.png' width='30px' height='30px'/></a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="http://www.welkins.com/cgi-bin/shutdown.py"><img src='http://www.welkins.com/shutdown.png' width='30px' height='30px'></a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="http://192.168.43.50/vnc/index.html?ip=192.168.43.50&port=7778" target="_blank" ><img  src='http://www.welkins.com/fullscreen.png' width='20px' height='20px'></a>
</center><br />
<center><b>Windows 10</b></center>
</div>
</div>
<div id='frame'>
<div id='os'>
<iframe id="fset" src="http://192.168.43.50/vnc/index.html?ip=192.168.43.50&port=7777"></iframe>
</div>
<div id='os_detail'>
<center><br />
<a href="http://www.welkins.com/cgi-bin/startr.py"><img src='http://www.welkins.com/play.png' width='30px' height='30px'/></a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="http://www.welkins.com/cgi-bin/shutdownr.py"><img src='http://www.welkins.com/shutdown.png' width='30px' height='30px'></a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href="http://192.168.43.50/vnc/index.html?ip=192.168.43.50&port=7777" target="_blank" ><img src='http://www.welkins.com/fullscreen.png' width='20px' height='20px'></a>
</center><br />
<center><b>Redhat Linux</b></center></div>
</div>

</body>
</html>
'''


#!/usr/bin/python2


import cgi

print "content-type:text/html"

print ""

print '''
<!DOCTYPE html>
<html>
<head>
<title>
Dashboard-Welkins Cloud Services
</title>
<link rel="stylesheet" type="text/css" href="http://192.168.43.18/styles.css" />
</head>
<body>

<!---the header of the page --->

<div class="top">
<div class="topleft">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<font size="40"><b><i>Welkins</i></b></font>&nbsp;&nbsp;&nbsp;&nbsp;<sup style="vertical-align:super;font-size:20px;"><b><i>Cloud services</i></b></sup>
</div>

</div>

<!---the menu code --->

<div class="mainHeader">
	<nav><ul>
		<li class="active"><a href="http://www.welkins.com/index.html">HOME</a></li>
		<li><a href="#">MY SERVICES</a></li>
		<li><a href="#">MY ACCOUNT</a></li>
		<li><a href="#">ABOUT WELKINS</a></li>
		<li><a href="#">FEEDBACK</a></li>
	</ul></nav>
</div>
<div class="content">
<div class="welcome">

'''
getn=cgi.FormContent()
print "<span style='margin-left:1100px;color:white;font-size:20px;'><b>Hii "+getn['name'][0]+" !!!!</b></span>"


print '''
</div>
<div class="droplist">
<div class='left'>

<a class='amenu' href='http://192.168.43.18/cgi-bin/dash.py' target='main'>Dashboard</a>
<a class='amenu' href='http://192.168.43.18/saas_intro.html' target='main'>Halola</a>
<a class='amenu' href='http://192.168.43.18/obj.html' target="main">Ekeka</a>
<a class='amenu' href='http://192.168.43.18/blk.html' target="main">Eureka</a>
<a class='amenu' href='http://192.168.43.18/iaas.html' target='main'>Katrina</a>
<a class='amenu' href='http://192.168.43.18/paas.html' target='main'>Typhoon</a>
<a class='amenu' href='http://192.168.43.18/caas.html' target='main'>Tahoma</a>
</div>
</div>
<div class="dash">
<iframe width="100%" height="100%" style="border:0px;" name="main">

</iframe>

</div>
</div>



<div class="foot">
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<div class="part">
<ul style="list-style-type:none;font-family:Copperplate Gothic;color:white;">
<li style="font-size:20px;"><b>Contact Us :</b></li><br />
<li style="font-size:15px;">National Institute of Technology,Patna</li>
<li style="font-size:15px;">Ashok Rajpath,Mahendru</li>
<li style="font-size:15px;">Patna,Bihar-800005</li>
</ul>
</div>
<div class="part">
<ul style="list-style-type:none;font-family:Copperplate Gothic;color:white;">
<li style="font-size:22px;"><b>Our Policy :</b></li><br />
<li style="font-size:15px;">General Policy</li>
<li style="font-size:15px;">Refund Policy</li>
<li style="font-size:15px;">Pricing Policy</li>
</ul>
</div>
<div class="part">
<ul style="list-style-type:none;font-family:Copperplate Gothic;color:white;">
<li style="font-size:22px;"><b>Connect us :</b></li><br />
<li style="font-size:15px;">Facebook</li>
<li style="font-size:15px;">Twitter</li>
<li style="font-size:15px;">Youtube</li>
</ul>
</div>
</div>

</body>
</html>
'''

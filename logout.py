#!/usr/bin/python2


import os
import commands
import cgi
import cgitb
cgitb.enable()

import mysql.connector as mariadb

use=commands.getstatusoutput('sudo cat /var/www/html/user_log')
user=use[1]
db=mariadb.connect(user='root',password='redhat',database='welkins')

cursor=db.cursor()

cursor.execute('delete from saas where user=%s',(user,))
cursor.close()

cursor=db.cursor()

cursor.execute('delete from obj where user=%s',(user,))
cursor.close()

cursor=db.cursor()

cursor.execute('delete from blk where user=%s',(user,))
cursor.close()

cursor=db.cursor()

cursor.execute('delete from iaas where user=%s',(user,))
cursor.close()

cursor=db.cursor()

cursor.execute('delete from paas where user=%s',(user,))
cursor.close()

cursor=db.cursor()

cursor.execute('delete from caas where user=%s',(user,))
cursor.close()

db.commit()
db.close()


print "content-type:text/html"

print ""


print '''
<!DOCTYPE html>
<html>
<head>
<title>
Dashboard-Welkins Cloud Services
</title>
<link rel="stylesheet" type="text/css" href="http://www.welkins.com/styles.css" />
<style>
div#mid{
	position:relative;
	width:100%;
	height:275px;
}
</style>
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
		<li><a href="http://www.welkins.com/index.html">HOME</a></li>
		<li><a href="#">MY SERVICES</a></li>
		<li><a href="#">MY ACCOUNT</a></li>
		<li><a href="#">ABOUT WELKINS</a></li>
		<li><a href="#">FEEDBACK</a></li>
	</ul></nav>
</div>


<div id='mid'>
<center>
<font style="color:grey;font-size:20px;" ><b>You are Successfully logged out.<a href="http://www.welkins.com/cgi-bin/login.py" style="color:red;text-decoration:none;">Click here</a> to login.</b></font>
</center>
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

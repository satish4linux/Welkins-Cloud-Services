#!/usr/bin/python2

import cgi

print "content-type:text/html"

print ""

print '''

<!DOCTYPE html>
<html>
<head>
<title>
SignUp-Welkins Cloud Services
</title>
<link rel="stylesheet" type="text/css" href="http://www.welkins.com/styles.css"/>
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
<center>
<div class="signport">
<center>
<form method="POST" action="http://www.welkins.com/cgi-bin/sign_redi.py">
<fieldset style="border-radius:4px;margin:10px;border:3px groove;padding : 10px;">
<legend><h2> Personal Details:</h2></legend>
<table>
<tr>
<td class="key">First Name</td> 
<td><input class="in" placeholder="enter first name" name="f_name" size="30" type="text"></td>
</tr>
<tr>
<td class="key">Last Name</td>
<td><input class="in" placeholder="enter last name" type="text" size="30" name="l_name"></td>
</tr>
<tr>
<td class="key">Username</td>
<td><input class="in" placeholder="enter username" type="text" size="30" name="user"></td>
</tr>
<tr>
<td class="key">Password</td>
<td><input class="in" placeholder="enter password" type="password" size="30" name="password"></td>
</tr>
<tr>
<td class="key">Email</td>
<td><input class="in" placeholder="enter email" type="text" size="30" name="email"></td>
</tr>
<tr>
<td class="key">Contact</td>
<td><input class="in" placeholder="enter contact" type="text" size="30" name="contact"></td>
</tr>
<tr>
<td>
<input type="submit" value="Register" style="width:100px;height:35px;color:white;font-size:20px;background:grey;border-radius:10px;">
</td>
<td>

<input type="reset" value="Reset" style="width:100px;height:35px;color:white;font-size:20px;background:grey;border-radius:10px;">
</td>
</tr>
</table>
</fieldset>
</form>
</center>
</div>
</center>
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


#!/usr/bin/python

import cgi,random
from commands import getstatusoutput
import cgitb
cgitb.enable()

import os

print "content-type:text/html"

print ""

form=cgi.FieldStorage()

fileitem=form['filename']
name=form.getvalue('name')
detail=form.getvalue('detail')

if fileitem.filename :

	fn=os.path.basename(fileitem.filename)

	open('/tmp/'+fn,'wb').write(fileitem.file.read())

	key=random.randint(1,100000)

	fold=getstatusoutput('sudo echo {} | sudo md5sum | sudo head -c 10'.format(key))
	folder=fold[1]

	path='/var/www/html/home4u/files/bin/'
	getstatusoutput('sudo mkdir {}{}'.format(path,folder))
	getstatusoutput('sudo mv /tmp/{1} {0}{2} '.format(path,fn,folder))
	getstatusoutput('sudo cp /var/www/html/home4u/files/images/back.png {}{}'.format(path,folder))
	getstatusoutput('sudo touch {}{}/welcome.html'.format(path,folder))
	getstatusoutput('sudo chmod 777 {}{}/welcome.html'.format(path,folder))
	x=open('{}{}/welcome.html'.format(path,folder),mode='w')
	x.write('<!DOCTYPE html>\n')
	x.write('<html>\n')
	x.write('<head>\n')
	x.write('<title>\n')
	x.write('Welcome to Dark-knight\'s Browser\n')
	x.write('</title>\n')
	x.write('<style>\n')
	x.write('html{\n')
	x.write('background:url(back.png) no-repeat center center fixed;\n')
	x.write('-moz-background-size: cover;\n')
	x.write('background-size:cover;}\n')
	x.write('div#intro{\n')
	x.write('position:relative;\n')
	x.write('top:50px;\n')
	x.write('float:left;}\n')
	x.write('img#image{\n')
	x.write('border-radius:150px;}\n')
	x.write('div#search{\n')
	x.write('position:relative;\n')
	x.write('float:left;\n')
	x.write('top:350px;\n')
	x.write('left:100px;}\n')
	x.write('input#box{\n')
	x.write('border-radius:5px;\n')
	x.write('width:500px;\n')
	x.write('height:30px;\n')
	x.write('box-shadow: 0px 0px 5px white;\n')
	x.write('font-size:20px;}\n')
	x.write('input#but{\n')
	x.write('width:200px;\n')
	x.write('font-size:20px;\n')
	x.write('color:maroon;}\n')
	x.write('div#links{\n')
	x.write('position:relative;\n')
	x.write('top:45px;\n')
	x.write('float:left;\n')
	x.write('left:250px;}\n')
	x.write('h3.lnk{\n')
	x.write('color:white;\n')
	x.write('left:0px;\n')
	x.write('box-shadow: 0px 0px 5px white;}\n')
	x.write('h3.lnk:hover{\n')
	x.write('color:red;\n')
	x.write('left:3px;}\n')
	x.write('</style>\n')
	x.write('</head>\n')
	x.write('<body><center>\n')
	x.write('<h1 style="color:white;font-family:\'Helvetica\';margin-top:\'20px\';">Welcome to Dark Knight\'s Browser !!!</h1>\n')
	x.write('</center>\n')
	x.write('<div id="intro">\n')
	x.write('<img id="image" src="'+fn+'" width=300px height=300px/><br/><br />\n')
	x.write('<span style="color:white;font-family:\'Arial\';font-size:25px;"><b>{0}</b><br /><span style="font-size:20px;">{1}</span></span>\n'.format(name,detail))
	x.write('</div>\n')
	x.write('<div id="search">\n')
	x.write('<center>\n')
	x.write('<span style="color:white;font-size:25px;"><b>Google Down:</b></span><br /><br />\n')
	x.write('<form method="get" action="http://www.google.com/search">\n')
	x.write('<input type="text" id="box" name="q" value="" placeholder="search here...."/><br /><br />\n')
	x.write('<input id="but" type="submit" value="Google...!!!"/>\n')
	x.write('</form>\n')
	x.write('</center>\n')
	x.write('</div>\n')
	x.write('<div id="links">\n')
	x.write('<h2 style="color:white;">Important Links:</h2>\n')
	x.write('<center>\n')
	x.write('<a href="http://www.facebook.com/" style="text-decoration:none;" ><h3 class="lnk">Facebook</h3></a>\n')
	x.write('<a href="http://www.gmail.com/" style="text-decoration:none;" ><h3 class="lnk" >Gmail</h3></a>\n')
	x.write('<a href="http://www.linkedin.com/" style="text-decoration:none;" ><h3 class="lnk">Linked In</h3></a>\n')
	x.write('<a href="http://www.twitter.com/" style="text-decoration:none;" ><h3 class="lnk" >Twitter</h3></a>\n')
	x.write('<a href="http://www.github.com/" style="text-decoration:none;" ><h3 class="lnk">Git Hub</h3></a>\n')
	x.write('<a href="http://www.quora.com/" style="text-decoration:none;" ><h3 class="lnk" >Quora</h3></a>\n')
	x.write('<a href="http://www.instagram.com/" style="text-decoration:none;" ><h3 class="lnk">Instagram</h3></a>\n')
	x.write('<a href="http://www.docker.com/" style="text-decoration:none;" ><h3 class="lnk">Docker</h3></a>\n')
	x.write('</center>\n')
	x.write('</div>\n')
	x.write('</body>\n')
	x.write('</html>\n')
	x.close()
	getstatusoutput('cd {1} && sudo zip -rv9 {0}.zip {0}'.format(folder,path))

	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=http://www.welkins.com/home4u/files/bin/{}.zip\">\n".format(folder)

	print "<a href='http://www.welkins.com/home4u/index.html'><b>Click here</b></a>"

else:

	message='No file uploaded'

	print message

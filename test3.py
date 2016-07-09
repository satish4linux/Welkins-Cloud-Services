import Cookie

#create the cookie

c=Cookie.SimpleCookie()

#assign a value

c['user']='admin'

#set the expires time

c['user']['expires']=1*1*3*60*60

print c



========================

$wget --save-headers http://www.welkins.com/cgi-bin/<python-page>

=======================

retrieving cookies


import Cookie



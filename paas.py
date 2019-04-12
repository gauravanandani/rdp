#!/usr/bin/python

import  cgi
import  commands
print "Content-type:text/html"
print  ""

web=cgi.FieldStorage()
c=web.getvalue('t1')


print   "<pre>"
print commands.getoutput(c)
print  "</pre>"
print "<a href=/paaschoose.html>Go Back</a>"

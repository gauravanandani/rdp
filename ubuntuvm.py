#!/usr/bin/python

import os
import cgi

print "Content-type:text/html"
print  ""

web=cgi.FieldStorage()

name=web.getvalue('osname')
ram=web.getvalue('ram')
cpu=web.getvalue('cpu')

os.system("qemu-img  create -f qcow2 -b  /var/lib/libvirt/images/rhvmdnd.qcow2 /var/lib/libvirt/images/"+ name +".qcow2")
output="sudo virt-install --name "+ name +" --ram "+ ram +" --vcpu "+ cpu +" --disk path=/var/lib/libvirt/images/"+ name +".qcow2  --import"
os.system("virt-install --name "+ name +" --ram "+ ram +" --vcpu "+ cpu +" --disk path=/var/lib/libvirt/images/"+ name +".qcow2  --import")

print "<pre>"
print output
print "Please Wait....."
print "</pre>"

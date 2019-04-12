#!/usr/bin/python3.6

import subprocess
import os
import cgi
import mysql.connector as mariadb
import webbrowser

mariadb_connection = mariadb.connect(user='root', password='redhat', database='cloudvm')
cursor = mariadb_connection.cursor()


print("Content-type:text/html")
print("")

web=cgi.FieldStorage()

name=web.getvalue('osname')
ram=web.getvalue('ram')
cpu=web.getvalue('cpu')
port=web.getvalue('port')
#checking query
cursor.execute("SELECT os_name,port_no FROM novnc where os_name='"+str(name)+"'")
cursor.fetchone()
a=cursor.fetchone()
cursor.execute("SELECT port_no FROM novnc where port_no='"+str(port)+"' ")
cursor.fetchone()
b=cursor.fetchone()

if(a != None):
	if(a[0] == name):
		print("Try another name")
		if(b != None):		
			if(b[0] == port):
				print("Try another port number")
	#	return false
		#print("<a href="/html/redhatvm.html">GO BACK</a>")
'''
cursor.execute("SELECT port_no FROM novnc where port_no='"+str(port)+"' ")
cursor.fetchone()
b=cursor.fetchone()
if(a != None):
	if(b[0] == port):
		print("Port Already Exist")
	#	return false
'''
#insert information
try:
    cursor.execute("INSERT INTO novnc (port_no,os_name,cpu,ram) VALUES (%s,%s,%s,%s)", (port,name,cpu,ram))
except mariadb.Error as error:
    print("Error: {}".format(error))

mariadb_connection.commit()
print ("The last inserted id was: ", cursor.lastrowid)


mariadb_connection.close()

#os build with novnc

#os.system("sudo qemu-img  create -f qcow2 -b  /var/lib/libvirt/images/rhvmdnd.qcow2 /var/lib/libvirt/images/"+ str(name) +".qcow2 &")

subprocess.Popen("sudo qemu-img  create -f qcow2 -b  /var/lib/libvirt/images/rhvmdnd.qcow2 /var/lib/libvirt/images/"+ str(name) +".qcow2 &", stdout=None, shell=True)

#os.system("sudo virt-install --name "+ str(name) +" --ram "+ str(ram) +" --vcpu "+ str(cpu) +" --disk path=/var/lib/libvirt/images/"+ str(name) +".qcow2 --import --graphics=vnc,listen=192.168.42.163,port=5992 --noautoconsole &")

subprocess.Popen("sudo  virt-install --name "+ str(name) +" --ram "+ str(ram) +" --vcpu "+ str(cpu) +" --disk path=/var/lib/libvirt/images/"+ str(name) +".qcow2 --import --graphics=vnc,listen=192.168.42.180,port=5992 --noautoconsole &", stdout=None, shell=True)

#os.system("nohup websockify --web=/usr/share/novnc "+ str(port) +" 192.168.42.21:5990  &")

subprocess.Popen("nohup websockify --web=/usr/share/novnc "+str(port)+" 192.168.42.163:5992  &", stdout=None, shell=True)

print("<br/>")
print ("opening your vm...")
os.system("sleep 5")

print("<br/>")
print(" <a href=http://192.168.42.180:"+str(port)+"> Click here to start your vm </a> ")






#IP get
'''print "<pre>"
print "You can SSH through this IP ADDRESS:"
print "Your Instance Ip is:-"
os.system("virt=`virsh dumpxml "+ str(osname) +" | grep 'mac address' | cut -d"'" -f2` ")
os.system("v1=`arp-scan -q -l | grep -i $virt | awk '{print $1}'`")
a=os.system("echo $v1")

print a'''

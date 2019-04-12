#!/usr/bin/python3.6

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='redhat', database='cloudvm')
cursor = mariadb_connection.cursor()

name="abc7"
port="50003"
#checking query
cursor.execute("SELECT os_name FROM novnc where os_name="+str(name)+"")
a=cursor.fetchone()
if(a[0] == name):
        {
                print("Name already Exist Try another name")
        #       return false
                #print("<a href="/html/redhatvm.html">GO BACK</a>")
        }
cursor.execute("SELECT port_no FROM novnc where port_no="+str(port)+"")
b=cursor.fetchone()
if(b[0] == port):
        {
                print("Port Already Exist")
        #       return false
        }




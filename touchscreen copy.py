#!/usr/bin/python

# this is the old version of the file where we sent one of four characters
# through the raspberrypi serial port to the arduino

import cgi
import cgitb; cgitb.enable()
import serial
import time
import subprocess
#import csv

print "Content-type: text/html\n\n"
print "<html>"

f = cgi.FieldStorage()
bag=int(f['bag'].value)

if bag == 1:
	subprocess.call(['./bag1.sh'])
elif bag == 2:
	subprocess.call(['./bag2.sh'])
elif bag == 3:
	subprocess.call(['./bag3.sh'])
elif bag == 4:
	subprocess.call(['./bag4.sh'])

print "<html>"

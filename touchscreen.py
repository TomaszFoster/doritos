#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()
import time
import smbus
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# here we use SMBus to transfer a three digit number
# in reality smbus lets you send one of 256 values at a time
# which wasn't enough as we had about 600 bags of doritos to worry about
# there are cleaner methods to do this, sure, but since we were asked to rewrite everything the day before
# SXSW to not use twitter integration anymore but rather an iPad interface (pinch and zoom on the bag)
# we wrote this in Norfolk, VA and pushed it to the raspberry pi in Austin, TX hours before
# the Doritos vending machine went live. 

# This is the address we setup in the Arduino Program
address = 0x04

print "Content-type: text/html\n\n"
print "<html>"

f = cgi.FieldStorage()
bag=int(f['bag'].value)

number_string = str(bag)

if bag < 10:
	print 'I will return: '
	bus.write_byte(address, 0)
	bus.write_byte(address, 0)
	bus.write_byte(address, bag)
	print 0
	print 0
	print bag
elif bag >= 10 and bag < 100:
	print 'I will return: '
	bus.write_byte(address, 0)
	print 0
	for ch in number_string:
		bus.write_byte(address, int(ch))
		print ch
elif bag >= 100 and bag <= 600:
	print 'I will return: '
	for ch in number_string:
		print ch
		bus.write_byte(address, int(ch))

print "</html>"

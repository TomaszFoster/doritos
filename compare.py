#!/usr/bin/python

import csv
import twitter
import re
import time
import datetime
import subprocess
print "trying..."
ts = time.time()

api = twitter.Api(consumer_key='xxx',consumer_secret='xxx',access_token_key='xxx',access_token_secret='xxx')

status = api.GetSearch("#doritosvending")
log = open('/usr/lib/cgi-bin/log.txt', 'a')
for s in status:
	print "tweet! " + str(s.created_at) + " " +str(s.text)
	with open('/usr/lib/cgi-bin/log.txt', 'rb') as f:
		reader = csv.reader(f, delimiter=',')
		foundIt=False
		for row in reader:
			if str(s.id) == str(row[0]):
				foundIt=True
				break
		if foundIt==False:
			print "append!"
			bagNum = int(re.sub(r'#doritosvending ','',s.text))
			
			if bagNum == 1:
				subprocess.call(['/usr/lib/cgi-bin/bag1.sh'], shell=True)
			elif bagNum == 2:
				subprocess.call(['/usr/lib/cgi-bin/bag2.sh'], shell=True)
			elif bagNum == 3:
				subprocess.call(['/usr/lib/cgi-bin/bag3.sh'], shell=True)
			elif bagNum == 4:
				subprocess.call(['/usr/lib/cgi-bin/bag4.sh'], shell=True)

			log.write(str(s.id) + ","+s.created_at + "," + re.sub(r'#doritosvending ','',s.text)+"\n")

log.close()

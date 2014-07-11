import csv
import twitter
import re
import time
import datetime
ts = time.time()

# we ended up not using the twitter integration because the delay was considered too great
# (it took approximately 20-30 seconds before any tweet was searchable on their api)

api = twitter.Api(consumer_key='xxx',consumer_secret='xxx',access_token_key='xxx',access_token_secret='xxx')
status = api.GetSearch("#doritosvending")
log = open('log.txt', 'r+w')
for s in status:
	log.write(str(s.id) + ","+s.created_at + "," + re.sub(r'#doritosvending ','',s.text)+"\n")
log.close()
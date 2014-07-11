import csv
import twitter
import re
import time
import datetime
ts = time.time()

api = twitter.Api(consumer_key='nLr50Uiqc87lz89fuRTCOQ',consumer_secret='l120NsqGFwbw2YjSBdPNpGxe7cJH7l4D8yYlDwSi8',access_token_key='2351875860-m8FNBOzxlfUkQ3eLGgEgZ2rmTS5zPkr2dRVCoyY',access_token_secret='9AinlaGHaTjitJ2peSV22LrkqcLeSWPJt4nXYiE4H1uey')
status = api.GetSearch("#doritosvending")
log = open('log.txt', 'r+w')
for s in status:
	log.write(str(s.id) + ","+s.created_at + "," + re.sub(r'#doritosvending ','',s.text)+"\n")
log.close()
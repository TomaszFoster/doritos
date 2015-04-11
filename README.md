## Doritos vending machine for SXSW - June 2014

You can read more about this machine on [Make Zine](http://makezine.com/2014/06/10/massive-vending-machine-drops-doritos-on-demand/)

#### The breakdown

##### Revision One
+ `touchscreen_old.py` is the original code I wrote when the design params called for choosing one of four different types of Doritos bags.
+ `compare.py` was written to search for Tweets on the Twittersphere for anything containing the hashtag `#doritosvending`. The idea was that a user would tweet something like `#doritosvending 3` and with regular expressions we would filter out everything but the 3, compare this to the log of recent tweets, and if it was new and we hadn't selected this bag yet, we would call on of four shell scripts, i.e. `bag3.sh`, to write out the appropriate number through GPIO pins to the master arduino.
+ `cronjob.sh` was set up so that we could run compare.py every 5 seconds upon boot. We wanted to make this as plug and play as possible.
+ `getRecentTweets.py`, `testSubmit.py`, `checkTwitter.py` were written on day one to get an initial proof of concept and test out the serial and GPIO ports as well as make sure the Twitter authentication worked.

##### Revision Two
+ `touchscreen.py` is the final working code we used. This code reads in the request from an iPad, breaks the code up into three single digit values and sends it through the RPi GPIO pins to a master Arduino. Essentially the Doritos team decided to scrap the Twitter logic I built since it took too long. Realistically once you sent a tweet, it could take 20-30 seconds before that hashtag was searchable through their API. The code I wrote works and although I understand their decision to remove this functionality, I was still pretty bummed we couldn't keep it.
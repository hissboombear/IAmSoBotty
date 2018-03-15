import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Adds a prefix to all tweets
prefix = 'Boop Beep\n'
#Adds a postfix to all tweets
postfix = '\nBeep Boop'

filename=open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(prefix + line + postfix)
    time.sleep(900)

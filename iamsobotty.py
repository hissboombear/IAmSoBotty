import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = 'y9YcMQ0LoPJ27wqUZrtmrwbCw'
CONSUMER_SECRET = 'teNYTvUbYXd8QojtkdB2tJBkfoXbEJS6mPpHxDDRonOw4DKzMf'
ACCESS_KEY = '965609423644364801-dsbfLeIwy54ah3aN3ZL4VybftXOWe5e'
ACCESS_SECRET = '5abLklwA5GPhlIH4rTsCZN8UCOfhJ4LF0sXGdC7DydauM'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)

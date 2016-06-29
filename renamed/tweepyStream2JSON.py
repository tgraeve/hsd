import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = "2OM8NeaYfQRcXng9tPgFKft3t"
consumer_secret = "7QP0bVI0qDPotmHG0DSI8FBJVQExCPmdJczdGQFGtC0g98zZEn"
access_token = "67152181-hXGXzZcsCIjxtcQPWmyJjzEvm4tEmlbbu8eUivbvB"
access_secret = "q0sAC1WtPhHt21ChPtUSrkWQqRXo4WHcmkgMtUSKBdiQU"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

class MyStreamListener(StreamListener):
 
 	# def on_status(self, status):
 	# 	print(status.text)

    def on_data(self, data):
        try:
            with open('hatespeech.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

myStreamListener = MyStreamListener()
myStream = Stream(auth = api.auth, listener = myStreamListener)
myStream.filter(track=['rapefugees,krimigranten,stopislam,deport,migrantcrisis,refugeecrisis,refujihadis,immivasion,istandwithhatespeech'],languages=['de'])


# twitter_stream = Stream(auth, MyListener())
# twitter_stream.filter(track=['#rapefugees'])
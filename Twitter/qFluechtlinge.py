import tweepy
import json

consumer_key = "2OM8NeaYfQRcXng9tPgFKft3t"
consumer_secret = "7QP0bVI0qDPotmHG0DSI8FBJVQExCPmdJczdGQFGtC0g98zZEn"
access_token = "67152181-hXGXzZcsCIjxtcQPWmyJjzEvm4tEmlbbu8eUivbvB"
access_secret = "q0sAC1WtPhHt21ChPtUSrkWQqRXo4WHcmkgMtUSKBdiQU"

auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

query = "rapefugees OR krimigranten OR stopislam OR deport OR migrantcrisis OR refugeecrisis OR refujihadis OR immivasion"

# places = api.geo_search(query="Deutschland", granularity = "country")
# place_id = places[0].id

# print places[0].id

# tweets = api.search(q="place:%s" % place_id + "#krimigranten")
# for tweet in tweets:
#     print tweet.text + " \n\n " +  tweet.place.name if tweet.place else "Undefined place"

count = 1

for tweet in tweepy.Cursor(api.search,q=query,geocode="51.1656910,10.4515260,454km").items():
	print ("Nummer: %5d, Inhalt: %150s" % (count,tweet.text))
	with open('fluechtlinge.json','a') as f:
		f.write(json.dumps(tweet._json))
		f.write("\n")
	count +=1

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

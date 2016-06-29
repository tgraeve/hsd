import tweepy
import json

consumer_key = "2OM8NeaYfQRcXng9tPgFKft3t"
consumer_secret = "7QP0bVI0qDPotmHG0DSI8FBJVQExCPmdJczdGQFGtC0g98zZEn"
access_token = "67152181-hXGXzZcsCIjxtcQPWmyJjzEvm4tEmlbbu8eUivbvB"
access_secret = "q0sAC1WtPhHt21ChPtUSrkWQqRXo4WHcmkgMtUSKBdiQU"

auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

query = "schwuchtel"

count = 1

search_results = []

for status in tweepy.Cursor(api.search,q=query,geocode="51.1656910,10.4515260,454km",lang="de").items():
	search_results.append(status._json)
	print ("Nummer: %5d, Inhalt: %150s" % (count,status.text))
	count +=1

with open('data/homophobie.json','a') as f:
	json.dump(search_results, f)
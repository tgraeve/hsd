#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import tweepy
import json

consumer_key = "2OM8NeaYfQRcXng9tPgFKft3t"
consumer_secret = "7QP0bVI0qDPotmHG0DSI8FBJVQExCPmdJczdGQFGtC0g98zZEn"
access_token = "67152181-hXGXzZcsCIjxtcQPWmyJjzEvm4tEmlbbu8eUivbvB"
access_secret = "q0sAC1WtPhHt21ChPtUSrkWQqRXo4WHcmkgMtUSKBdiQU"

auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

query = "rapefugees OR krimigranten OR stopislam OR deport OR migrantcrisis OR refugeecrisis OR refujihadis OR immivasion OR merkills OR germanozid"

count = 0

for tweet in tweepy.Cursor(api.search,q=query,geocode="51.1656910,10.4515260,454km",lang="de").items():
	with open('/home/hsd/twitter/data/fluechtlinge.json','a') as f:
		json.dump(tweet._json, f)
		f.write("\n")
	count +=1

print ("Crawled %5d Tweets" % (count))
import json
from pymongo import MongoClient

client = MongoClient("localhost",21051)
db_auth = client.admin
db_auth.authenticate("hsd_mongoadmin","KoPh8oh9oo")

db = client.tweets

with open("data/fluechtlinge.json") as jsonFile:
	for line in jsonFile:
		tweet = json.loads(line)
		id = tweet['id']
		date = tweet['created_at']
		coords = tweet['coordinates']
		user_loc = tweet['user']['location'].encode('utf-8')
		text = tweet['text'].encode('utf-8')
		if (tweet['place'] is not None):
			place = tweet['place']['full_name'].encode('utf-8')
		else:
			place = ""

		result = db.test.insert_one(
		{
			"id" : id,
			"date" : date,
			"geo" : {
				"coords" : coords,
				"tweet" : place,
				"user" : user_loc
			},
			"text" : text
		}
		)
		print result.inserted_id

print "soweit, so gut..."

				
					
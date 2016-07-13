import json
 
with open('data/fluechtlinge.json', 'r') as f:
	for line in f:
		tweet = json.loads(line)
		print(tweet['user']['location'])
		#if(tweet['coordinates'] is not None):
			#print(tweet['coordinates'])
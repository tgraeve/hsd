import json

class Json2Cons:

	def __init__(self):
		pass

	@staticmethod
	def extract(input):
		if(type(input)==str):
			with open('data/fluechtlinge.json', 'r') as f:
				for line in f:
					tweet = json.loads(line)
					if(tweet['coordinates'] is not None): 			#prints coordinates of tweet
						print(tweet['coordinates'])
					elif(tweet['place'] is not None): 				#prints place of tweet
						print(tweet['place']['full_name'])
					elif(tweet['user']['location'] is not None):	#prints location of user
						print(tweet['user']['location'])
					else:
						print("-*-TWEET IS NOT GEOLOCATED-*-")
		else:
			print("Input path is not a string!")
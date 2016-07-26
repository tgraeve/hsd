#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import json
import csv

class Json2Cons:

	def __init__(self):
		pass

	@staticmethod
	def extract(input):
		if(type(input)==str):
			with open(input+".json", 'r') as f:
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

class Json2Csv:

	def __init__(self):
		pass

	@staticmethod
	def extract(input):
		if(type(input)==str):
			csvFile = open(input+".csv",'a')
			csvWriter = csv.writer(csvFile)

			with open(input+".json") as jsonFile:
				for line in jsonFile:
					tweet = json.loads(line)
					if(tweet['place'] is not None):
						csvWriter.writerow([tweet['id'],
											tweet['coordinates'],
											tweet['place']['full_name'].encode('utf-8'),
											tweet['user']['location'].encode('utf-8'),
											tweet['text'].encode('utf-8')
											])
					else:
						csvWriter.writerow([tweet['id'],
											tweet['coordinates'],
											'None',
											tweet['user']['location'].encode('utf-8'),
											tweet['text'].encode('utf-8')
											])
			csvFile.close()
		else:
			print("Input path is not a string!")

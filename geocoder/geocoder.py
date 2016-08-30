# This python file uses the following encoding: utf-8

import csv
import json

ifile = open('db/staedte.csv', "r")
csvReader = csv.reader(ifile, delimiter='\n')

#ofile = open('wacken_coords.txt', "wb")
#writer = csv.writer(ofile, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

with open("../visualization/json/homophobie.json", 'r') as f:
	countTweets = 0
	countMatches = 0
	for line in f:
		tweet = json.loads(line)
		# if (tweet['place'] is not None):
		# 	tweetPlaceTemp = tweet['place']['full_name'].split(",")
		# 	tweetPlace = tweetPlaceTemp[0].upper().encode('utf-8')
		# 	print tweetPlace					
		# 	for row in tabReader:
		# 		if row[2] == (tweetPlace):
		# 			print "Stadt: " + row[2] + ", Einwohner: " + row[9]
		if (tweet['user']['location'] is not None):
			countTweets += 1
			endSearch = False
			userPlace = tweet['user']['location'].encode('utf-8')
			print userPlace
			userPlaceSplit = userPlace.split(',')
			for row in csvReader:
				if (endSearch == False):
					cityName = str(row[0])
					#print cityName
					if (cityName in userPlaceSplit):
						endSearch = True
						print "---FOUND MATCH--- : " + cityName
						countMatches += 1

		ifile.seek(0)

print "Anzahl Tweets mit User-Location Angabe: " + str(countTweets)
print "Anzahl erfolgreicher Zuordnungen zu Staedten: " + str(countMatches)

acc = float(countMatches)/float(countTweets)

print "Accuracy: " + str(acc)
print "------------------ geocoder.py FINISHED ------------------"

ifile.close()
#ofile.close()
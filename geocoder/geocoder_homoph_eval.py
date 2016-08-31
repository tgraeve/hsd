#import csv
import json

#ofile = open('homophobie_counts.txt', "wb")
#writer = csv.writer(ofile, delimiter=',', quotechar = '"', quoting=csv.QUOTE_ALL)

with open("../visualization/json/homophobie.json", 'r') as f:
	countCoords = 0
	countPlaces = 0
	countUserLoc = 0
	for line in f:
		tweet = json.loads(line)
		if (tweet['coordinates'] is not None):
			countCoords += 1
		elif (tweet['place'] is not None):
			countPlaces += 1
		elif (tweet['user']['location'] is not None):
			countUserLoc += 1

print "Anzahl Tweets mit Coordinaten: " + str(countCoords)
print "Anzahl Tweets mit Tweet-Places: " + str(countPlaces)
print "Anzahl Tweets mit User-Location: " + str(countUserLoc)

print "---------- geocoder_homoph_eval.py FINISHED ----------"
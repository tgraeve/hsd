# This python file uses the following encoding: utf-8

import csv
import json

ifile = open('db/staedte.csv', "r")
csvReader = csv.reader(ifile, delimiter='\n')

ofile = open('noMatchFound.txt', "wb")
writer = csv.writer(ofile, delimiter=' ', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

with open("../visualization/json/homophobie.json", 'r') as f:
	countCoords = 0
	countPlaces = 0
	countUserLoc = 0
	countMatches = 0
	for line in f:
		tweet = json.loads(line)
		if (tweet['coordinates'] is not None):
			countCoords += 1
		elif (tweet['place'] is not None):
			countPlaces += 1
		elif (tweet['user']['location'] is not None):
			countUserLoc += 1
			endSearch = False
			userPlace = tweet['user']['location'].encode('utf-8')
			userPlaceStrip = userPlace.strip(' \t\n\r')
			if (userPlaceStrip != ""):
				#countUserLoc += 1
				print userPlace
				userPlaceSplitC = userPlace.split(',')
				userPlaceSplitS = userPlace.split(' ')
				for row in csvReader:
					if (endSearch == False):
						cityName = str(row[0])
						#print cityName
						if (cityName in userPlaceSplitC or cityName in userPlaceSplitS):
							endSearch = True
							print "---FOUND MATCH--- : " + cityName
							countMatches += 1
			if endSearch == False:
				writer.writerow([userPlace])

		ifile.seek(0)

print "Anzahl Tweets mit User-Location Angabe: " + str(countUserLoc)
print "Anzahl erfolgreicher Zuordnungen zu Staedten: " + str(countMatches)

dropout = float(1) - (float(countMatches)/float(countUserLoc))

print "Dropout: " + str(dropout)
print "------------------ geocoder.py FINISHED ------------------"

ifile.close()
ofile.close()
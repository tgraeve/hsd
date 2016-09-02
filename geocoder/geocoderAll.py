# This python file uses the following encoding: utf-8

import csv
import json

ifile = open('db/staedte.csv', "r")
csvReader = csv.reader(ifile, delimiter='\n')

ofileNoMatch = open('noMatchFoundAll.txt', "wb")
writerNoMatch = csv.writer(ofileNoMatch, delimiter=' ', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

ofileCities = open('matchedCitiesAll.txt', "wb")
writerMatchedCities = csv.writer(ofileCities, delimiter = ' ', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

with open("../visualization/json/all.json", 'r') as f:
	countCoords = 0
	countPlaces = 0
	countUserLoc = 0
	countUserLocNotEmpty = 0
	countMatches = 0
	for line in f:
		tweet = json.loads(line)
		if (tweet['coordinates'] is not None):
			countCoords += 1

		elif (tweet['place'] is not None):
			countPlaces += 1
			endS = False
			tweetPlace = tweet['place']['full_name'].encode('utf-8').lower()
			#print tweetPlace
			tweetPlaceSplitC = tweetPlace.split(',')
			for row in csvReader:
				if (endS == False):
					cityName = str(row[0]).lower()
					if (cityName in tweetPlaceSplitC):
						endS = True
						#print "FOUND MATCH: " + cityName
						writerMatchedCities.writerow([cityName])
			if endS == False:
				writerNoMatch.writerow([tweetPlace])
			ifile.seek(0)

		elif (tweet['user']['location'] is not None):
			countUserLoc += 1
			endSearch = False
			userPlace = tweet['user']['location'].encode('utf-8').lower()
			userPlaceStrip = userPlace.strip(' \t\n\r')
			if (userPlaceStrip != ""):
				countUserLocNotEmpty += 1
				#print userPlace
				userPlaceSplitC = userPlace.split(',')
				userPlaceSplitS = userPlace.split(' ')
				userPlaceSplitM = userPlace.split('-')
				for row in csvReader:
					if (endSearch == False):
						cityName = str(row[0]).lower()
						#print cityName
						if (cityName in userPlaceSplitC or cityName in userPlaceSplitS or cityName in userPlaceSplitM):
							endSearch = True
							#print "---FOUND MATCH--- : " + cityName
							writerMatchedCities.writerow([cityName])
							countMatches += 1
			if endSearch == False:
				writerNoMatch.writerow([userPlace])

		ifile.seek(0)

print "Anzahl Tweets mit User-Location Angabe: " + str(countUserLoc)
print "Anzahl erfolgreicher Zuordnungen zu Staedten: " + str(countMatches)

dropout = float(1) - (float(countMatches)/float(countUserLoc))

print "Dropout von User-Angaben: " + str(dropout)
print "------------------ geocoderAll.py FINISHED ------------------"

ifile.close()
ofileNoMatch.close()
ofileCities.close()
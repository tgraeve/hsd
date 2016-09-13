# This python file uses the following encoding: utf-8

import time
import csv
import json
from geopy.geocoders import Nominatim
from nltk import FreqDist

class hsdGeocoder:

	def __init__(self):
		pass

	@staticmethod
	def json2cities(input):
		if(type(input)==str):

			ifile = open('db/staedte.csv', "r")
			csvReader = csv.reader(ifile, delimiter='\n')

			ofileNoMatch = open(input + "_noMatchFound.txt", "wb")
			writerNoMatch = csv.writer(ofileNoMatch, delimiter=' ', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

			ofileCities = open(input + "_matchedCities.txt", "wb")
			writerMatchedCities = csv.writer(ofileCities, delimiter = ' ', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

			with open("../visualization/json/" + input + ".json", 'r') as f:
				countCoords = 0
				countMatchesCoords = 0
				countPlaces = 0
				countMatchesPlaces = 0
				countUserLoc = 0
				countUserLocNotEmpty = 0
				countMatchesUserLoc = 0
				for line in f:
					tweet = json.loads(line)
					if (tweet['coordinates'] is not None):
						countCoords += 1
						endSearch1 = False
						coords = str(tweet['coordinates'])[37:-2].split(',')
						coordsString = coords[1][1:] + ", " + coords[0]
						#print coordsString
						geolocator = Nominatim()
						location = geolocator.reverse(coordsString)
						if (location.address is not None):
							locAddress = str(location.raw['display_name'].encode('utf-8').lower())
							locSplit = locAddress.split(',')
							counter = 0
							for i in locSplit:
								locSplit[counter] = i.strip(' \t\n\r')
								counter += 1
							#print locSplit
							for row in csvReader:
								if (endSearch1 == False):
									cityName = str(row[0]).lower()
									#print cityName
									if (cityName in locSplit):
										endSearch1 = True
										#print "---FOUND MATCH--- : " + cityName
										writerMatchedCities.writerow([cityName])
										countMatchesCoords += 1
						if endSearch1 == False:
							writerNoMatch.writerow([userPlace])

						ifile.seek(0)
						time.sleep(1)

					elif (tweet['place'] is not None):
						countPlaces += 1
						endS = False
						tweetPlace = tweet['place']['full_name'].encode('utf-8').lower()
						#print tweetPlace
						tweetPlaceSplitC = tweetPlace.split(',')
						#print tweetPlaceSplitC
						for row in csvReader:
							if (endS == False):
								cityName = str(row[0]).lower()
								if (cityName in tweetPlaceSplitC):
									endS = True
									#print "FOUND MATCH: " + cityName
									writerMatchedCities.writerow([cityName])
									countMatchesPlaces += 1
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
										countMatchesUserLoc += 1
						if endSearch == False:
							writerNoMatch.writerow([userPlace])

					ifile.seek(0)

			print "Tweets mit Angabe der Koordinaten: " + str(countCoords)
			print "Erfolgreiche Zuordnungen zu Staedten: " + str(countMatchesCoords)
			print "-----"
			print "Tweets mit Angabe des Tweet-Places: " + str(countPlaces)
			print "Erfolgreiche Zuordnungen zu Staedten: " + str(countMatchesPlaces)
			print "-----"
			print "Tweets mit Angabe der User-Location: " + str(countUserLoc)
			print "Erfolgreiche Zuordnungen zu Staedten: " + str(countMatchesUserLoc)

			#dropout = float(1) - (float(countMatchesUserLoc)/float(countUserLoc))

			#print "Dropout von User-Angaben: " + str(dropout)
			print "--- json2cities FINISHED ---"

			ifile.close()
			ofileNoMatch.close()
			ofileCities.close()

		else: 
			print("Input must be a string!")

	@staticmethod
	def cities2coords(input):

		ifile = open("txt/" + input + "_matchedCities.txt", "r")
		csvReaderMatches = csv.reader(ifile, delimiter='\n')

		ifile2 = open("db/DE_cleanedUp.tab", "r")
		csvReaderDB = csv.reader(ifile2, delimiter='\t')

		ofile = open(input + "_coords.txt", "wb")
		writerCoords = csv.writer(ofile, delimiter=' ', quotechar='"', quoting= csv.QUOTE_MINIMAL)

		cityList = []
		fdList = []

		for row in csvReaderMatches:
			cityList.append(row[0])

		citiesFD = FreqDist(cityList)

		for i in citiesFD.most_common():
			fdList.append([i[0], i[1]])

		for item in fdList:
			for row in csvReaderDB:
				if (str(item[0]) == str(row[0])):
					weight = float(item[1])
					writerCoords.writerow([row[1] + "," + row[2] + "," + str("%.1f" % weight)])

			ifile2.seek(0)

		print "--- cities2coords FINISHED ---"

	@staticmethod
	def pop_normalizer(input):
		ifile = open("txt/" + input + "_matchedCities.txt", "r")
		csvReaderMatches = csv.reader(ifile, delimiter='\n')

		ifile2 = open("db/DE_cleanedUp.tab", "r")
		csvReaderDB = csv.reader(ifile2, delimiter='\t')

		ofile = open(input + "_coords_pn.txt", "wb")
		writerCoords = csv.writer(ofile, delimiter=' ', quotechar='"', quoting= csv.QUOTE_MINIMAL)

		matchedCitiesList = []
		fdList = []

		for row in csvReaderMatches:
			matchedCitiesList.append(row[0])

		citiesFD = FreqDist(matchedCitiesList)

		for i in citiesFD.most_common():
			fdList.append([i[0], i[1]])

		for item in fdList:
			for row in csvReaderDB:
				if (str(item[0]) == str(row[0])):
					weight = (float(item[1])/float(row[3])) * 1500000
					#print weight
					writerCoords.writerow([row[1] + "," + row[2] + "," + str("%.1f" % weight)])
					
			ifile2.seek(0)

		print "--- pop_normalizer FINISHED ---"

	@staticmethod
	def tweet_normalizer(input):
		ifile = open("txt/" + input + "_matchedCities.txt", "r")
		csvReaderMatches = csv.reader(ifile, delimiter='\n')

		ifile2 = open("db/DE_cleanedUp.tab", "r")
		csvReaderDB = csv.reader(ifile2, delimiter='\t')

		ifile3 = open("txt/all_matchedCities.txt", "r")
		csvReaderTweetCount = csv.reader(ifile3, delimiter='\n')

		ofile = open(input + "_coords_tn.txt", "wb")
		writerCoords = csv.writer(ofile, delimiter=' ', quotechar='"', quoting= csv.QUOTE_MINIMAL)

		matchedCitiesList = []
		fdMatchedCities = []
		allTweetsList = []
		fdAllTweets = []

		for row in csvReaderMatches:
			matchedCitiesList.append(row[0])

		matchesFD = FreqDist(matchedCitiesList)

		for i in matchesFD.most_common():
			fdMatchedCities.append([i[0], i[1]])

		for row in csvReaderTweetCount:
			allTweetsList.append(row[0])

		allTweetsFD = FreqDist(allTweetsList)

		for i in allTweetsFD.most_common():
			fdAllTweets.append([i[0], i[1]])

		for i in fdMatchedCities:
			for row in csvReaderDB:
				if (str(i[0]) == str(row[0])):
					for j in fdAllTweets:
						if(str(i[0]) == str(j[0])):
							weight = (float(i[1])/float(j[1])) * 1000
							#print weight
							writerCoords.writerow([row[1] + "," + row[2] + "," + str("%.1f" % weight)])
					
			ifile2.seek(0)

		print "--- tweet_normalizer FINISHED ---"
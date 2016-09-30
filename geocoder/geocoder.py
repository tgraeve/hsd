# This python file uses the following encoding: utf-8

import time
import csv
import math
import json
from geopy.geocoders import Nominatim
from nltk import FreqDist

class hsdGeocoder:

	def __init__(self):
		pass

	@staticmethod
	def json2cities(input):
		"""
		Diese Methode ließt eine json-Datei ein, welche pro Zeile einen Tweet als json-Objekt enthalten muss.
		Die Ausgabe ist eine Liste von Städten (als Textdatei), zu welchen die einzelnen Tweets geographisch zugeordnet werden konnten. 
		Alle Orts-Angaben aus Tweets, die keiner Stadt zugeordnet werden konnten, werden zur weiteren Überprüfung in eine seperate 
		Textdatei geschrieben. Aktuell können nur deutsche Schreibweisen der Städte erkannt werden.
		"""

		if(type(input)==str):

			# Öffnen der input- und outputstreams
			# Die Datei staedte.csv enthält eine Liste aller deutschen Städte und dient als Datenbank für die folgenden Geocoding-Aufgaben.
			ifile = open('db/staedte.csv', "r")
			csvReader = csv.reader(ifile, delimiter='\n')

			ofileNoMatch = open(input + "_noMatchFound.txt", "wb")
			writerNoMatch = csv.writer(ofileNoMatch, delimiter=' ', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

			ofileCities = open(input + "_matchedCities.txt", "wb")
			writerMatchedCities = csv.writer(ofileCities, delimiter = ' ', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

			# Öffnen der json-Datei, welche pro Zeile einen Tweet enthält.
			with open("../visualization/json/" + input + ".json", 'r') as f:

				# Counter für abschließende Textausgaben
				countCoords = 0
				countMatchesCoords = 0
				countPlaces = 0
				countMatchesPlaces = 0
				countUserLoc = 0
				countUserLocNotEmpty = 0
				countMatchesUserLoc = 0

				#tweetCounter = 0
				for line in f:
					tweet = json.loads(line)
					if ("" in tweet['text'].encode('utf-8')):
						# Durchsuchen der Spalte tweet['coordinates'].
						# Falls Koordinaten vorhanden sind, werden diese mithilfe des externen Werkzeugs "Nominatim" einer Stadt zugeordnet.
						if (tweet['coordinates'] is not None):
							countCoords += 1
							endSearch = False
							coords = str(tweet['coordinates'])[37:-2].split(',')
							coordsString = coords[1][1:] + ", " + coords[0]
							geolocator = Nominatim()
							location = geolocator.reverse(coordsString)
							if (location.address is not None):
								locAddress = str(location.raw['display_name'].encode('utf-8').lower())
								locSplit = locAddress.split(',')
								counter = 0
								for i in locSplit:
									locSplit[counter] = i.strip(' \t\n\r')
									counter += 1
								for row in csvReader:
									if (endSearch == False):
										cityName = str(row[0]).lower()
										if (cityName in locSplit):
											endSearch = True
											writerMatchedCities.writerow([cityName])
											countMatchesCoords += 1
											break
							# Falls Zuordnung fehlschlägt, werden Koordinaten in _noMatchFound.txt geschrieben.
							if endSearch == False:
								writerNoMatch.writerow([coordsString])

							ifile.seek(0)
							#Timer um externen Service "Nominatim" nicht zu überlasten.
							time.sleep(1)

						# Durchsuchen der Spalte tweet['place']
						# Falls Tweetplace angegeben ist, wird versucht, diesen mithilfe der staedte.csv einer Stadt zuzuordnen.
						elif (tweet['place'] is not None):
							countPlaces += 1
							endSearch = False
							tweetPlace = tweet['place']['full_name'].encode('utf-8').lower()
							tweetPlaceSplitC = tweetPlace.split(',')
							for row in csvReader:
								if (endSearch == False):
									cityName = str(row[0]).lower()
									if (cityName in tweetPlaceSplitC):
										endSearch = True
										writerMatchedCities.writerow([cityName])
										countMatchesPlaces += 1
										break
							# Falls Zuordnung fehlschlägt, wird der Tweet-Place in _noMatchFound.txt geschrieben.
							if endSearch == False:
								writerNoMatch.writerow([tweetPlace])

							ifile.seek(0)

						# Durchsuchen der Spalte tweet['user']['location'] (Freitext-Angabe von Usern)
						elif (tweet['user']['location'] is not None):
							countUserLoc += 1
							endSearch = False
							userPlace = tweet['user']['location'].encode('utf-8').lower()
							userPlaceStrip = userPlace.strip(' \t\n\r')
							if (userPlaceStrip != ""):
								countUserLocNotEmpty += 1
								userPlaceSplitC = userPlace.split(',')
								userPlaceSplitS = userPlace.split(' ')
								userPlaceSplitM = userPlace.split('-')
								userPlaceSplitSl = userPlace.split('/')
								for row in csvReader:
									if (endSearch == False):
										cityName = str(row[0]).lower()
										if (cityName in userPlaceSplitC or cityName in userPlaceSplitS or cityName in userPlaceSplitM or cityName in userPlaceSplitSl):
											endSearch = True
											writerMatchedCities.writerow([cityName])
											countMatchesUserLoc += 1
											break
							# Falls Zuordnung fehlschlägt, wird die User-Location in _noMatchFound.txt geschrieben.
							if endSearch == False:
								writerNoMatch.writerow([userPlace])

						#tweetCounter += 1
						#print str(tweetCounter)
						ifile.seek(0)

			# Ausgaben für weitere Überprüfungen
			print "Tweets mit Angabe der Koordinaten: " + str(countCoords)
			print "Erfolgreiche Zuordnungen zu Staedten: " + str(countMatchesCoords)
			print "-----"
			print "Tweets mit Angabe des Tweet-Places: " + str(countPlaces)
			print "Erfolgreiche Zuordnungen zu Staedten: " + str(countMatchesPlaces)
			print "-----"
			print "Tweets mit Angabe der User-Location: " + str(countUserLoc)
			print "Erfolgreiche Zuordnungen zu Staedten: " + str(countMatchesUserLoc)

			print "--- json2cities FINISHED ---"

			# Streams schließen
			ifile.close()
			ofileNoMatch.close()
			ofileCities.close()

		else: 
			print("Input must be a string!")

	@staticmethod
	def cities2coords(input):
		"""
		Die Eingabe dieser Methode ist eine Liste von Städten (als Textdatei), zu welchen die einzelnen Tweets
		in der json2cities-Methode geographisch zugeordnet werden konnten. 
		Die Ausgabe ist eine Textdatei, welche als Input für den Heatmap-Layer der Visualisierung dient.
		Diese Textdatei enthält die Koordinaten der zugeordneten Städte, sowie ein Gewicht für die Visualisierung. 
		Das Gewicht wird in dieser Methode durch die reine Anzahl der Vorkommen der Städte (in _matchedCities.txt) bestimmt. 
		"""

		# Öffnen der input- und outputstreams
		# Die Datei DE_cleanedUp.tab dient als Datenbank (enthält Koordinaten aller Städte).
		ifile = open("txt/" + input + "_matchedCities.txt", "r")
		csvReaderMatches = csv.reader(ifile, delimiter='\n')

		ifile2 = open("db/DE_cleanedUp.tab", "r")
		csvReaderDB = csv.reader(ifile2, delimiter='\t')

		ofile = open(input + "_coords.txt", "wb")
		writerCoords = csv.writer(ofile, delimiter=' ', quotechar='"', quoting= csv.QUOTE_MINIMAL)

		# Erstellen einer Frequency-Distribution, um die Anzahl der Vorkommen als Gewicht übergeben zu können.
		cityList = []
		fdList = []

		for row in csvReaderMatches:
			cityList.append(row[0])

		citiesFD = FreqDist(cityList)

		for i in citiesFD.most_common():
			fdList.append([i[0], i[1]])

		# In dieser Schleife werden für alle Städte die entsprechenden Koordinaten aus der Datenbank gelesen und mit Gewicht in die Output-Datei geschrieben.
		for item in fdList:
			for row in csvReaderDB:
				if (str(item[0]) == str(row[0])):
					weight = float(item[1])
					writerCoords.writerow([row[1] + "," + row[2] + "," + str("%.1f" % weight)])

			ifile2.seek(0)

		print "--- cities2coords FINISHED ---"

	@staticmethod
	def pop_normalizer(input):
		"""
		Die Eingabe dieser Methode ist eine Liste von Städten (als Textdatei), zu welchen die einzelnen Tweets
		in der json2cities-Methode geographisch zugeordnet werden konnten. 
		Die Ausgabe ist eine Textdatei, welche als Input für den Heatmap-Layer der Visualisierung dient.
		Diese Textdatei enthält die Koordinaten der zugeordneten Städte, sowie ein Gewicht für die Visualisierung. 
		Das Gewicht wird in dieser Methode durch die Einwohnerzahl der entsprechenden Städte normalisiert. 
		"""

		# Öffnen der input- und outputstreams
		# Die Datei DE_cleanedUp.tab dient als Datenbank (enthält Koordinaten und Einwohnerzahlen aller Städte).
		ifile = open("txt/" + input + "_matchedCities.txt", "r")
		csvReaderMatches = csv.reader(ifile, delimiter='\n')

		ifile2 = open("db/DE_cleanedUp.tab", "r")
		csvReaderDB = csv.reader(ifile2, delimiter='\t')

		ofile = open(input + "_coords_pn.txt", "wb")
		writerCoords = csv.writer(ofile, delimiter=' ', quotechar='"', quoting= csv.QUOTE_MINIMAL)

		# Erstellen einer Frequency-Distribution, um die Anzahl der Vorkommen durch die Einwohnerzahlen normalisieren zu können.
		matchedCitiesList = []
		fdList = []

		for row in csvReaderMatches:
			matchedCitiesList.append(row[0])

		citiesFD = FreqDist(matchedCitiesList)

		for i in citiesFD.most_common():
			fdList.append([i[0], i[1]])

		# In dieser Schleife werden für alle Städte die entsprechenden Koordinaten aus der Datenbank gelesen und mit Gewicht in die Output-Datei geschrieben.
		# Das Gewicht für jede Stadt lässt sich berechnen durch: (Anzahl Tweets / Anzahl Einwohner) * 1.500.000
		for item in fdList:
			for row in csvReaderDB:
				if (str(item[0]) == str(row[0])):
					weight = (float(item[1])/float(row[3])) * 1500000
					writerCoords.writerow([row[1] + "," + row[2] + "," + str("%.5f" % weight)])
					
			ifile2.seek(0)

		print "--- pop_normalizer FINISHED ---"

	@staticmethod
	def tweet_normalizer(input):
		"""
		Die Eingabe dieser Methode ist eine Liste von Städten (als Textdatei), zu welchen die einzelnen Tweets
		in der json2cities-Methode geographisch zugeordnet werden konnten. 
		Die Ausgabe ist eine Textdatei, welche als Input für den Heatmap-Layer der Visualisierung dient.
		Diese Textdatei enthält die Koordinaten der zugeordneten Städte, sowie ein Gewicht für die Visualisierung. 
		Das Gewicht wird in dieser Methode durch eine generelle Tweethäufigkeit der entsprechenden Städte normalisiert. 
		"""
		
		# Öffnen der input- und outputstreams
		# Die Datei DE_cleanedUp.tab dient als Datenbank (enthält Koordinaten aller Städte).
		# Außerdem dient die Datei all_matchedCities.txt als Grundlage zur Normalisierung des Gewichts.
		ifile = open("txt/" + input + "_matchedCities.txt", "r")
		csvReaderMatches = csv.reader(ifile, delimiter='\n')

		ifile2 = open("db/DE_cleanedUp.tab", "r")
		csvReaderDB = csv.reader(ifile2, delimiter='\t')

		ifile3 = open("txt/normalize_matchedCities.txt", "r")
		csvReaderTweetCount = csv.reader(ifile3, delimiter='\n')

		ofile = open(input + "_coords_tn.txt", "wb")
		writerCoords = csv.writer(ofile, delimiter=' ', quotechar='"', quoting= csv.QUOTE_MINIMAL)

		# Erstellen der Frequency-Distributions, um die Anzahl der Vorkommen durch die generelle Tweet-Häufigkeit der entsprechenden Stadt normalisieren zu können.
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

		# In dieser Schleife werden für alle Städte die entsprechenden Koordinaten aus der Datenbank gelesen und mit Gewicht in die Output-Datei geschrieben.
		# Das Gewicht für jede Stadt lässt sich berechnen durch: (Anzahl Tweets(zum Thema) / Anzahl Tweets (generell)) * 1.000
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
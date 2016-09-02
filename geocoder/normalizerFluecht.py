# This python file uses the following encoding: utf-8

import csv
from nltk import FreqDist

ifile = open('txt/matchedCitiesFluecht.txt', "r")
csvReaderMatches = csv.reader(ifile, delimiter='\n')

ifile2 = open('db/DE.tab', "r")
csvReaderDB = csv.reader(ifile2, delimiter='\t')

ifile3 = open('txt/tweetCountCities.txt', "r")
csvReaderCount = csv.reader(ifile3, delimiter='\n')

ofileWeighted = open('weightedCoordsFluecht.txt', "wb")
writerCoords = csv.writer(ofileWeighted, delimiter=' ', quotechar='"', quoting= csv.QUOTE_MINIMAL)

ofileWeighted2 = open('tweetWeightedCoordsFluecht', "wb")
writerTNCoords = csv.writer(ofileWeighted2, delimiter=' ', quotechar='"', quoting= csv.QUOTE_MINIMAL)

cityList = []
fdList = []
countList = []

for row in csvReaderMatches:
	cityList.append(row[0])

citiesFD = FreqDist(cityList)

for i in citiesFD.most_common():
	fdList.append([i[0], i[1]])

#print fdList[0][0]

# for item in fdList:
# 	for row in csvReaderDB:
# 		if (str(item[0]) == str(row[3]).lower() and row[4] not in "" and row[5] not in "" and row[9] not in ""):
# 			#print "Liste: " + str(item) + ", Mapping auf: " + str(row[3]).lower() + ", Lat: " + row[4] + ", Lon: " + row[5] + ", Einwohner: " + row[9]
# 			weight = (float(item[1])/float(row[9])) * 1500000
# 			#print weight
# 			writerCoords.writerow([row[4] + "," + row[5] + "," + str("%.1f" % weight)])
			
# 	ifile2.seek(0)

for r in csvReaderCount:

	arr = str(r).split(',')
	#print arr[0]
	countList.append(arr)
	#print countList[0][1]

for item in fdList:
	counter = 0
	for row in csvReaderDB:
		if (str(item[0]) == str(row[3]).lower() and row[4] not in "" and row[5] not in "" and row[9] not in ""):
			#print "Liste: " + str(item) + ", Mapping auf: " + str(row[3]).lower() + ", Lat: " + row[4] + ", Lon: " + row[5] + ", Einwohner: " + row[9]
			if (str(countList[counter][0][2:]) == str(item[0])):
				print str(countList[counter][0][2:]) + " auf: " + str(item[0])
				counter += 1
		
			weight = (float(item[1])/float(row[9])) * 1500000
			#print weight
			#writerCoords.writerow([row[4] + "," + row[5] + "," + str("%.1f" % weight)])
		ifile3.seek(0)
			
	ifile2.seek(0)

print "---normalizerFluecht.py FINISHED---"
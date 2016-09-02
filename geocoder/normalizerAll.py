# This python file uses the following encoding: utf-8

import csv
from nltk import FreqDist

ifile = open('txt/matchedCitiesAll.txt', "r")
csvReaderMatches = csv.reader(ifile, delimiter='\n')

ifile2 = open('db/DE.tab', "r")
csvReaderDB = csv.reader(ifile2, delimiter='\t')

ofileWeighted = open('weightedCoordsAll.txt', "wb")
writerCoords = csv.writer(ofileWeighted, delimiter=' ', quotechar='"', quoting= csv.QUOTE_MINIMAL)

cityList = []
fdList = []

for row in csvReaderMatches:
	cityList.append(row[0])

citiesFD = FreqDist(cityList)

for i in citiesFD.most_common():
	fdList.append([i[0], i[1]])

for item in fdList:
	for row in csvReaderDB:
		if (str(item[0]) == str(row[3]).lower() and row[4] not in "" and row[5] not in "" and row[9] not in ""):
			#print "Liste: " + str(item) + ", Mapping auf: " + str(row[3]).lower() + ", Lat: " + row[4] + ", Lon: " + row[5] + ", Einwohner: " + row[9]
			weight = (float(item[1])/float(row[9])) * 1500000
			#print weight
			writerCoords.writerow([row[4] + "," + row[5] + "," + str("%.1f" % weight)])
			

	ifile2.seek(0)

print "---normalizerAll.py FINISHED---"
import csv
import geocoder

ifile = open('wacken.csv', "rb")
reader = csv.reader(ifile)
ofile = open('wacken_coords.txt', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

for row in reader:
	if row[1] not in (None, ""):
		data = str(row[1][37:-2])
		strArray = data.split(",")
		latlngStr = strArray[1][1:] + ", " + strArray[0]
		#print latlngStr
		writer.writerow([latlngStr])

	elif row[2] not in (None, "None"):
		print (row[2])
		g = geocoder.google(row[2])
		#print (g.latlng)
		data2 = str(g.latlng)
		if data2 not in (None, "[]"):
			writer.writerow([data2[1:-1]])

	elif row[3] not in (None, ""):
		#print row[3]
		geo = geocoder.google(row[3])
		data3 = str(geo.latlng)
		#print data3
		if data3 not in (None, "[]"):
			writer.writerow([data3[1:-1]])

print "------------------ csvParser.py FINISHED ------------------"

ifile.close()
ofile.close()
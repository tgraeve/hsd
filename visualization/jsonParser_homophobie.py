import csv
import json
import geocoder

ofile = open('homophobie_coords.txt', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar = '"', quoting=csv.QUOTE_ALL)

with open("json/homophobie.json", 'r') as f:
				for line in f:
					tweet = json.loads(line)
					if (tweet['coordinates'] is not None):
						print ("Koordinaten: " + str(tweet['coordinates']))
						data = str(tweet['coordinates'])[37:-2]
						strArray = data.split(",")
						latlngStr = strArray[1][1:] + ", " + strArray[0]
						#print latlngStr
						writer.writerow([latlngStr])
					elif (tweet['place'] is not None):
						#print ("Tweet-Place: " + tweet['place']['full_name'])
						g = geocoder.google(tweet['place']['full_name'])
						data2 = str(g.latlng)
						if data2 not in (None, "[]"):
							writer.writerow([data2[1:-1]])
					elif (tweet['user']['location'] is not None):
						print ("User-Location: " + tweet['user']['location'].encode('utf-8'))
						g2 = geocoder.google(tweet['user']['location'])
						data3 = str(g2.latlng)
						if data3 not in (None, "[]"):
							#print (data3)
							writer.writerow([data3[1:-1]])


print "---------- jsonParser_homophobie.py FINISHED ----------"
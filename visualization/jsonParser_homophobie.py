import csv
import json
import geocoder

ofile = open('homophobie_coords.txt', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar = '"', quoting=csv.QUOTE_ALL)

with open("json/homophobie.json", 'r') as f:
				for line in f:
					tweet = json.loads(line)
					if (tweet['coordinates'] is not None):
						print ("Koordinaten: " + tweet['coordinates'])
						#tweetCoords =  tweet['coordinates']
						#writer.writerow([tweetCoords])
					elif (tweet['place'] is not None):
						print ("Tweet-Place: " + tweet['place']['full_name'])
						#g = geocoder.google(tweet['place']['full_name'])
						#data = str(g.latlng)
						#if data not in (None, "[]"):
						#	writer.writerow([data[1:-1]])
					elif (tweet['user']['location'] is not None):
						print ("User-Location: " + tweet['user']['location'])
						#g2 = geocoder.google(tweet['user']['location'])
						#data2 = str(g2.latlng)
						#if data2 not in (None, "[]"):
						#	print (data2)
						#	writer.writerow([data2[1:-1]])


print "---------- jsonParser_homophobie.py FINISHED ----------"
import json
import csv

with open('data/homophobie.json') as jsonFile:
	jsonStr = jsonFile.read()
	jsonData = json.loads(jsonStr)

csvFile = open('data/homophobie.csv','a')
csvWriter = csv.writer(csvFile)

print "nothing"

for item in jsonData:
	print item
	csvWriter.writerow([item.get('created_at'),
						item.get('text').encode('utf-8'),
						item.get('user').get('screen_name')
						])
csvFile.close()
import json
import csv

csvFile = open('data/homophobie.csv','a')
csvWriter = csv.writer(csvFile)

with open('data/homophobie.json') as jsonFile:
	for line in jsonFile:
		tweet = json.loads(line)
		csvWriter.writerow([tweet['id'],
							tweet['user']['location'].encode('utf-8')
							])
csvFile.close()


	
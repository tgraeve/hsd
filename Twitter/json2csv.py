import json
import csv

with open('data/homophobie.json') as jsonFile:
	jsonData = json.loads(jsonFile)

# csvFile = open('test.csv','a')
# csvWriter = csv.writer(csvFile)

print "nothing"

# for item in jsonData:
# 	print item
	# csvWriter.writerow([line.get('created_at'),
	# 					line.get('text').encode('utf-8'),
	# 					line.get('user').get('screen_name')
	# 					])
csvFile.close()
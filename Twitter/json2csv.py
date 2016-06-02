import json
import csv

jsonFile = open('data/homophobie.json','r')
jsonData = json.loads(jsonFile)

csvFile = open('test.csv','a')
csvWriter = csv.writer(csvFile)

print jsonData

# for line in jsonData:
# 	csvWriter.writerow([line.get('created_at'),
# 						line.get('text').encode('utf-8'),
# 						line.get('user').get('screen_name')
# 						])
csvFile.close()
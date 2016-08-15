import csv
import json

ofile = open('wacken_texts.txt', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar = '"', quoting=csv.QUOTE_ALL)

with open("wacken.json", 'r') as f:
				for line in f:
					tweet = json.loads(line)
					tweetText =  tweet['text'].encode('utf-8')
					writer.writerow([tweetText])

print "---------- jsonParser.py FINISHED ----------"
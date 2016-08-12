#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from somajo import Tokenizer
import json
import io
from collections import Counter
from nltk.corpus import stopwords

tokenizer = Tokenizer(split_camel_case=False, token_classes=True)
count_all = Counter()
count_hashtags = Counter()
twStop = set(io.open('resources/german_stopwords.txt', encoding='utf-8').read().splitlines())
stop = set(stopwords.words('german'))

with io.open("data/fluechtlinge.json", encoding='utf-8') as jsonFile:
	for line in jsonFile:
		tweet = json.loads(line)
		text = tweet['text'].encode('utf-8').replace('ö','oe').replace('ä','ae').replace('ü','ue')
		regular = [token.token for token in tokenizer.tokenize(text.lower()) if token.token_class=="regular" and token.token not in twStop]
		hashtag = [token.token for token in tokenizer.tokenize(tweet['text'].lower()) if token.token_class=="hashtag"]
		count_all.update(regular)
		count_hashtags.update(hashtag)
		tokens = tokenizer.tokenize(tweet['text'])
		print text
		for token in tokenizer.tokenize(text):
			print token.token + " ist " + token.token_class

print "Häufigste Worte: " 
for word in count_all.most_common(10):
	print word[0]
print "Häufigste Hashtags: " 
print count_hashtags.most_common(10)
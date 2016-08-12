#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import io
import json
from nltk.tokenize import TweetTokenizer
from pattern.de import parse, split

tknzr = TweetTokenizer(preserve_case=True)

with io.open("data/fluechtlinge.json", encoding='utf-8') as jsonFile:
	for line in jsonFile:
		tweet = json.loads(line)
		text = tweet['text'].encode('utf-8').replace('ö','oe').replace('ä','ae').replace('ü','ue')
		tt = tknzr.tokenize(text)
		print tt
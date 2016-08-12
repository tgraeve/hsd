#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import io
import json
import re
from collections import Counter
import treetaggerwrapper
from nltk import bigrams
from nltk import trigrams

class TreeTagger: #nutzt den TreeTagger Ansatz
	tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
	twStop = set(io.open('resources/german_stopwords.txt', encoding='utf-8').read().splitlines())
	def __init__(self):
		pass

	#tagged JSON Tweets und gibt Tag Objekte als namedtuple aus.
	def tagJson(self,path):
		tags = []
		with io.open(path, 'r') as jsonFile:
			for line in jsonFile:
				tweet = json.loads(line)
				text = preprocessTweetText(tweet['text'])
				tag = self.tagText(text)
				tags.append(tag)
		return tags

	def tagText(self,text):
		cleared_text = preprocessTweetText(text)
		tags = self.tagger.tag_text(cleared_text, notagemail=True, notagdns=True)
		tags2 = treetaggerwrapper.make_tags(tags)
		return tags2
			
	#zählt tags aus obiger Liste und gibt collection zurück.
	def countTags(self,tags):
		count_all = Counter()
		for list in tags:	
			for tag in list:
				if type(tag).__name__ is "Tag":
					if tag.pos == "NN" and tag.lemma not in self.twStop and len(tag.lemma.encode('utf-8')) >1:
						print tag.lemma
						count_all.update([tag.lemma])
		return count_all

class ngrams:

	def __init__(self):
		pass

# STOPWORD REMOVAL IN PREPROCESS?
	@staticmethod
	def bigrams(path):
		twStop = set(io.open('resources/german_stopwords.txt', encoding='utf-8').read().splitlines())
		with io.open(path, 'r') as jsonFile:
			for line in jsonFile:
				tokens = []
				tweet = json.loads(line)
				text = preprocessTweetText(tweet['text'])
				tags = TreeTagger.tagText(text)
				for tag in tags:
					if type(tag).__name__ is "Tag":
						if tag.pos == "NN" and tag.lemma not in twStop and len(tag.lemma.encode('utf-8')) >1:
							tokens.append(tag.lemma)
				bi_tokens = bigrams(tokens)
				print [(item) for item in sorted(set(bi_tokens))]


def preprocessTweetText(text):

	uml_text = text.lower().replace(u'\u201c','').replace(u'\u201e','').replace(u'\u00c4','Ae').replace(u'\u00e4','ae').replace(u'\u00d6','Oe').replace(u'\u00f6','oe').replace(u'\u00dc','Ue').replace(u'\u00fc','ue')
	cleared_text = re.sub(r"\@\w+", "", uml_text) #entfernt alle mentions, beginnend mit @
	return cleared_text

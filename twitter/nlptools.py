#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import io
import json
import re
from collections import Counter
import treetaggerwrapper
import nltk
from nltk import bigrams
from nltk import trigrams
from nltk import FreqDist
from nltk.collocations import *

class TreeTagger: #Funktionen mit TreeTagger Funktionalität
	tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
	twStop = set(io.open('resources/german_stopwords.txt', encoding='utf-8').read().splitlines())
	def __init__(self):
		pass

	#wendet TreeTagger auf JSON-Tweetdatei an und gibt die Frequency Distribuition aus, sonst namedtuple
	def tagJson(self,path, asFD=True, FDtoText=True):
		tags = []
		all_NN = []
		with io.open(path, 'r') as jsonFile:
			for line in jsonFile:
				tweet = json.loads(line)
				text = preprocessTweetText(tweet['text'])
				tags = self.tagText(text)
				for tag in tags:
					if type(tag).__name__ is "Tag":
						if tag.pos == "NN" and tag.lemma not in self.twStop and len(tag.lemma.encode('utf-8')) >1:
							all_NN.append(tag.lemma.lower().encode('utf-8'))
		if not asFD:
			return tags
		else:
			tagFD = FreqDist(all_NN)
			if FDtoText:
				self.toTextfile(path, tagFD)
			return tagFD

	#wendet TreeTagger auf Eingabestring an
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
						count_all.update([tag.lemma.lower().encode('utf-8')])
		return count_all

	def toTextfile(self,path, tags):
		with open(path.replace(".json","")+"FD"+".txt",'w') as f:
			for item in tags.most_common():
				f.write(item[0]+"; "+str(item[1])+"\n")

class ngrams:
	def __init__(self):
		pass

	def bigrams(self,path): #bildet bigrams aus NN-Tokens
		tagger = TreeTagger()
		all_bigrams = []
		twStop = set(io.open('resources/german_stopwords.txt', encoding='utf-8').read().splitlines())
		with io.open(path, 'r') as jsonFile:
			for line in jsonFile:
				tokens = []
				tweet = json.loads(line)
				text = preprocessTweetText(tweet['text'])
				tags = tagger.tagText(text)
				for tag in tags:
					if type(tag).__name__ is "Tag":
						if tag.pos == "NN" and tag.lemma not in twStop and len(tag.lemma.encode('utf-8')) >1:
							tokens.append(tag.lemma.lower().encode('utf-8'))
				bi_tokens = list(bigrams(tokens))
				if bi_tokens:
					for i in bi_tokens:
						all_bigrams.append(i)
		return all_bigrams

	def collocations(self,path):
		tagger = TreeTagger()
		bigram_measures = nltk.collocations.BigramAssocMeasures()
		scored_tokens = []
		twStop = set(io.open('resources/german_stopwords.txt', encoding='utf-8').read().splitlines())
		with io.open(path, 'r') as jsonFile:
			for line in jsonFile:
				tokens = []
				tweet = json.loads(line)
				text = preprocessTweetText(tweet['text'])
				tags = tagger.tagText(text)
				for tag in tags:
					if type(tag).__name__ is "Tag":
						if tag.pos == "NN" and tag.lemma not in twStop and len(tag.lemma.encode('utf-8')) >1:
							tokens.append(tag.lemma.lower().encode('utf-8'))
				finder = BigramCollocationFinder.from_words(tokens)
				scored = finder.score_ngrams(bigram_measures.raw_freq)
				if scored:
					for i in scored:
						scored_tokens.append(i)

		return sorted(bigram for bigram, score in scored_tokens)

	def bigram_fd(self,path,toText=False):
		tagger = TreeTagger()
		all_bigrams = []
		twStop = set(io.open('resources/german_stopwords.txt', encoding='utf-8').read().splitlines())
		with io.open(path, 'r') as jsonFile:
			for line in jsonFile:
				tokens = []
				tweet = json.loads(line)
				text = preprocessTweetText(tweet['text'])
				tags = tagger.tagText(text)
				for tag in tags:
					if type(tag).__name__ is "Tag":
						if tag.pos == "NN" and tag.lemma not in twStop and len(tag.lemma.encode('utf-8')) >1:
							tokens.append(tag.lemma.lower().encode('utf-8'))
				bi_tokens = list(bigrams(tokens))
				if bi_tokens:
					for i in bi_tokens:
						all_bigrams.append(i)
		fd = FreqDist(all_bigrams)
		if toText:
			with open(path.replace(".json",".txt"),'w') as f:
				for item in fd.most_common():
					f.write(item[0][0]+","+item[0][1]+"; "+str(item[1])+"\n")
		else:
			return fd


def preprocessTweetText(text):

	uml_text = text.replace(u'\u201c','').replace(u'\u201e','').replace(u'\u00c4','Ae').replace(u'\u00e4','ae').replace(u'\u00d6','Oe').replace(u'\u00f6','oe').replace(u'\u00dc','Ue').replace(u'\u00fc','ue')
	low_text = uml_text.lower()
	cleared_text = re.sub(r"\@\w+", "", low_text) #entfernt alle mentions, beginnend mit @
	return cleared_text

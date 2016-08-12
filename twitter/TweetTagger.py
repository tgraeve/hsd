#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import io
import json
import re
from collections import Counter
import treetaggerwrapper

class TreeTagger:

	def __init__(self):
		pass

		@staticmethod
		def tagJson(path):
			tagger = treetaggerwrapper.TreeTagger(TAGLANG='de')
			twStop = set(io.open('resources/german_stopwords.txt', encoding='utf-8').read().splitlines())

		with io.open(path) as jsonFile:
			for line in jsonFile:
				tweet = json.loads(line)
				text = tweet['text'].lower().replace(u'\u201c','').replace(u'\u201e','').replace(u'\u00c4','Ae').replace(u'\u00e4','ae').replace(u'\u00d6','Oe').replace(u'\u00f6','oe').replace(u'\u00dc','Ue').replace(u'\u00fc','ue')
				text = re.sub(r"\@\w+", "", text) #entfernt alle mentions, beginnend mit @
				tags = tagger.tag_text(text, notagemail=True)
				tags2 = treetaggerwrapper.make_tags(tags)
		return tags2
				
		@staticmethod
		def countTags(tags):
			count_all = Counter()
			for tag in tags:
					if type(tag).__name__ is "Tag":
						if tag.pos == "NN" and tag.lemma not in twStop and len(tag.lemma.encode('utf-8')) >1:
							print tag.lemma
							count_all.update([tag.lemma])
			return count_all
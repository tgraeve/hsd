#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
from nlptools import TreeTagger
from nlptools import ngrams

tagger = TreeTagger()
tags = tagger.tagJson("data/fluechtlinge.json")
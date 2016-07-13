#!/usr/bin/env python
# This Python file uses the following encoding: utf-8

from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()

myText = "Flüchtlinge klauen mir den Arbeitsplatz!"
response = alchemyapi.sentiment("text", myText)
print "Sentiment: ", response["docSentiment"]["type"]
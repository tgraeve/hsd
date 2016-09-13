# This python file uses the following encoding: utf-8

from geocoder import hsdGeocoder

geo = hsdGeocoder()

geo.json2cities("homophobie")
#geo.cities2coords("homophobie")
#geo.pop_normalizer("homophobie")
#geo.tweet_normalizer("homophobie")

print "--- main.py FINISHED ---"
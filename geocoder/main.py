# This python file uses the following encoding: utf-8

from geocoder import hsdGeocoder

geo = hsdGeocoder()

#geo.json2cities("fluechtlinge")
#geo.cities2coords("fluechtlinge")
#geo.pop_normalizer("fluechtlinge")
geo.tweet_normalizer("fluechtlinge")

print "--- main.py FINISHED ---"
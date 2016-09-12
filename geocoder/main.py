# This python file uses the following encoding: utf-8

from geocoder import hsdGeocoder

g = hsdGeocoder()

g.json2cities("homophobie")
#g.cities2coords("homophobie")
#g.pop_normalizer("homophobie")

print "--- main.py FINISHED ---"
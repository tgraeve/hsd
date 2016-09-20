# This python file uses the following encoding: utf-8

"""
Diese Datei dient zum Ausführen der Methoden aus geocoder.py
"""

from geocoder import hsdGeocoder

geo = hsdGeocoder()

geo.json2cities("fluechtlinge")
#geo.cities2coords("fluechtlinge")
#geo.pop_normalizer("fluechtlinge")
#geo.tweet_normalizer("fluechtlinge_rapefugees")

print "--- main.py FINISHED ---"
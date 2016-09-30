# This python file uses the following encoding: utf-8

"""
Diese Datei dient zum Ausführen der Methoden aus geocoder.py
"""

from geocoder import hsdGeocoder
from time import *

geo = hsdGeocoder()

t1 = clock()
geo.json2cities("fluechtlinge")
t2 = clock()

# t1 = clock()
# geo.cities2coords("normalize")
# t2 = clock()

# t1 = clock()
# geo.pop_normalizer("normalize")
# t2 = clock()

# t1 = clock()
# geo.tweet_normalizer("fluechtlinge")
# t2 = clock()

t = t2 - t1
print "Runtime: " + str(t)
print "--- main.py FINISHED ---"
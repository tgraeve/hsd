#!/usr/bin/env python
# This Python file uses the following encoding: utf-8
import JsonExtractor

extr = JsonExtractor.Json2Csv()

extr.extract("/home/hsd/twitter/data/wacken")

print "DONE."
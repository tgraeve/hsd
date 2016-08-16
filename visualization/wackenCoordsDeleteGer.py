import csv
import geocoder

ifile = open('txt/wacken_coordsBACKUP_ALL.txt', "rb")
reader = csv.reader(ifile)
ofile = open('txt/wacken_coordsBACKUP_ALL_WITHOUT_GER.txt', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

for row in reader:
	if row[0] not in ("\"51.165691, 10.451526\""):
		writer.writerow(row)

print "------------------ wackenCoordsDeletGer.py FINISHED ------------------"

ifile.close()
ofile.close()
#!/usr/bin/python

import os
import shelve
"""
filepath = os.getcwd()+ "/pdf/db/000882.pdf"
os.chdir(filepath)

shelfFile = shelve.open('2-gram.txt')
shelfFile20 = shelve.open('20-gram.txt')
setGram = shelfFile['gram']
setGram20 = shelfFile20['gram']

listGram20 = list(setGram20)
print listGram2.index('\xbb\x96\xf9\x1a\x1a\xa37\xb2@\xdb{q&\xcf\xbe_\x94\xd6m\xc7')
print listGram2[1447]
print listGram20
print len(listGram20)


shelfFile.close()
shelfFile20.close()
"""

filepath = os.getcwd()+ "/pdf"
os.chdir(filepath)

db = shelve.open('pdf-unfiltered.db')
for i in range(1,20) :
	ngram = "%d-gram" % i
	setGram = db[ngram]
	print "{} panjang {}".format(ngram, len(setGram))
	print setGram

		

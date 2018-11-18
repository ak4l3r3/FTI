#!/usr/bin/python
"""
fileList = ['./pdf/db/000012.pdf/20-gram.txt.db', './pdf/db/000022.pdf/20-gram.txt.db', './pdf/db/000236.pdf/20-gram.txt.db', './pdf/db/000251.pdf/20-gram.txt.db', './pdf/db/000263.pdf/20-gram.txt.db', './pdf/db/000266.pdf/20-gram.txt.db', './pdf/db/000356.pdf/20-gram.txt.db', './pdf/db/000360.pdf/20-gram.txt.db', './pdf/db/000368.pdf/20-gram.txt.db', './pdf/db/000369.pdf/20-gram.txt.db', './pdf/db/000567.pdf/20-gram.txt.db', './pdf/db/000587.pdf/20-gram.txt.db', './pdf/db/000605.pdf/20-gram.txt.db', './pdf/db/000606.pdf/20-gram.txt.db', './pdf/db/000738.pdf/20-gram.txt.db', './pdf/db/000742.pdf/20-gram.txt.db', './pdf/db/000757.pdf/20-gram.txt.db', './pdf/db/000818.pdf/20-gram.txt.db', './pdf/db/000840.pdf/20-gram.txt.db', './pdf/db/000882.pdf/20-gram.txt.db']

print fileList[0]

for files in fileList[1::] :
	print files
"""
import os
import shelve

def stripCommonNgram(path, fileType) : 
	db = shelve.open(path)
	for i in range(1,21) :
		ngram = "%d-gram" % i
		setGram = db[ngram]
		print "{} panjang {}".format(ngram, len(setGram))
		print setGram


listFileType = ['pdf','bmp','doc','png']
path = os.getcwd() + "/"
for fileType in listFileType :
	files = path + fileType + "/" + fileType + "-unfiltered"
	print files
	ngramUnique = shelve.open(fileType)
	stripCommonNgram(files, fileType)
#!/usr/bin/python

import shelve
import os

filepath = os.getcwd()+ "/PDF/db/1"
os.chdir(filepath)

shelfFile = shelve.open('2-gram.txt')
shelfFile2 = shelve.open('3-gram.txt')
setGram = shelfFile['gram']
setGram2 = shelfFile2['gram']

listGram2 = list(setGram2)
print listGram2.index('pdf')
print listGram2[1447]
print listGram2


shelfFile.close()
shelfFile2.close()
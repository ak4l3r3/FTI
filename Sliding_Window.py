#!/usr/bin/python


import os
import errno
import time
import sys
import shelve

def bytes2int(str):
	return int(str.encode('hex'), 16)

def int2bytes(i):
 	h = int2hex(i)
 	return hex2bytes(h)

def hex2bytes(h):
 	if len(h) > 1 and h[0:2] == '0x':
		h = h[2:]
	
 	if len(h) % 2:
		h = "0" + h
 	return h.decode('hex')

def int2hex(i):
 	return hex(i)

def slidingWindow(sequence,winSize,step):

	# Pre-compute number of chunks to emit
	numOfChunks = int(((len(sequence)-winSize)/step)+1)
	
	#print(numOfChunks*step)
 
	# Do the work
	for i in range(0,numOfChunks*step,step):
		yield sequence[i:i+winSize]

def normalizeChar(sequence):
	normalize = sequence
	return normalize


filepath = os.getcwd()+ "/PDF/db/1"
filename = "000020.pdf"
filetemp = filepath + "/" + filename + "-temp"

start = time.time()

# Membuat subdir
if not os.path.exists(os.path.dirname(filetemp)):
	try:
		os.makedirs(os.path.dirname(filetemp))
	except OSError as exc: # Guard against race condition
		if exc.errno != errno.EEXIST:
			raise
#summarisasi uppercase to lowercase
			
with open(filename, 'rb') as in_file, open(filetemp, "wb") as out_file:
	data = 1
	try :
		while data:
			data = in_file.read(1)
			if (ord(data) > 64 and ord(data) < 91):
				number = bytes2int(data) + 32
				data = int2bytes(number)
				out_file.write(data)
			else:		
				out_file.write(data)
	except Exception as eror:
			print eror



os.chdir(filepath)
filetemp = filename + "-temp"

with open(filetemp, "rb") as in_file :
 	try :
		
		byteSequence = in_file.read()

		byteNormalizeSequence = normalizeChar(byteSequence)

		print("Panjang sequence : %d" % len(byteSequence))
		
		for i in range(1,21):
			
			winSize = i
			step = 1
			chunks = slidingWindow(byteSequence,winSize,step)
			listGram = []
			setGram = []
			filegram = "%d-gram.txt" % i
	
			for chunk in chunks:
				listGram.append(chunk)
							
			setGram = set(listGram)
			
			shelfFile = shelve.open(filegram)
			shelfFile['gram'] = setGram
			shelfFile.close()
					
		end = time.time()
		print "Time execution {} second".format(end - start)
		
	except Exception as im:
		print im
		print type(chunks)






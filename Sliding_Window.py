#!/usr/bin/python

import os

def slidingWindow(sequence,winSize,step):
	"""Returns a generator that will iterate through
	the defined chunks of input sequence.  Input sequence
	must be iterable."""
 
	# Verify the inputs
	try: it = iter(sequence)
	except TypeError:
		raise Exception("**ERROR** sequence must be iterable.")
	if not ((type(winSize) == type(0)) and (type(step) == type(0))):
		raise Exception("**ERROR** type(winSize) and type(step) must be int.")
	if step > winSize:
		raise Exception("**ERROR** step must not be larger than winSize.")
	if winSize > len(sequence):
		raise Exception("**ERROR** winSize must not be larger than sequence length.")
 
	# Pre-compute number of chunks to emit
	numOfChunks = int(((len(sequence)-winSize)/step)+1)
	
	print(numOfChunks*step)
 
	# Do the work
	for i in range(0,numOfChunks*step,step):
		yield sequence[i:i+winSize]


Filename = open("gigih.JPG","rb")
byteSequence = Filename.read()

print("Panjang sequence : %d" % len(byteSequence))

for i in range(2,19):
	arraybyteSequence = bytearray(byteSequence)
	winSize = i
	step = 1
	chunks = slidingWindow(byteSequence,winSize,step)


	filename = "%d-gram.txt" % i
	fd = open(filename,"wb")
	for chunk in chunks:
		#print(chunk)
		fd.write(chunk)
		fd.write(b"\n")
	fd.close()

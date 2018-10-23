#!/usr/bin/python

import os
import time
def slidingWindow(sequence,winSize,step):
	
	# Pre-compute number of chunks to emit
	numOfChunks = int(((len(sequence)-winSize)/step)+1)
	
	print(numOfChunks*step)
 
	# Do the work
	for i in range(0,numOfChunks*step,step):
		yield sequence[i:i+winSize]



Filename = open("gigih.JPG","rb")
start = time.time()
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
end = time.time()
print "Time execution {} second".format(end - start)
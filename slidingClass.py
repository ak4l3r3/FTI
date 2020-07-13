#Gigih
#!/usr/bin/python

import os, errno, time, sys, shelve

class slidingClass():
	
	def __init__(self, filename, sourceDir, targetDir):
		self.filename = filename
		self.sourceDir = sourceDir
		self.targetDir = targetDir 
		
	def bytes2int(self, str):
		return int(str.encode('hex'), 16)

	def int2bytes(self, i):
		h = self.int2hex(i)
		return self.hex2bytes(h)

	def hex2bytes(self, h):
		if len(h) > 1 and h[0:2] == '0x':
			h = h[2:]
		
		if len(h) % 2:
			h = "0" + h
		return h.decode('hex')

	def int2hex(self, i):
		return hex(i)

	def slidingWindow(self, sequence,winSize,step):

		# Pre-compute number of chunks to emit
		numOfChunks = int(((len(sequence)-winSize)/step)+1)
		
		for i in range(0,numOfChunks*step,step):
			yield sequence[i:i+winSize]

	def normalizeChar(self, sequence):
		normalize = sequence
		return normalize
				
	def summarized(self):
		#filepath = os.getcwd() + self.targetDir
		filetemp = self.targetDir + "/" + self.filename + "-temp"	
		#targetDir = sourceDir + "/db/" + str(files)
		
		print filetemp
		if not os.path.exists(os.path.dirname(filetemp)):
			try:
				os.makedirs(os.path.dirname(filetemp))
			except OSError as exc: # Guard against race condition
				if exc.errno != errno.EEXIST:
					raise	
		
		with open(self.sourceDir + "/" + self.filename, 'rb') as in_file, open(filetemp, "wb") as out_file:
			data = 1
			try :
				while data:
					data = in_file.read(1)
					if (ord(data) > 64 and ord(data) < 91):
						number = self.bytes2int(data) + 32
						data = self.int2bytes(number)
						out_file.write(data)
					else:		
						out_file.write(data)
			except Exception as eror:
					print eror
					
		
		with open(filetemp, "rb") as in_file :
		 	try :
				byteSequence = in_file.read()
				byteNormalizeSequence = self.normalizeChar(byteSequence)
				print("Panjang sequence : %d" % len(byteSequence))
				
				for i in range(1,21):					
					winSize = i
					step = 1
					chunks = self.slidingWindow(byteSequence,winSize,step)
					listGram = []
					setGram = []
					filegram = "/%d-gram.txt" % i
					filegram = self.targetDir + filegram
					for chunk in chunks:
						listGram.append(chunk)
									
					setGram = set(listGram)
					
					shelfFile = shelve.open(filegram)
					shelfFile['gram'] = setGram
					shelfFile.close()
				
			except Exception as im:
				print im
					
# end of class

start = time.time()

if __name__ == "__main__":
	fileLearning = []
	filetype = "txt"
	sourceDir = os.getcwd() + "/" + filetype
	
	for namafile in os.listdir(sourceDir) :
		if namafile.endswith('.' + filetype):
			fileLearning.append(namafile)
	
	for files in fileLearning:
		targetDir = sourceDir + "/db/" + str(files)
		corpus = slidingClass(files, sourceDir, targetDir)
		corpus.summarized()
		
	end = time.time()
	print "Time execution {} second".format(end - start)

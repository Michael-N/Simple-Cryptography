class cryptoErr(BaseException):
	#This is the error class that will be raised if there is a problem
	def __init__():
		self.errName = ''
		self.errValue = None
		self.errHandler = None
		self.errMetaData = ''
		self.errUsrMsg = ''
		return
	def handle(self):
		if self.errHandler != None:
			try:
				errHandler()
			except:
				return
		else:
			return
class map(object):
	def __init__(self,mapI,err = -1,):
		#consider adding a map sequence so that certin letters map to certin numbers
		#mapSequence = range(0,len(mapI))
		self.mapLength = len(mapI)
		self.mapI = mapI
		self.err = err
		self.mod = int(len(mapI))
		return
	def __call__(self,chrNum):
		#will convert any string to a chr and any chr to a num according to the map
		if type(chrNum) == str:
			for index in range(0,self.mapLength):
				if chrNum == self.mapI[index]:
					return int(index)
				else:
					continue
			return self.err
		elif type(chrNum) == int:
			if 0 <= chrNum < self.mapLength:
				return str(self.mapI[chrNum])
			else:
				return self.err
		else:
			raise self.err
	def setMap(self,mapB):
		self.mapI = mapB
		self.mod = len(mapB)
		self.mapLength = len(mapB)
		return
class caesar(object):
	def __init__(self):
		self.cipherType = 'caesar'
		self.defMap = map('abcdefghijklmnopqrstuvwxyz')
		self.enVariance = [0.0867,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02361,0.00150,0.01974,0.00074]
		return
	def opp(t):
		if t == True:
			return False
		elif t == False:
			return True
	def chrToNum(self, char,forceMap = False):
		#converts a character to a number based upon the classes self.defMap
		if forceMap == False:
			forceMap = self.defMap
		num = forceMap(char)
		return 	num
	def setMap(self,mapN):
		#takes a map as an argument
		self.defMap = mapN
		return 
	def numToChr(self, num,forceMap = False):
		if forceMap == False:
			forceMap = self.defMap
		#converts a number to a character based upon the classes self.defMap
		char  = forceMap(num)
		return char
	def az(self, letter):
		#checks if a letter is a to z 
		if 97 <= ord(letter) <= 122:
			return True
		else:
			return False
	def sanitizeMsg(self,msg,rmvChrs):
		for index in range(0, len(msg)):
			for letterB in rmvChrs:
				if msg[index] == letterB:
					msg[index] == ''
				else:
					continue
		return msg
	def encrypt(self,msg,key):
		#ENCRYPTION CODE
		encrypted = ''
		for letter in msg:
			en = self.defMap(letter)
			if en == self.defMap.err:
				pass
			else:
				encrypted += str(self.numToChr((self.chrToNum(letter) + key) % self.defMap.mod))
		return encrypted
	def decrypt(self,msg,key):
		#DECRYPTION CODE
		decrypted = ''
		for letter in msg:
			de = self.defMap(letter)
			if de == self.defMap.err:
				pass
			else:
				decrypted += str(self.numToChr((self.chrToNum(letter) - key) % self.defMap.mod))
		return decrypted
	def frequencyAnalysis(self,msg):
		#ANALYSIS CODE
		frequency = [0] * self.defMap.mod
		for letter in msg:
			fe = self.defMap(letter)
			if fe == self.defMap.err:
				pass
			else:
				frequency[self.chrToNum(letter)] += 1
		total = 0
		for index in range(0,self.defMap.mod):
			total += frequency[index]
		total = float(total)
		for indexAlpha in range(0,len(frequency)):
			frequency[indexAlpha] = frequency[indexAlpha] / total
		return frequency
	def variance(self,frequency):
		#VARIATION CODE only works for msgs with a self.defMap = map('abcdefghijklmnopqrstuvwxyz')
		if len(frequency) > 26:
			raise BaseException
		else:
			variance = 0
			englishVariance = [0.0867,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02361,0.00150,0.01974,0.00074]
			for index in range(0,26):
				variance += abs(englishVariance[index]-frequency[index])
			return variance
	def noKeysDecrypt(self,msg):
		#NO KEY DECRYPTION CODE # returns a list where the first item is the decrypted msg and the 2nd the key 
		key = 0
		lowestVariance = 1000
		testKey = 0
		for index in range(0,self.defMap.mod):
			testDecrypt = self.decrypt(msg,key)
			testFrequency = self.frequencyAnalysis(testDecrypt)
			testVariance = variance(testFrequency)
			if testVariance < lowestVariance:
				lowestVariance = testVariance
				testKey = key
			key += 1 
		return [self.decrypt(msg,testKey), testKey]
class afine(caesar,object):
	def __init__(self):
		self.cipherType = 'afine'
		self.defMap = map('abcdefghijklmnopqrstuvwxyz')
		return
	def getValidMultkeys(self,num):
		# Should retrun all intigers relativly prime to num
		validKeys = []
		for indexA in range(0,num):
			for indexB in range(0,num):
				if ((indexA *indexB) % num) == 1:
					validKeys.append(indexA)
				else:
					continue
		return validKeys
	def getInvrsMultKey(self,key):
		# gets the inverse of the mult key , asumes 26 , watches for keys that do not have a reverse
		inverseKey = None
		for index in range(0,self.defMap.mod):
			if ((key * index) % self.defMap.mod) == 1:
				inverseKey = index
			else:
				continue
		return inverseKey
	def getInvrsAddKey(self,key,delta = 'neg'):
		#or delta = 'neg', assumes 26, only accepts positive keys
		if delta == 'neg':
			keyN = 0 - key
			return keyN
		else:
			keyN = self.defMap.mod -key ######## THIS MAY CAUSE AN ERROR 
			return keyN
	def encrypt(self, msg,multKey,addKey):
		#ENCRYPTION CODE
		encrypted = ''
		for letter in msg:
			en =  self.defMap(letter)
			if en == self.defMap.err:
				pass
			else:
				encrypted += str(self.numToChr(((self.chrToNum(letter) + addKey) * multKey) % self.defMap.mod))
		return encrypted
	def decrypt(self,msg,multKey,addKey):
		#DECRYPTION CODE
		decrypted = ''
		for letter in msg:
			de = self.defMap(letter)
			if de == self.defMap.err:
				pass
			else:
				decrypted += str(self.numToChr(((self.chrToNum(letter) * self.getInvrsMultKey(multKey)) + self.getInvrsAddKey(addKey)) % self.defMap.mod))
		return decrypted
	def noKeysDecrypt(self,msg):
		#NO KEY DECRYPTION CODE
		lowestVariance = 1000
		testMultKey = None
		testAddKey = None
		for indexA in getValidMultkeys(self.defMap.mod):
			for indexB in range(0,self.defMap.mod):
				testDecrypt = self.decrypt(msg, indexA,indexB)
				testFrequency = frequencyAnalysis(testDecrypt)
				testVariance = variance(testFrequency)
				if testVariance < lowestVariance:
					lowestVariance = testVariance
					testMultKey = indexA
					testAddKey = indexB
		return [self.decrypt(msg,testMultKey,testAddKey),testMultKey,testAddKey]
class viginere(afine):
	def __init__(self):
		self.cipherType = 'viginere'
		self.defMap = map('abcdefghijklmnopqrstuvwxyz')
		return
	def encrypt(self,msg, keyWord):
		#ENCRYPTION CODE
		encrypted = ''
		counter = 0
		lenK = len(keyWord)
		for letter in msg:
			en = self.defMap(letter)
			if en == self.defMap.err:
				pass
			else:
				encrypted += str(self.numToChr((self.chrToNum(letter) + self.chrToNum(keyWord[counter])) % self.defMap.mod))
				counter += 1
				if counter == lenK:
					counter = 0
		return encrypted
	def decrypt(self, msg, keyWord):
		#DECRYPTION CODE
		decrypted = ''
		counter = 0
		lenK = len(keyWord)
		for letter in msg:
			de = self.defMap(letter)
			if de == self.defMap.err:
				pass
			else:
				decrypted += self.numToChr((self.chrToNum(letter) - self.chrToNum(keyWord[counter])) % 26)
				counter += 1
				if counter == lenK:
					counter = 0
		return decrypted
	def keysValidate(self,key):
		#KEY VALIDATION tests if the key will work based upon the defMap and format
		if (key != str) | (self.defMap(key) == self.defMap.err):
			return false
		return True
	def msgValidate(self, msg):
		#MSG VALIDATION CODE
		for letter in msg:
			if self.defMap(letter) == self.defMap.err:
				return False
			else:
				continue
		return True
	def noKeysDecrypt(self):
		#NO KEY DECRYPTION CODE
		return True
	def search(self,text,target,startInxex = 0):
		#SEARCH THE text srting for a target strng, and does so from the starting index
		# returns a list of the starting index of each hit
		hitsIndexes = []
		txtLen = len(text)
		if len(target)> len(text):
			return []
		for indexA in range(startInxex,txtLen):
			testTarget = ''
			for indexB in range(0,len(target)):
				if (indexA + indexB) > (txtLen-1):
					pass
				else:
					testTarget += text[indexA + indexB]
			if target == testTarget:
				hitsIndexes.append(indexA)
		return hitsIndexes
	def getRepetes(self,textSource,maxLen = 10,startInxexN = 0):
		'''looks at a textN and returns a dictionary where the key is a hit for a repete string and the
			key's value is a list of all the start unique start indexes of that repete string, the function
			searches for repetes maxLen in length and starts searching the text at startIndexN
		'''
		repetes = {}
		txtLen = len(textSource)
		for indexA in range(startInxexN,txtLen):
			testRepete = ''
			testIndex = indexA + 1
			for indexB in range(0,maxLen):
				if (indexA + indexB)> (len(textSource)-1):
					pass
				else:
					testRepete += textSource[indexA + indexB]
			testList = self.search(textSource,testRepete, testIndex)
			print(testList)
			if testList != []:
				for indexAItem in testList:
					if testRepete not in repetes:
						repetes[testRepete] = []
						continue
					else:
						continue
					for indexBItem in repetes[testRepete]:
						if indexAItem != indexBItem:
							repetes[testRepete].append(indexAItem)
						else:
							continue
			else:
				continue
		return repetes
class viginereOld(viginere):
	def __init__(self):
		self.cipherType = 'viginereold'
		self.defMap = map('abcdefghijklmnopqrstuvwxyz')
	def encrypt(self,msg, keyWord):
		#ENCRYPTION CODE
		encrypted = ''
		counter = 0
		lenK = len(keyWord)
		for letter in msg:
			en = self.defMap(letter)
			if en == self.defMap.err:
				pass
			else:
				encrypted += str(self.numToChr((self.chrToNum(letter) + self.chrToNum(keyWord[counter])) % self.defMap.mod))
				counter += 1
				if counter == lenK:
					keyWord = encrypted[(len(encrypted)-lenK): len(encrypted)]
					counter = 0
		return encrypted
	def decrypt(self, msg, keyWord):
		#DECRYPTION CODE
		decrypted = ''
		counter = 0
		lenK = len(keyWord)
		for letter in msg:
			de = self.defMap(letter)
			if de == self.defMap.err:
				pass
			else:
				decrypted += self.numToChr((self.chrToNum(letter) - self.chrToNum(keyWord[counter])) % 26)
				counter += 1
				if counter == lenK:
					keyWord = msg[(len(decrypted)-lenK) : len(decrypted)]
					counter = 0
		return decrypted
	def noKeysDecrypt(self):
		#NO KEY DECRYPTION CODE ???????????
		return True
		#INHERITS .searchMsg()

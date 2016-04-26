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
		self.mod = len(mapI)
	def __call__(self,chrNum):
		#will convert any string to a chr and any chr to a num according to the map
		if type(chrNum) == str:
			for index in range(0,self.mapLength):
				if chrNum == self.mapI[index]:
					return index
				else:
					continue
			return self.err
		elif type(chrNum) == int:
			if self.mapLength <= chrNum <= self.mapLength:
				return self.mapI[chrNum]
			else:
				return self.err
		else:
			raise self.err
class caesar(object):
	def __init__(self):
		self.cipherType = 'caesar'
		self.defMap = map('abcdefghijklmnopqrstuvwxyz')
		return
	def opp(t):
		if t == True:
			return False
		elif t == False:
			return True
	def chrToNum(self, char):
		#converts a character to a number based upon the classes self.defMap
		num = self.defMap(char)
		return 	num
	def setMap(self,mapN):
		#takes a map as an argument
		self.defMap = mapN
		return 
	def numToChr(self, num):
		#converts a number to a character based upon the classes self.defMap
		char  = self.defMap(num)
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
				encrypted += self.numToChr((self.chrToNum(letter) + key) % self.defMap.mod)
		return encrypted
	def decrypt(self,msg,key):
		#DECRYPTION CODE
		decrypted = ''
		for letter in msg:
			de = self.defMap(letter)
			if de == self.defMap.err:
				pass
			else:
				decrypted += self.numToChr((self.chrToNum(letter) - key) % self.defMap.mod)
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
class afine(caesar):
	def __init__(self):
		self.cipherType = 'afine'
		self.defMap = map('abcdefghijklmnopqrstuvwxyz')
		return
	def phi(num):
		num = num - 1
		return num
	def isRelPrime(n,a):
		#checks if two numbers are relativly prime
		return True
	def GFC(num, numA):
		#Get the greatest common factor of the two numbers
		return True
	def getValidMultkeys(num):
		# Should retrun all intigers relativly prime to num
		validKeys = []
		for indexA in range(0,num):
			for indexB in range(0,num):
				if ((indexA *indexB) % num) == 1:
					validKeys.append(indexA)
				else:
					continue
		return validKeys
	def factor(n):
		#should factor n and return a list of factors
		
		return True
	def isValidMultKey(key,num):
		#check if key is relativly prime to num return true or false
		return True
	def getInvrsMultKey(key):
		# gets the inverse of the mult key , asumes 26 , watches for keys that do not have a reverse
		inverseKey = None
		for index in range(0,26):
			if ((key * index) % 26) == 1:
				inverseKey = index
			else:
				continue
		return inverseKey
	def getInvrsAddKey(key,delta = 'pos'):
		#or delta = 'neg', assumes 26
		if delta == 'neg':
			key = 0-key
			return key
		else:
			key = 25-key ######## THIS MAY CAUSE AN ERROR 
	def encrypt(self, msg,multKey,addKey):
		#ENCRYPTION CODE
		encrypted = ''
		for letter in msg:
			letter = letter.lower()
			if self.az(letter):
				encrypted += self.numToChr(((self.chrToNum(letter) + addKey) * multKey) % self.defMap.mod)
			else:
				continue
		return encrypted
	def decrypt(self,msg,multKey,addKey):
		#DECRYPTION CODE
		decrypted = ''
		for letter in msg:
			letter = letter.lower()
			if self.az(letter):
				decrypted += self.numToChr(((self.chrToNum(letter) * self.getInvrsMultKey(multKey)) - getInvrsAddKey(addKey)) % self.defMap.mod)
			else:
				continue
		return decrypted
	def keysValidate(self,keys):
		if type(keys) != str:
			return False
		elif True:
			for letter in keys:
				if self.opp(self.az(letter)):
					return False
		else:
			return True
	def noKeysDecrypt(self,msg):
		#NO KEY DECRYPTION CODE
		lowestVariance = 1000
		testMultKey = None
		testAddKey = None
		for indexA in getValidMultkeys(26):
			for indexB in range(0,26):
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
		return 
	def encrypt(self,msg, keyWord):
		#ENCRYPTION CODE
		encrypted = ''
		counter = 0
		lenK = len(keyword) -1
		for letter in msg:
			letter = letter.lower()
			if self.az(letter):
				encrypted += self.numToChr((self.chrToNum(letter) + self.chrToNum(keyWord[counter])) % 26)
				counter += 1
				if counter == lenK:
					counter = 0
			else:
				continue
		return encrypted
	def decrypt(self, msg, keyWord):
		#DECRYPTION CODE
		decrypted = ''
		counter = 0
		lenK = len(keyword) -1
		for letter in msg:
			letter = letter.lower()
			if self.az(letter):
				decrypted += self.numToChr((self.chrToNum(letter) - self.chrToNum(keyWord[counter])) % 26)
				counter += 1
				if counter == lenK:
					counter = 0
			else:
				continue
		return decrypted
	def frequencyAnalysis(self):
		#ANALYSIS CODE
		return True
	def msgVariation(self):
		#MSG VARIATION CODE
		return True
	def keysValidate(self):
		#KEY VALIDATION
		return True
	def msgValidate(self):
		#MSG VALIDATION CODE
		return True
	def noKeysDecrypt(self):
		#NO KEY DECRYPTION CODE
		return True
	def searchMsg(self,arg):
		#SEARCH THE self.msg FOR THE arg STRING
		return True
class viginereOldMsg(viginere):
	def __init__(self,keys,msg):
		self.keys = []
		self.cipherType = 'viginereold'
		self.msg = msg
	def encrypt(self):
		#ENCRYPTION CODE
		return True
	def decrypt(self):
		#DECRYPTION CODE
		return True
	def frequencyAnalysis(self):
		#ANALYSIS CODE
		return True
	def msgVariation(self):
		#MSG VARIATION CODE
		return True
	def keysValidate(self):
		#KEY VALIDATION
		return True
	def msgValidate(self):
		#MSG VALIDATION CODE
		return True
	def noKeysDecrypt(self):
		#NO KEY DECRYPTION CODE
		return True
		#INHERITS .searchMsg()

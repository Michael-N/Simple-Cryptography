class caesar(object):
    def __init__(self):
        self.cipherType = 'caesar'
	def chrToNum(char):
		#converts to lower case
		num = ord(char)
		num -= 97
		return num
	def numToChr(num):
		#accepts numbers in lowercase ascii form
		char = ord(num + 97)
		return char
    def encrypt(self,msg,key):
        #ENCRYPTION CODE
		encrypted = ''
		for letter in msg:
			letter = letter.lower()
			if 97 <= ord(letter) <= 122:
				encrypted += numToChr((chrToNum(letter) + key) % 26)
			else:
				continue
		return encrypted
		
    def decrypt(self,msg,key):
        #DECRYPTION CODE
		decrypted = ''
		for letter in msg:
			letter = letter.lower()
			if 97 <= ord(letter) <= 122:
				decrypted += numToChr((chrToNum(letter) - key) % 26)
			else:
				continue
		return decrypted
		
    def frequencyAnalysis(self,msg):
        #ANALYSIS CODE
		frequency = [0] * 26
		for letter in msg:
			if 97 <= ord(letter) <= 122:
				frequency[chrToNum(letter)] += 1
			else:
				continue
		total = 0
		for index in range(0,26):
			total += frequency[index]
		total = float(total)
		for indexAlpha in range(0,len(frequency)):
			frequency[indexAlpha] = frequency[indexAlpha] / total
		return frequency
		
    def msgVariation(self):
        #MSG VARIATION CODE
    def keysValidate(self):
        #KEY VALIDATION
    def msgValidate(self):
        #MSG VALIDATION CODE
    def noKeysDecrypt(self):
        #NO KEY DECRYPTION CODE
class afineMsg(caesarMsg):
    def __init__(self,keys,msg):
        self.keys = []
        self.cipherType = 'afine'
        self.msg = msg
    def encrypt(self):
        #ENCRYPTION CODE
    def decrypt(self):
        #DECRYPTION CODE
    def frequencyAnalysis(self):
        #ANALYSIS CODE
    def msgVariation(self):
        #MSG VARIATION CODE
    def keysValidate(self):
        #KEY VALIDATION
    def msgValidate(self):
        #MSG VALIDATION CODE
    def noKeysDecrypt(self):
        #NO KEY DECRYPTION CODE
class viginereMsg(afineMsg):
    def __init__(self,keys,msg):
        self.keys = []
        self.cipherType = 'viginere'
        self.msg = msg
    def encrypt(self):
        #ENCRYPTION CODE
    def decrypt(self):
        #DECRYPTION CODE
    def frequencyAnalysis(self):
        #ANALYSIS CODE
    def msgVariation(self):
        #MSG VARIATION CODE
    def keysValidate(self):
        #KEY VALIDATION
    def msgValidate(self):
        #MSG VALIDATION CODE
    def noKeysDecrypt(self):
        #NO KEY DECRYPTION CODE
    def searchMsg(self,arg):
        #SEARCH THE self.msg FOR THE arg STRING
class viginereOldMsg(viginereMsg):
    def __init__(self,keys,msg):
        self.keys = []
        self.cipherType = 'viginereold'
        self.msg = msg
    def encrypt(self):
        #ENCRYPTION CODE
    def decrypt(self):
        #DECRYPTION CODE
    def frequencyAnalysis(self):
        #ANALYSIS CODE
    def msgVariation(self):
        #MSG VARIATION CODE
    def keysValidate(self):
        #KEY VALIDATION
    def msgValidate(self):
        #MSG VALIDATION CODE
    def noKeysDecrypt(self):
        #NO KEY DECRYPTION CODE
    #INHERITS .searchMsg()

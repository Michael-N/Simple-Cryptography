class caesar(object):
    def __init__(self):
        self.cipherType = 'caesar'
        return 
        
    def chrToNum(char):
	#converts to lower case
	num = ord(char)
	num -= 97
	return num
	
    def numToChr(num):
	#accepts numbers in lowercase ascii form
	char = ord(num + 97)
	return char
	
    def az(letter):
    	if 97 <= ord(letter) <= 122:
    	   return True
    	else:
    	   return False
    	   
    def encrypt(self,msg,key):
        #ENCRYPTION CODE
		encrypted = ''
		for letter in msg:
			letter = letter.lower()
			if az(letter):
				encrypted += numToChr((chrToNum(letter) + key) % 26)
			else:
				continue
		return encrypted
		
    def decrypt(self,msg,key):
        #DECRYPTION CODE
		decrypted = ''
		for letter in msg:
			letter = letter.lower()
			if az(letter):
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
class afine(caesarMsg):
    def __init__(self):
        self.cipherType = 'afine'
        return
    def getValidMultkeys(num):
    	# Should retrun all intigers relativly prime to num
    def isValidMultKey(key,num):
    	#check if key is relativly prime to num return true or false
    def getInvrsMultKey(key):
    	# gets the inverse of the mult key , asumes 26 , watches for keys that do not have a reverse
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
           if az(letter):
              encrypted += self.numToChr(((self.chrToNum(letter) + addKey) * multKey) % 26)
           else:
              continue
        return encrypted
        
    def decrypt(self,msg,multKey,addKey):
        #DECRYPTION CODE
        decrypted = ''
        for letter in msg:
           letter = letter.lower()
           if az(letter):
              decrypted += self.numToChr(((self.chrToNum(letter) * self.getInvrsMultKey(multKey)) - getInvrsAddKey(addKey)) % 26)
           else:
              continue
        return decrypted
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

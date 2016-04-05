class caesarMsg(object):
    def __init__(self,keys,msg):
        self.keys = []
        self.cipherType = 'caesar'
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

class cryptoMsg(object):
    def __init__(self, keys, msg, cipher, name):
        self.keys = keys #keys[0] is addKey or keyword, eys[1] mult
        self.msg = msg #the message to work with a-z + spaces
        self.cipher = cipher #cipher type ex. Caesar
        self.name = name
        
    def numToChr(self, i):
        #converts numbers 0-25 to a letter a-z
        i = int(i)
        return chr(i + 97)
    
    def chrToNum(self, i):
        #converts Lowercase letters a-z to a number 0-25
        i = i.lower()
        return ord(i)-97
    
    '''def fixMsg(self):
        #Removes harmfull characters / Fixes the self.msg
        self.msg = str(self.msg).lower
        fixedMsg = ''
        for i in self.msg:
            if (97<= ord(i) <= 122):
                fixedMsg += i
            else:
                pass
        self.msg = fixedMsg'''
        
    '''def msgValidate(self):
        #checks msg to see if it is a string,assumes lower case, accepts a-z . Spaces
        will check to make sure that the code is compatable with the other functions and return false if otherwise
        if (type(self.msg)== str):
            for i in self.msg:
                if (97<= ord(i) <= 122)| ( ord(i) == 32) | (ord(i) == 46):
                    return true
                else:
                    return false, 'Error: ' + i + ' Character not supported'
        else:
            return false,'Error: msg is not a string' '''
        
    def frequencyAnalysis(self):
        #returns the frequency of self.msg a in a list decimal percentage ex. 0.05 for 5%
        #List index 0 = the percentage for a etc...
        msgFreq = [0]*26
        total = 0
        for i in range(0,len(self.msg)):
            #exclude . and spaces
            if (ord(self.msg[i]) == 32) |(ord(self.msg[i]) == 46):
                pass
            else:
                index = self.chrToNum(self.msg[i])
                msgFreq[index] += 1
        for t in range(0,len(msgFreq)):
            total += msgFreq[t]
        for y in range(0,len(msgFreq)):
            msgFreq[y] = float(msgFreq[y]/total)
        return msgFreq
    
    def varianceAnalysis(self):
        #returns the self.msg Variance as a float
        #english variance a,b.......
        eng = [0.0867,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02361,0.00150,0.01974,0.00074]
        mssg = self.frequencyAnalysis() 
        total = 0
        for i in range(0,len(mssg)):
            total += abs(eng[i]-mssg[i])
        return total
    
    '''def cryptoHelp(self):
        return true'''
    '''def searchMsg(self,target):
        #returns the start,end index of the matched text 
        hits = []
        for i in range(0,len(self.msg)):
            testText = ''
            for u in range(0,len(target)):
                testText[i] += self.msg[i + u]
            if testText == target:
                hits.append([i,(i+len(target))])
        return hits'''
    
    def encrypt(self):
        if self.cipher == 'caesar':#----------------CAESAR
            encryptedText = ""
            for i in range(0,len(self.msg)):
                encryptedText += self.numToChr((self.chrToNum(self.msg[i]) + self.keys[0]) % 26)
            return encryptedText
        elif self.cipher == 'afine':#----------------AFINE
            return true
        elif self.cipher == 'viginere':#----------------VIGINERE
            return true
        elif self.cipher == 'rsa':#----------------RSA
            return true
        else:
            return 'Error: encrypt() does not support' + self.cipher
    def decryptd(self):
        #Has Decryption Key
        decryptedText = ""
        for i in range(0,len(self.msg)):
            decryptedText += self.numToChr((self.chrToNum(self.msg[i]) - self.keys[0]) % 26)
        return decryptedText       
    def decrypt(self):   
        if self.cipher == 'caesar':#----------------CAESAR
            if self.keys == []:
                #Not Have Decryption Key
                lowestVariance = 100000000000
                guessKey = 0
                msgStore = self.msg
                #set the starting key to zero
                self.keys.append(0)
                for i in range(0,26):
                    self.keys[0] = i
                    test = self.decryptd()
                    #so self.variance can be called on the 'test' decryption
                    self.msg = test
                    h = self.varianceAnalysis()
                    if h < float(lowestVariance):
                        #guess key is set to the key that yeilds the lowest variance
                        lowestVariance = h
                        guessKey = i
                # set the class vars for decryption by self.decryptd()
                self.keys[0] = guessKey
                self.msg = msgStore
                return self.decryptd()
            else:
                #DO has key decryption code
                return self.decryptd()
            
        elif self.cipher == 'afine':#----------------AFINE
            return true
        elif self.cipher == 'viginere':#----------------VIGINERE
            return true
        elif self.cipher == 'rsa':#----------------RSA
            return true 
        else:
            return 'Error: decrypt() does not support ' + self.cipher
    
    # END OF CLASS cryptoMsg
     
    ''' 
    def keysValidate(self): #NEEDS WORK !!!!!!!!!!!!
        if (type(self.keys) == list):
            if len(self.keys[1]) > 1:
                return false 'Error: keys[1] is not a single letter or number
            elif 
        else:
            return false, 'Error: keys is not a list'
    '''   
cryptoMsgs = [0] # this is where we store the previous inialized objects used to decrypt/encrypt etc......
totalMsgs = 0
currentTask = "No current task"

import os as os
def clear():
    #clear the screen easily
    os.system('cls')
    
def start():
    def printTasks():
        print("~~~~~~~~~ Previous Tasks ~~~~~~~~~")
        print("N | type   | name")
        print("------------------")
        for  i in range(1,len(cryptoMsgs)):
            print( str(i) + " | " + str(cryptoMsgs[i].cipher) + " | "+ str(cryptoMsgs[i].name))
        print("~~~~~~~~~ No More Tasks ~~~~~~~~~")
    def graphFrequency(task):
        for i in range(0,len(task.frequencyAnalysis())):
            print(task.numToChr(i) + " : " )
            line = "/" * int(task.frequencyAnalysis()[i] *100) 
            print(line)
            print("(" + str((task.frequencyAnalysis()[i]*100)) + "%)")
    def createTask():
        n = input("Type the Name of this new Task: ")
        t = input("Type a cipher type (ex. caesar): ")
        k = input("Type a number as the key for the cipher: ")
        m = input("Type in your message: ")
        k = int(k)
        t = t.lower()
        m = m.lower()
        cryptoMsgs.append( cryptoMsg([k], m, t, n))
        global totalMsgs
        totalMsgs += 1
        
    def openTask(stn, task):#### make this two seperate functions one that handles the if d/e input then shows d/e task.encrypt() , task. decrypt()
        global currentTask,totalMsgs
        if stn.lower == 'd':
            currentTask = task
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Decrypted Text: " + task.decrypt())
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Key: " + str(task.keys[0]))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Variance Analysis : " )
            print(task.varianceAnalysis())
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            currentTask = task
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Encrypted Text: " + task.encrypt())
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Key: " + str(task.keys[0]))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Variance Analysis : " )
            print(task.varianceAnalysis())
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        
    
    '''
           This is where the user interface should go here based upon the totalMsg we will creat a new instance of the
           class cryptoMsg and save it in cryptoMsgs[totalMsgs] then add one to totalMsg. the user interface will ask the user a series of questions
           0.) Greet user and ask if they would like create a new message or view a previous one 1.) cipher type 2.) encrypt or decrypt 3.) the message
           4.)  the key(leave blank if unknown --> behind the scenes initalize the object and save it then based upon user choice
           give the user the ability to view the previous messages then pick one --> should display listindex[selection].name as what is presented
           should also provide a space for the tools defined in the program. as well as when displaying frequency graph  it /// /// //////// etc........
           make sure that the user can type. inputs should watch for key int errors or key is a char error!!!!!!!!!!! 
    '''
   # incase the person forgets quotations
    p = 'p'
    n = 'n'
    d = 'd'
    e = 'e'
    caesar = 'caesar'
    clear()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("            Cryptography Tools            ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if len(cryptoMsgs) == 1:
        print("There are no previous mesages")
    task = input("Type  p to view previous tasks or n to make a new one: ")
    task = str(task.lower())
    if task == 'p':
        clear()
        printTasks()
        select = input("Type the number of the task open or 'e' to exit: ")
        if select  == 'e':
            pass
        else:
            select = int(select)
            t = input("Type d or e to encrypt or decrypt: ")
            t.lower()
            clear()
            openTask(t,cryptoMsgs[select])
            print(" type start() to begin")
    elif task == 'n':
        clear()
        createTask()
        t = input("Type d or e to encrypt or decrypt: ")
        t.lower()
        openTask(t,cryptoMsgs[totalMsgs])
        print(" type start() to begin")
        
        
        

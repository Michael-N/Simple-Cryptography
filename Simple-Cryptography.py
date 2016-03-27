'''
    
    # END OF CLASS cryptoMsg
     
     
    def keysValidate(self): #NEEDS WORK !!!!!!!!!!!!
        if (type(self.keys) == list):
            if len(self.keys[1]) > 1:
                return false 'Error: keys[1] is not a single letter or number
            elif 
        else:
            return false, 'Error: keys is not a list'
       
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
        
        
    
           This is where the user interface should go here based upon the totalMsg we will creat a new instance of the
           class cryptoMsg and save it in cryptoMsgs[totalMsgs] then add one to totalMsg. the user interface will ask the user a series of questions
           0.) Greet user and ask if they would like create a new message or view a previous one 1.) cipher type 2.) encrypt or decrypt 3.) the message
           4.)  the key(leave blank if unknown --> behind the scenes initalize the object and save it then based upon user choice
           give the user the ability to view the previous messages then pick one --> should display listindex[selection].name as what is presented
           should also provide a space for the tools defined in the program. as well as when displaying frequency graph  it /// /// //////// etc........
           make sure that the user can type. inputs should watch for key int errors or key is a char error!!!!!!!!!!! 
    
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
        '''
class cryptoTask(object):

    def __init__(self,keys,msg,cipherType,taskName):
        #initalize class vars
        self.keys = keys #keys is a list
        self.msg = msg
        self.cipherType = cipherType
        self.taskName = taskName
           
    def numToChar(self,num):
        # convert 0-25 to coresponding lowercase Ascii
        if type(num) == int:
            char = chr(num + 97)
            char = str(char)
            return char
        else:
            print("Error: " + str(num) + " is not a valid input")
            return false
         
    def charToNum(self,char):
        # convert lowercase letter to ascii then convert to 0-25
        if type(char) == str:
            char = char.lower()
            num = ord(char)-97
            return num
        else:
            print( "Error: " + str(char) + " is not a valid input")
            return false
        
    def msgFrequency(self):
        # checks letter frequency of the msg
        frequency = [0]*26
        numLettersInMsg = len(self.msg)
        for letter in self.msg:
            if 97 <= ord(letter) <= 122:
                frequency[self.charToNum(letter)] += 1
            else:
                pass
        for dataPointIndex in range(0,len(frequency)):
            frequency[dataPointIndex] = float(frequency[dataPointIndex] / numLettersInMsg)
        return frequency
            
    
    def msgVariance(self):
        # gets the variance of msg 
        variance = 0
        msgFrequency = self.msgFrequency()
        englishFrequency = [0.0867,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02361,0.00150,0.01974,0.00074]
        for indexAlpha in range(0,26):
            variance += abs(msgFrequency[indexAlpha]-englishFrequency[indexAlpha])
        return variance
    def msgEncrypt(self):
        self.cipherType = str(self.cipherType.lower())

        #add code to validate the keys
        if self.cipherType == 'caesar':
            self.keys[0] = int(self.keys[0])
            encryptedText = ''
            for letter in self.msg:
                letter = letter.lower()
                if 97 <= ord(letter) <= 122:
                    encryptedText += self.numToChar((self.charToNum(letter) + self.keys[0])%26)
                else:
                    pass
            return encryptedText
        else:
            print("Error: " + self.cipherType + " is not a valid input")
            return false
        
    def msgDecrypt(self):
        self.cipherType = str(self.cipherType.lower())
        
        if self.cipherType == 'caesar':
            if self.keys == []:
                #NO KEY DECRYPTION
                storeMsg = self.msg
                lowestVariance = 100000000000000000000
                corespondingKey = 0
                self.keys.append(0)
                for i in range(0,26):
                    self.keys[0] = i
                    self.msg = storeMsg
                    decryptedTextAlpha = self.msgDecrypt()
                    self.msg = decryptedTextAlpha
                    if self.msgVariance() <= lowestVariance:
                        lowestVariance = self.msgVariance()
                        corespondingKey = self.keys[0]
                        continue
                    else:
                        pass
                self.msg = storeMsg
                self.keys[0] = corespondingKey
                return self.msgDecrypt()
                    
            else:
                #KEY DECRYPTION
                decryptedTextBeta = ''
                for letter in self.msg:
                    letter = letter.lower()
                    if 97 <= ord(letter) <= 122:
                        decryptedTextBeta += self.numToChar(abs((self.charToNum(letter) - self.keys[0]) % 26))
                    else:
                        pass
                return decryptedTextBeta
        else:
            print("Error: " + self.cipherType + " is not a valid input")
            return false

#USER INTERFACE STUFF

#STORED CRYPTO TASKS
storedTasks = [0]
totalTasks = 0
#INITALIZED VARS
import os as os
#INTERFACE
def start():
    
    def clear():
        #for Windows
        os.system('cls')
        
    def pickTask():# PREVIOUS TASKS OR SELECTING A TASK
        global storedTasks
        global totalTasks
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("PICK A TASK")
        print(" Type the index number of the task you wish to select or exit to exit")
        #print(" (be sure to type it withine quotations '')")
        if totalTasks == 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(" There are no saved tasks please type exit and go make one")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            return 'exit'
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Index | Task Name | Message Preview")
            print("-----------------------------------")
            for i in range(1,len(storedTasks)):
                #THIS makes sure that the table of results turns out well formated????????????????
                if len(str(i))> 6:
                    index = " MAX  "
                else:
                    index = str(i) + ( " " * (5-len(str(i))))
                if len(storedTasks[i].taskName) > 12: #ERROR??????? TypeError: string indices must be integers
                    name = str(storedTasks[i].taskName[0,12])
                else:
                    name = str(storedTasks[i].taskName)
                    name +=  " " * (11-len(name))
                if len(storedTasks[i].msg) > 15:
                      msgPreview = storedTasks[i].msg[0,16]
                else:
                    msgPreview = storedTasks[i].msg
                print( index + "|" + name + "|" + msgPreview)
            print("No more Messages")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            userAnswer = input("Index: ")
            if str(userAnswer).lower() == 'exit':
                print("Exiting...")
                return ['exit']
            else:
                print("Task " + str(userAnswer) + " selected" )    
                return [storedTasks[int(userAnswer)], int(userAnswer)]
                
    def showTask(task): 
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("DISPLAYED TASK")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print( str(task.taskName))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Task Message: " + str(task.msg))
        print("Task Key: " + str(task.keys[0]))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Task Message Frequency Analysis: ")
        msgFreq = ''
        for index in range(0,26):
            msgFreq += task.numToChar(index) +  " " + str(task.msgFrequency()[index]) + ", "   
        print(msgFreq)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Task Message Variance: " + str(task.msgVariance()))

    def showEncrypted(task):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Encrypted the Message as: " + str(task.msgEncrypt()))
        start()
        
    def showDecrypted(task):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Decrypted the Message as: " + str(task.msgDecrypt()))
        start()
        
    def createTask():
        global storedTasks
        global totalTasks
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("CREATE A NEW TASK")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("follow the onscreen instructions then hit enter to proceed")
        #print(" (be sure to type your response withine quotations '')")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        name = str(input("Type the name for the new task: "))
        ciphType = str(input("Type the cipher type to be used (ex. caesar): "))
        message = str(input("Type your message: "))
        selectedKey = [0]                                                       #ERRORS HERE? line 326, in createTask ValueError: invalid literal for int() with base 10: ''
    selectedKey = [int(validatedKey[0])]
ValueError: invalid literal for int() with base 10: ''
        selectedKey[0] = input("Type the key(Type nk for no key decryption): ")
        validatedKey = selectedKey
        if selectedKey[0] == 'nk':
            selectedKey = []
        else:
            selectedKey = [int(validatedKey[0])]
        storedTasks.append(cryptoTask(selectedKey,message,ciphType,name))
        totalTasks += 1
        print("Task Sucessfully Created")
        start()
        return storedTasks[totalTasks]
        
    def editTask(task,index):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Edit TASK")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Follow the onscreen instructions then hit enter to proceed")
        #print(" (be sure to type your response withine quotations '' ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("If you wish the task setting to remain unchanged, leave blank")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Current task name: " + str(task.taskName))
        name = str(input("Rename the task as: "))
        print("Current Cipher Type: " + str(task.cipherType))
        ciphType = str(input("Redefine the cipher type (ex. caesar): "))
        print("Current Message: " + str(task.msg))
        message = str(input("Redefine your message: "))
        selectedKey = [0]
        print("Current Key: " + str(task.keys[0]))
        selectedKey[0] = input("Redefine the key(Type nk for no key decryption): ")
        validatedKey = [0]
        validatedKey[0] = selectedKey[0]
        if selectedKey == []:
            selectedKey = task.keys
        elif selectedKey[0] == 'nk':
            selectedKey = []
        else:
            selectedKey[0] = validatedKey[0]
        if ciphType == '':
            ciphType = task.cipherType
        if message == '':
            message = task.msg
        storedTasks[index] = cryptoTask(selectedKey,message,ciphType,name)
        print("Task Sucessfully Edited")
        start()
        
    def initial():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~                        Cryptography Interface                         ~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        choiceAlpha = str(input("Type p to view/edit previous tasks or n to create a new one: ")).lower()
        if choiceAlpha == 'p':
            task = pickTask()
            if task[0] == 'exit':
                return
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                choiceBeta = str(input("Type v to view the task or e to edit the task: ")).lower()
                if choiceBeta == 'v':
                    n = showTask(task[0])
                    if n== 'exit':
                        return
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    choiceGamma = str(input("Type e to encrypt or d to decrypt the task message: "))
                    if choiceGamma == 'e':
                        showEncrypted(task[0])
                    elif choiceGamma  == 'd':
                        showDecrypted(task[0])
                    else:
                        print("Invalid choice: " + choiceGamma + " , is not d or e")
                        print("Cryptography Interface will now exit, type start() to open the interface") 
                    return
                elif choiceBeta == 'e':
                    editTask(task[0],task[1])
                    return
                else:
                    print("Invalid choice: " + choiceBeta + " , is not v or e")
                    print("Cryptography Interface will now exit, type start() to open the interface")
                    return
        elif choiceAlpha == 'n':
            createTask()
            return 
        else:
            print("Invalid choice: " + choiceAlpha + " , is not p or n")
            print("Cryptography Interface will now exit, type start() to open the interface")
            return
    initial()


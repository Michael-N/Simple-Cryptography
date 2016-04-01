class settings(object):

    def __init__(self):
        self.__case  = 'lower' # or 'upper' or 'both'
        self.__removeChars = '' #remove these before doing anything
        self.__replaceRemoved = ''

    def setCase(self,arg):
        if type(arg) == str:
            arg = arg.lower()
            if (arg == 'lower') | (arg == 'upper') | (arg == 'both'):
                self.__case = arg
                return true
            else:
                return false
        else:
            return false

    def setRemoveChars(self,arg):
        if type(arg) == (str | list):
            if type(arg) == str:
                self.__removeChars = arg
                return true
            else:
                for letter in arg:
                    self.__removeChars += letter
                return true
        else:
            return false

    def charToNum(self,arg):
        if type(arg) == chr:
            for letter in self.__removeChars:
                if arg == letter:
                    return false
                else:
                    continue
            if self.__case == 'lower':
                arg = arg.lower()
                return ord(arg) - 97
            elif self.__case == 'upper':
                arg = arg.upper()
                return ord(arg) - 65
            else:
                return ord(arg)
        else:
            return false

    def numToChar(self,arg):
        if type(arg) == int:
            if self.__case == 'lower':
                return chr(arg + 97)
            elif self.__case == 'upper':
                return chr(arg + 65)
        else:
            return false
class caesar(settings):
    def __init__(self):
        self.__key = null
        self.__msg = ''

    def setKey(self,arg):
        if type(arg) == int:
            self.__key = arg
            return true
        elif type(arg) == str:
            arg = arg.lower()
            self.__key = ord(arg) - 97
            return true
        else:
            return false


    def setMsg(self,arg):
        if type(arg) == str:
            for letterAlpha in arg:
                for letterBeta in self.__removeChars:
                    if letterAlpha == letterBeta:
                        continue
                    else:
                        self.__msg += letter
            if self.__case == 'lower':
                self.__msg = self.__msg.lower()
            elif self.__case == 'upper':
                self.__msg = self.__msg.upper()
            else:
                self.__msg = self.__msg
            return true
        else:
            return false

    def encryptMsg(self):
        encryptedMsg = ''
        msgDataList = []
        for indexAlpha in range(0,len(self.__msg)):
            msgDataList[indexAlpha] = self.charToNum(self.__msg[indexAlpha])
        for indexBeta in range(0,len(msgDataList)):
            if msgDataList[indexBeta] == false:
                pass
            elif 0 <= msgDataList[indexBeta] <=25:
                msgDataList[indexBeta] = numToChar((msgDataList[indexBeta] + self.__key) % 26)
            elif msgDataList[indexBeta] > 25:
                if 65 <= msgDataList[indexBeta] <=90:
                    originalCase = self.__case
                    self.setCase('upper')
                    msgDataList[indexBeta] = numToChar(((msgDataList[indexBeta]-65) + self.__key)% 26)
                    self.setCase(originalCase)
                else:
                    originalCase = self.__case
                    self.setCase('lower')
                    msgDataList[indexBeta] = numToChar(((msgDataList[indexBeta]-97) + self.__key)% 26)
                    self.setCase(originalCase)
        for item in msgDataList:
            if type(item) == bool:
                pass
            else:
                encryptedMsg += item
        return encryptedMsg

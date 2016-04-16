class settings(object):
    #MAKE SURE THIS INITALIZES ITSELFE AS  AS IT IS ACCESSED LATER ON in editSettings
errors = []
class error(exception):

    #BUILD AN ERROR HANDELING SYSTEM
allTasks = []
currentTask = None
allChoices = []
activeChoices = []
currentChoice = None
class choice(object):
    #CREATE A CHOICE AND MAKE IT AVILIABLE
    def __init__(self,name,callback,quickDes,description)
        self.name = name # choice name to display
        self.callback = callback # what should the selection off this choice do
        self.quickDes = quickDes # Quick description to display
        self.description = description # long description with Help
    def addChoice(self):
        allChoices.append(self)
    addChoice(self)
class task(object):
    def __init__(self,cipherType,msg,keys,name):
        self.cipherType = cipherType
        self.msg = msg
        self.keys = keys
        self.name = name
    def getDisplay(self):
        #Name 6 char, ciphertype 12 char, msg 10 char
        def cut(tmsg, endLength):
            fmsg = ''
            if len(tmsg) == endLength:
                fmsg = tmsg
            elif len(tmsg) < endLength:
                fmsg += tmsg
                spacesn = (endLength-len(tmsg)) * ' '
                fmsg +=  spacesn
            else:
                fmsg += tmsg[0,endLength]
            return str(fmsg)
        cmsg = cut(self.msg, 10)
        cname = cut(self.name, 6)
        ccipherType = cut(self.cipherType, 12)
        return ' | Name: ' + cname + ' | Cipher Type: ' + ccipherType + ' | Message Preview: ' + cmsg + ' |'


def showActiveChoices():
    #PRINT OUT THE CHOICES WITH THEIR INDEX
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please type the number of the choice you wish to select")
    for indexAlpha in range(0,len(activeChoices)):
        print( str(indexAlpha) + " " + str(activeChoices[indexAlpha].name) + " " + str(activeChoices[indexAlpha].quickDes))
    print('No more choices')

def askChoice():
    #THIS FUNCTION SHOULD LOOK AT THE CHOICES AND BASED UPON
    #THEIR INDEX ASK THE USER TO PICK ONE AND RUN THE CALLBACK
    answer = int(input("Choice number: "))
    if ((answer < 0 ) | (answer > len(activeChoices))):
        print('You did not type a valid number')
        askChoice()
    else:
        activeChoices[answer].callback()
def exit():
    #ASk the user if they want to exit to the main menue or exit the program
    #SHOULD EXIT AND GO TO THE MAIN MENU/ the start()
def createTask():
    #CREATE TASK ask the questions etc ask what t do next with showActiveChoices() and askChoice()
    #auto asign as the current task but append it first to allTasks
def deleteTask():
    #ASKS THE USER WHAT TASK THEY WANT TO  DELETE Then does that
    #etc ask what t do next with showActiveChoices() and askChoice()
def showAllTasks():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('All Tasks')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    global allTasks
    if allTasks = []:
        print('There are no Tasks, go and make one')
    else:
        for taskn in range(0,len(allTasks)):
            print(str(taskn)+ ' ' + allTasks[taskn].getDisplay())
        print('No more Tasks')
    #LOOKS AT THE CURRENT TASKS LIST AND DISPLAYS THEM WATCHES FOR EMPTY LIST
    #then ask what t do next with showActiveChoices() and askChoice()
    #CREATE A CHOICE THAT TAKES USER INPUT AND SETS GLOBAL TASK TO CURRENT TASK ONLY DO THIS UNLESS altasks != []
def previewTask():
    #Should not encrypt/decrypt but show keys,msg,name,cipherName
    #etc ask what t do next with showActiveChoices() and askChoice()
def validateString(arg):
    #general validation for strings/user input
def validateInt(arg):
    #general validation for number/ user input
def editTask():
    #should look to current task preview it then ask the user what they want to overide
def createTaskDisplay():
    #looks at the cipherName of the currentTask and asigns a standardized way to display it
    #give the option to tell it to graph the frequency Visually----->SEE graphFrequency!!!!!!!!!!!
    #SHOULD GIVE THE CURRENT TASK A .display() method-- that does this---> checks if already present
def displayTask():
    #should call the .display() on the currentTask and then showActiveChoices etc....
def graphFrequency():
    #get the frequency of the currentTask make it able to iterate through a list of lists frequency
    #THIS IS AN ADD ON TO CREATE TASK DISPLAY
def start():
    #THE main Menue that asks the user for initial input
def setActiveChoices(arg):
    #TAKES a list of number indexes that correspond to allChoices and appends to and OVERIDES to these choices in the activeChoices
    global activeChoices
    activeChoices = []
    for index in arg:
        activeChoices.append(allChoices[index])

def devMode():
    # TAKES DIRECT INPUT FROM USER NO VALIDATION!!!! FOR DEBUGGING
choice('Create Task', createTask,'Create a new Task', "This choice allows you to create a a new cryptography task that you can later access for your needs")
choice('Edit Task', editTask, 'Edit a Task', 'This allows you to preview then edit previous tasks' )
choice('Exit', exit, 'Exit', 'Exit to the main menu or exit the program')
choice('Preview the current Task', previewTask, "Shows information about the most recent Task","Shows information about the most recent Task")
choice('Show All Tasks',showAllTasks,'Look at previous tasks','Look at previous tasks')
choice('Main Menue',start,'Retrun to the main menue',' Will return you to the main menue')
choice('Dev',devMode,'---------',' For Debugging and devlopers, directly input code')
choice("Inport Task/s",inportTasks,'Load a task/s from a file','Load a task from a file with the exetnsion .task.py')
choice('Export Tasks/s', exportTasks,'Send a  task/s to a file','Name and save a task to a new File')
start()# START THE INTERFACE THE FIRST TIME

class segment :
    def __init__(self,name='',relatedProcess='none',number=-1,type='',startAddress=-1,size=0,endAddress=-1):
        self.__name = name
        self.__relatedProcess=relatedProcess
        self.__number=number #########
        self.__type=type
        self.__startAddress=startAddress
        self.__size=size
        self.__endAddress=endAddress
        self.__state='none'
    def setName(self,name):  #to be
        self.__name = name
    def getName(self):
        return self.__name
    def setStartingAddress(self,start):    #to be
        self.__startAddress=start
    def getStartingAddress(self):
        return  self.__startAddress
    def setSize(self,size):      #to be
        self.__size=size
    def getSize(self):
        return self.__size
    def setEndingAddress(self, end):  #to be deleted
        self.__endAddress = end
    def getEndingAddress(self):
        return self.__endAddress
    def setType(self,type):       #to be deleted
        self.__type = type
    def getType(self):
        return self.__type
    def setState(self,state):
        self.__state=state
    def getState(self):
        return self.__state
    def setRelatedProcess(self,name):
        self.__relatedProcess=name
    def getRelatedProcess(self):
        return self.__relatedProcess




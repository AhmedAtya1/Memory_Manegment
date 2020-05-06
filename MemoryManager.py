from Memory import memory
class memoryManager :
    def __init__(self,mem=memory()):
        self.__mem=mem
    def setSize(self,size):
        self.__mem.setSize(size)
    def printSize(self):
        print(self.__mem.getSize())




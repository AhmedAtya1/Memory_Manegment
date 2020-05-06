class memory :
    def __init__(self, memorySize=0, listOfHoles=[], listOfOldProcesses=[], listOfAllocatedProcesses=[], listOfWaitingProcesses=[], listOfAllPartitions=[], partitionsNo=0,holesNo=0,oldProcessesNo=0):
        self.__memorySize = memorySize
        self.__listOfHoles = listOfHoles
        self.__listOfOldProcesses = listOfOldProcesses
        self.__listOfAllocatedProcesses=listOfAllocatedProcesses
        self.__listOfWaitingProcesses=listOfWaitingProcesses
        self.__listOfAllPartitions = listOfAllPartitions
        self.__partitionsNo = partitionsNo
        self.__holesNo = holesNo
        self.__oldProcessesNo = oldProcessesNo  #may be taken from list size
    def setSize(self,size):
        self.__memorySize = size
    def getSize(self):
        return self.__memorySize


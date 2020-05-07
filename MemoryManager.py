from Segment import segment
import operator

class memoryManager:
    #memory class may be deleted
    def __init__(self, memorySize=0, listOfHoles=[], listOfOldProcesses=[], listOfAllocatedProcesses=[], listOfWaitingProcesses=[], listOfAllPartitions=[], partitionsNo=0,holesNo=0,oldProcessesNo=0,lastAddressFlag=0):
        self.__memorySize = memorySize
        self.__listOfHoles = listOfHoles
        self.__listOfOldProcesses = listOfOldProcesses
        self.__listOfAllocatedProcesses=listOfAllocatedProcesses
        self.__listOfWaitingProcesses=listOfWaitingProcesses
        self.__listOfAllPartitions = listOfAllPartitions
        self.__partitionsNo = partitionsNo
        self.__holesNo = holesNo
        self.__oldProcessesNo = oldProcessesNo  #may be taken from list size
        self.__lastAddressFlag=lastAddressFlag

    def setSize(self,size):
        self.__memorySize=size
    def addHole(self,startingAddress,size):
        newSeg=segment('hole','none',len(self.__listOfHoles),'hole',startingAddress,size,startingAddress+size-1)
        self.__listOfHoles.append(newSeg)
    def displayOldProcess(self,startingAddress,size):
        newSeg=segment('oldProcess'+str(self.__oldProcessesNo),'none',len(self.__listOfHoles),'oldProcess',startingAddress,size,startingAddress+size-1)
        self.__listOfAllPartitions.append(newSeg)
        self.__oldProcessesNo+=1
    def divideMem(self):
        self.__listOfHoles.sort(key=operator.attrgetter('_segment__startAddress'))
        for i in range(len(self.__listOfHoles)):
            if self.__listOfHoles[i].getStartingAddress()==self.__lastAddressFlag:
                self.__listOfAllPartitions.append(self.__listOfHoles[i])
                self.__lastAddressFlag=self.__listOfHoles[i].getEndingAddress()+1
            else:
                self.displayOldProcess(self.__lastAddressFlag,self.__listOfHoles[i].getStartingAddress()-self.__lastAddressFlag)
                self.__listOfAllPartitions.append(self.__listOfHoles[i])
                self.__lastAddressFlag=self.__listOfHoles[i].getEndingAddress()+1
        if self.__lastAddressFlag!=self.__memorySize:
            self.displayOldProcess(self.__lastAddressFlag,self.__memorySize - self.__lastAddressFlag)



    def print(self):
        self.printList(self.__listOfAllPartitions)
    def printList(self,list):
        for i in range(len(list)):
            print (str(i)+"    "+list[i].getName()+ "  From  " +str(list[i].getStartingAddress())+"   T0   "+str(list[i].getEndingAddress()))


    def printSize(self):
        print(self.__memorySize)
    def getList(self):
        return self.__listOfAllPartitions






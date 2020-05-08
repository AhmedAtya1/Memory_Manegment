from Segment import segment
from Process import process
import operator

class memoryManager:
    #memory class may be deleted
    def __init__(self):
        self.__memorySize = 0
        self.__listOfHoles = []
        self.__listOfOldProcesses = []
        self.__listOfAllProcesses=[]
        self.__listOfAllocatedProcesses=[]
        self.__listOfWaitingProcesses=[]
        self.__listOfAllPartitions = []
        self.__partitionsNo = 0
        self.__holesNo = 0
        self.__oldProcessesNo = 0  #may be taken from list size
        self.__lastAddressFlag=0
        self.__firstFitFlag=-1


    def setSize(self,size):
        self.__memorySize=size
    def addHole(self,startingAddress,size):
        newSeg=segment('Hole','none',len(self.__listOfHoles),'Hole',startingAddress,size,startingAddress+size)
        self.__listOfHoles.append(newSeg)
    def displayOldProcess(self,startingAddress,size):
        name='Old Process'+' '+str(self.__oldProcessesNo)
        newSeg=segment(name,name,len(self.__listOfHoles),'Old Process',startingAddress,size,startingAddress+size)
        self.__listOfAllPartitions.append(newSeg)
        self.__oldProcessesNo+=1
    def divideMem(self):
        if len(self.__listOfHoles)==0:
            self.displayOldProcess(self.__lastAddressFlag,self.__memorySize)
            return
        self.__listOfHoles.sort(key=operator.attrgetter('_segment__startAddress'))
        for i in range(len(self.__listOfHoles)):
            if self.__listOfHoles[i].getStartingAddress()==self.__lastAddressFlag:
                self.__listOfAllPartitions.append(self.__listOfHoles[i])
                self.__lastAddressFlag=self.__listOfHoles[i].getEndingAddress()
            else:
                self.displayOldProcess(self.__lastAddressFlag,self.__listOfHoles[i].getStartingAddress()-self.__lastAddressFlag)
                self.__listOfAllPartitions.append(self.__listOfHoles[i])
                self.__lastAddressFlag=self.__listOfHoles[i].getEndingAddress()
        if self.__lastAddressFlag!=self.__memorySize:
            self.displayOldProcess(self.__lastAddressFlag,self.__memorySize - self.__lastAddressFlag)




    def setSegmentsAndAlgorithms(self,numberOfSegments,Algorithm):
        if Algorithm=='firstFit':
            self.__firstFitFlag = 1
        else:
            self.__firstFitFlag = 0
        proc=process('P'+str(len(self.__listOfAllProcesses)),'waiting',numberOfSegments)
        self.__listOfAllProcesses.append(proc)
        #print(self.__firstFitFlag)
        #print(self.__listOfAllProcesses[-1].getName())

    def addSegment(self,name,size):
        currentProc=self.__listOfAllProcesses[-1]
        newName=self.__listOfAllProcesses[-1].getName()+' '+name
        newSeg=segment(newName,currentProc.getName(),currentProc.getNoOfAddedSegments(),'segment',-1,size,-1)
        currentProc.getListOfSegments().append(newSeg)
        noOfAddedSeg=currentProc.getNoOfAddedSegments()
        currentProc.setNoOfAddedSegments(noOfAddedSeg+1)
        #print(self.__listOfAllProcesses[-1].getListOfSegments()[-1].getName())


    def checkIfFitted(self):
        listOfHoleSizes=[]
        for i in range(len(self.__listOfHoles)):
            listOfHoleSizes.append(self.__listOfHoles[i].getSize())
            #print(listOfHoleSizes[i])
        currentListOfSeg = self.__listOfAllProcesses[-1].getListOfSegments()
        for i in range(len(currentListOfSeg)):
            for j in range(len(listOfHoleSizes)):
                if currentListOfSeg[i].getSize()<listOfHoleSizes[j]:
                    listOfHoleSizes[j]-=currentListOfSeg[i].getSize()
                    currentListOfSeg[i].setState('fit')
                    break
                elif currentListOfSeg[i].getSize()==listOfHoleSizes[j]:
                    del listOfHoleSizes[j]
                    currentListOfSeg[i].setState('fit')
                    break
            if currentListOfSeg[i].getState()!='fit':
                return False
        return True



    def addProcess(self):
        if  self.__firstFitFlag==1:
            self.__listOfHoles.sort(key=operator.attrgetter('_segment__startAddress'))
        else:
            self.__listOfHoles.sort(key=operator.attrgetter('_segment__startAddress'))
            self.__listOfHoles.sort(key=operator.attrgetter('_segment__size'))
            #print(self.__listOfHoles[0].getSize())
            #print(self.__listOfHoles[1].getSize())
            #print(self.__listOfHoles[2].getSize())

        if self.checkIfFitted()==False:
            #print(11)
            return False


        else:
            currentListOfSeg=self.__listOfAllProcesses[-1].getListOfSegments()
            for i in range(len(currentListOfSeg)):
                for j in range(len(self.__listOfHoles)):
                    if currentListOfSeg[i].getSize() < self.__listOfHoles[j].getSize():
                        currentListOfSeg[i].setStartingAddress(self.__listOfHoles[j].getStartingAddress())
                        currentListOfSeg[i].setEndingAddress(currentListOfSeg[i].getStartingAddress()+currentListOfSeg[i].getSize())
                        self.__listOfAllPartitions.append(currentListOfSeg[i])
                        self.__listOfHoles[j].setStartingAddress(currentListOfSeg[i].getEndingAddress())
                        self.__listOfHoles[j].setSize(self.__listOfHoles[j].getEndingAddress()-self.__listOfHoles[j].getStartingAddress())
                        break
                    elif currentListOfSeg[i].getSize() == self.__listOfHoles[j].getSize():
                        currentListOfSeg[i].setStartingAddress(self.__listOfHoles[j].getStartingAddress())
                        currentListOfSeg[i].setEndingAddress(self.__listOfHoles[j].getEndingAddress())
                        self.__listOfAllPartitions.append(currentListOfSeg[i])
                        self.removeSegment(self.__listOfHoles[j].getStartingAddress(),self.__listOfAllPartitions)
                        del self.__listOfHoles[j]
                        break
            self.__listOfAllPartitions.sort(key=operator.attrgetter('_segment__startAddress'))
            return True




    def removeSegment(self,start,list):
        for i in range(len(list)):
            if list[i].getStartingAddress()==start:
                del list[i]
                break
    def deAllocate(self,name):
        self.replaceWithHoles(name)
        self.mergeHoles()
        #self.printList(self.__listOfHoles)

    def replaceWithHoles(self,name):
        for i in range(len(self.__listOfAllPartitions)):
                if self.__listOfAllPartitions[i].getRelatedProcess()==name:
                    self.__listOfAllPartitions[i].setName('Hole')
                    self.__listOfAllPartitions[i].setRelatedProcess('none')
                    self.__listOfAllPartitions[i].setType('Hole')
                    self.__listOfHoles.append(self.__listOfAllPartitions[i])



    def mergeHoles(self):
        i=0
        while len(self.__listOfAllPartitions) > 1:


            if self.__listOfAllPartitions[i].getName()=='Hole':
                while self.__listOfAllPartitions[i+1].getName()=='Hole':
                    start=self.__listOfAllPartitions[i].getStartingAddress()
                    end=self.__listOfAllPartitions[i+1].getEndingAddress()
                    size=self.__listOfAllPartitions[i].getSize()+self.__listOfAllPartitions[i+1].getSize()
                    newHole=segment('Hole','none',-1,'Hole',start,size,end)
                    secondStart=self.__listOfAllPartitions[i+1].getStartingAddress()
                    self.removeSegment(start,self.__listOfAllPartitions)
                    self.removeSegment(start,self.__listOfHoles)
                    self.removeSegment(secondStart, self.__listOfAllPartitions)
                    self.removeSegment(secondStart, self.__listOfHoles)
                    self.__listOfHoles.append(newHole)
                    self.__listOfAllPartitions.append(newHole)
                    self.__listOfAllPartitions.sort(key=operator.attrgetter('_segment__startAddress'))
                    #self.print()

                    if (i+1)==len(self.__listOfAllPartitions):
                        break
            i+=1
            if i == (len(self.__listOfAllPartitions) - 1):
                    break

    def addBinding(self):
        return self.addProcess()

    def getTableData(self,name):
        for i in range(len(self.__listOfAllProcesses)):
            if self.__listOfAllProcesses[i].getName()==name:
                list=self.__listOfAllProcesses[i].getListOfSegments()
                return list



    def print(self):
        self.printList(self.__listOfAllPartitions)
    def printList(self,list):
        for i in range(len(list)):
            print (str(i)+"    "+list[i].getName()+ "  From  " +str(list[i].getStartingAddress())+"   T0   "+str(list[i].getEndingAddress()))


    def printSize(self):
        print(self.__memorySize)
    def getListOfAllPartitions(self):
        return self.__listOfAllPartitions






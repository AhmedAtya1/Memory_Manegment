from Partition import partition
from Process import process
import operator

class memoryManager:
    def __init__(self):
        self.__memorySize = 0
        self.__listOfHoles = []
        self.__listOfAllProcesses=[]
        self.__listOfAllPartitions = []
        self.__oldProcessesNo = 0
        self.__lastAddressFlag=0
        self.__firstFitFlag=-1


    def setSize(self,size):
        self.__memorySize=size
    def addHole(self,startingAddress,size):
        newSeg=partition('Hole', 'none', len(self.__listOfHoles), 'Hole', startingAddress, size, startingAddress + size)
        self.__listOfHoles.append(newSeg)
    def displayOldProcess(self,startingAddress,size):
        name='Old Process'+' '+str(self.__oldProcessesNo)
        newSeg=partition(name, name, len(self.__listOfHoles), 'Old Process', startingAddress, size, startingAddress + size)
        self.__listOfAllPartitions.append(newSeg)
        self.__oldProcessesNo+=1
    def divideMem(self):
        if len(self.__listOfHoles)==0:
            self.displayOldProcess(self.__lastAddressFlag,self.__memorySize)
            return
        self.__listOfHoles.sort(key=operator.attrgetter('_partition__startAddress'))
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

    def addSegment(self,name,size):
        currentProc=self.__listOfAllProcesses[-1]
        newName=self.__listOfAllProcesses[-1].getName()+' '+name
        newSeg=partition(newName, currentProc.getName(), currentProc.getNoOfAddedSegments(), 'segment', -1, size, -1)
        currentProc.getListOfSegments().append(newSeg)
        noOfAddedSeg=currentProc.getNoOfAddedSegments()
        currentProc.setNoOfAddedSegments(noOfAddedSeg+1)


    def checkIfFitted(self):
        listOfHoleSizes=[]
        for i in range(len(self.__listOfHoles)):
            listOfHoleSizes.append(self.__listOfHoles[i].getSize())
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
            self.__listOfHoles.sort(key=operator.attrgetter('_partition__startAddress'))
        else:
            self.__listOfHoles.sort(key=operator.attrgetter('_partition__startAddress'))
            self.__listOfHoles.sort(key=operator.attrgetter('_partition__size'))

        if self.checkIfFitted()==False:
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
            self.__listOfAllPartitions.sort(key=operator.attrgetter('_partition__startAddress'))
            return True




    def removeSegment(self,start,list):
        for i in range(len(list)):
            if list[i].getStartingAddress()==start:
                del list[i]
                break
    def deAllocate(self,name):
        self.replaceWithHoles(name)
        self.mergeHoles()

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
                while self.__listOfAllPartitions[i+1].getName()=='Hole' :
                    start=self.__listOfAllPartitions[i].getStartingAddress()
                    end=self.__listOfAllPartitions[i+1].getEndingAddress()
                    size=self.__listOfAllPartitions[i].getSize()+self.__listOfAllPartitions[i+1].getSize()
                    newHole=partition('Hole', 'none', -1, 'Hole', start, size, end)
                    secondStart=self.__listOfAllPartitions[i+1].getStartingAddress()
                    self.removeSegment(start,self.__listOfAllPartitions)
                    self.removeSegment(start,self.__listOfHoles)
                    self.removeSegment(secondStart, self.__listOfAllPartitions)
                    self.removeSegment(secondStart, self.__listOfHoles)
                    self.__listOfHoles.append(newHole)
                    self.__listOfAllPartitions.append(newHole)
                    self.__listOfAllPartitions.sort(key=operator.attrgetter('_partition__startAddress'))

                    a=i+1
                    if a==len(self.__listOfAllPartitions):
                        break

            i+=1
            if i >= (len(self.__listOfAllPartitions))-1:
                    break

    def addBinding(self):
        return self.addProcess()

    def getTableData(self,name):
        for i in range(len(self.__listOfAllProcesses)):
            if self.__listOfAllProcesses[i].getName()==name:
                list=self.__listOfAllProcesses[i].getListOfSegments()
                if list[0].getName()!='Hole':
                    return list
        return []



    def print(self):
        self.printList(self.__listOfAllPartitions)
    def printList(self,list):
        for i in range(len(list)):
            print (str(i)+"    "+list[i].getName()+ "  From  " +str(list[i].getStartingAddress())+"   T0   "+str(list[i].getEndingAddress()))


    def printSize(self):
        print(self.__memorySize)
    def getListOfAllPartitions(self):
        return self.__listOfAllPartitions






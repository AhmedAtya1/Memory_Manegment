from MemoryManager import memoryManager
A=memoryManager()
A.setSize(100.5)
A.addHole(0,0.5)
A.addHole(10,10.5)
A.addHole(50,5.5)
A.addHole(90,9.5)
A.divideMem()
A.setSegmentsAndAlgorithms(1,'bestFit')
A.addSegment('code',5.5)
print(A.addProcess())
A.deAllocate('Old Process 1')
A.setSegmentsAndAlgorithms(1,'firstFit')
A.addSegment('code',50)
print(A.addProcess())
A.deAllocate('Old Process 2')
print(A.addBinding())
A.deAllocate('Old Process 3')












#A.setSegmentsAndAlgorithms(1,'firstFit')
#A.addSegment('code',80)
#print(A.addProcess())
#A.deAllocate('Old Process 0')
#print(A.addBinding())
#A.deAllocate('Old Process 2')
#print(A.addBinding())
#A.deAllocate('Old Process 1')
#print(A.addBinding())





#A.deAllocate('Old Process 1')




#A.printList(A.getTableData('P0'))

#A.addHole(75,7)
#A.addHole(0,7)
#A.addHole(40,7)
#A.divideMem()
#A.setSegmentsAndAlgorithms(2,'firstFit')
#A.addSegment('code',4)
#A.addSegment('main',7)
#print(A.addProcess())
#A.setSegmentsAndAlgorithms(2,'bestFit')
#A.addSegment('code',4)
#A.addSegment('main',7)
#print(A.addProcess())
#A.deAllocate('p0')
#A.addBinding()
#A.deAllocate('p1')
#A.setSegmentsAndAlgorithms(2,'bestFit')
#A.addSegment('code',4)
#A.addSegment('main',7)
#A.addProcess()
#A.deAllocate('oldProcess0')

A.print()




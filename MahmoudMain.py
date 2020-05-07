from MemoryManager import memoryManager
A=memoryManager()
A.setSize(100)
A.addHole(75,7)
A.addHole(0,7)
A.addHole(40,20)
A.divideMem()
A.setSegmentsAndAlgorithms(2,'firstFit')
A.addSegment('code',4)
A.addSegment('main',7)
A.addProcess()
A.setSegmentsAndAlgorithms(2,'bestFit')
A.addSegment('code',4)
A.addSegment('main',7)
A.addProcess()
A.deAllocate('p0')
A.deAllocate('p1')
A.setSegmentsAndAlgorithms(2,'bestFit')
A.addSegment('code',4)
A.addSegment('main',7)
A.addProcess()
A.deAllocate('oldProcess0')

A.print()




class process :
    def __init__(self,name= '',state='',noOfSegments=0):
        self.__name = name
        self.__listOfSegments=[]
        self.__state=state
        self.__noOfsegments=noOfSegments
        self.__noOfAddedsegments=0


    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    def setNoOfsegments(self,segments):
        self.__noOfsegments=segments
    def getNoOfsegments(self):
        return self.__noOfsegments
    def setNoOfAddedSegments(self,segments):
        self.__noOfAddedsegments=segments
    def getNoOfAddedSegments(self):
        return self.__noOfAddedsegments
    def getListOfSegments(self):
        return self.__listOfSegments


class segment :
    def __init__(self,name='',relatedProcess='',number=0,type='',startAddress=-1,size=0,endAddress=-1):
        self.__name = name
        self.__relatedProcess=relatedProcess
        self.__number=number
        self.__type=type
        self.__startAddress=startAddress
        self.__size=size
        self.__endAddress=endAddress


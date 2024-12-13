from abc import ABC 

class GeometricObject(ABC):
    def __init__(self):
        self.__lineColor = 'black'  
        self.__lineWidth = 1  
        self.__visible = False  
        self.__myCanvas = None  

    def setColor(self, color):  
        self.__lineColor = color
        if self.__visible:  
            self.__myCanvas.drawAll()

    def setWidth(self, width):  
        self.__lineWidth = width
        if self.__visible:  
            self.__myCanvas.drawAll()

    def getColor(self):
        return self.__lineColor  

    def getWidth(self):
        return self.__lineWidth  

    def _draw(self, turtle):  
        pass

    def setVisible(self, vFlag):
        self.__visible = vFlag  

    def getVisible(self):
        return self.__visible  

    def setCanvas(self, theCanvas):
        self.__myCanvas = theCanvas  

    def getCanvas(self):
        return self.__myCanvas  
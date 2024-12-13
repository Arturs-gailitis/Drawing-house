from GeometricObject import GeometricObject  

class Line(GeometricObject):
    def __init__(self, p1, p2):
        super().__init__()  
        self.__p1 = p1  
        self.__p2 = p2  

    def getP1(self):
        return self.__p1  

    def getP2(self):
        return self.__p2  

    def _draw(self, turtle):
        turtle.color(self.getColor())  
        turtle.width(self.getWidth())  
        turtle.up()  
        turtle.goto(self.__p1.getCoord())  
        turtle.down()  
        turtle.goto(self.__p2.getCoord())  



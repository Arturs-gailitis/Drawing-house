from GeometricObject import GeometricObject  

class Point(GeometricObject):
    def __init__(self, x, y):
        super().__init__()  
        self.__coordinates = (x, y) # Storing the x and y coordinates as a tuple.

    # Returns the coordinates of the point as a tuple (x, y).
    def getCoord(self):
        return self.__coordinates  

    # Returns the x-coordinate of the point.
    def getX(self):
        return self.__coordinates[0] 

    # Returns the y-coordinate of the point.
    def getY(self):
        return self.__coordinates[1]  

    def _draw(self, turtle):
        turtle.goto(self.__coordinates) # Moves the turtle to the point's coordinates.
        turtle.dot(self.getWidth(), self.getColor()) 
from GeometricObject import GeometricObject

# Circle class, subclass of GeometricObject
class Circle(GeometricObject):

    def __init__(self, pointx, pointy, radiuss):
        super().__init__()

        self.__pointx = pointx # x-coordinate of the circle's center
        self.__pointy = pointy # y-coordinate of the circle's center
        self.__radiuss = radiuss # Radius of the circle

    def get_pointx(self):

        return self.__pointx
    
    def get_pointy(self):

        return self.__pointy
    
    def get_radiuss(self):

        return self.__radiuss
    
    def _draw(self, turtle):

        # Draws the circle using the turtle object

        turtle.color(self.getColor())

        turtle.width(self.getWidth())

        turtle.begin_fill()

        turtle.up()

        turtle.goto(self.__pointx, self.__pointy) # Move turtle to the circle's center

        turtle.down()

        turtle.circle(self.__radiuss) # Draw the circle with specified radius

        turtle.end_fill()
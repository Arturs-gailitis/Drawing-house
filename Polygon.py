from GeometricObject import GeometricObject

class Polygon(GeometricObject):

    # Constructor for the Polygon class that accepts a list of points (vertices).
    def __init__(self, points):
        super().__init__()

        self.__points = points # Storing the points (vertices) of the polygon.
    
    # Getter method to return the list of points of the polygon.
    def get_points(self):
        
        return self.__points 

    # Method to draw the polygon using the turtle module
    def _draw(self, turtle):

        turtle.color(self.getColor()) # Setting the color of the turtle based on the polygon's color.

        turtle.width(self.getWidth()) # Setting the line width for drawing the polygon.

        turtle.begin_fill() # Starts filling the polygon with the set color.

        turtle.up()

        turtle.goto(self.__points[0]) # Moves the turtle to the first point of the polygon.

        turtle.down()

        # Loop to draw lines connecting the points of the polygon.
        for point in self.__points[1:]:

            turtle.goto(point)
        
        turtle.goto(self.__points[0]) # Closing the polygon by drawing a line back to the first point.

        turtle.end_fill() # Fills the polygon with the specified color.
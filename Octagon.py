from Polygon import Polygon

class Octagon(Polygon):

    # Initializes an Octagon object with its center at (pointx, pointy) and specified height and width.
    def __init__(self, pointx, pointy, height, width):

        # Calling the parent class constructor with the calculated points of the octagon.
        super().__init__(self._setup_points(pointx, pointy, height, width))
    
    # Helper method to calculate the vertices of the octagon.
    def _setup_points(self, pointx, pointy, height, width):

        # Defining each point in the octagon, starting at the top center and moving clockwise.
        point1 = (pointx, pointy)

        point2 = (pointx + width, pointy - height)

        point3 = (point2[0], point2[1] - height)

        point4 = (point2[0] - width, point3[1] - height)

        point5 = (point4[0] - width, point4[1])

        point6 = (point5[0] - width, point4[1] + height)

        point7 = (point6[0], point6[1] + height)

        point8 = (pointx - width, pointy)

        # Returning a list of points to represent the vertices of the octagon.
        return [point1, point2, point3, point4, point5, point6, point7, point8]

        

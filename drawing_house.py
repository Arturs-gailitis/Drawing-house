from Rectangle import Rectangle
from Triangle import Triangle
from Octagon import Octagon
from Canvas import Canvas
from Line import Line 
from Point import Point

myCanvas = Canvas(600, 500)

# Function to draw a house using various shapes
def drawing_house():
    
    # Drawing the body of the house
    house_body = Rectangle(-50, -50, 100, 200)
    house_body.setColor('orange')
    myCanvas.draw(house_body)

    # Drawing the roof triangles
    roof1 = Triangle(50, 25, 75, 100)   
    roof1.setColor('red')
    myCanvas.draw(roof1)

    roof2 = Triangle(50, 25, 75, -100)   
    roof2.setColor('red')
    myCanvas.draw(roof2)

    # Drawing a small window on the roof
    roofwindow = Octagon(55, 0, 10, 10)
    roofwindow.setColor('white')
    myCanvas.draw(roofwindow)

    # Adding window lines
    windowline1 = Line(Point(50, 0), Point(50, -30))
    windowline1.setWidth(2)
    windowline1.setColor('black')
    myCanvas.draw(windowline1)

    windowline2 = Line(Point(35, -16), Point(65, -16)) 
    windowline2.setWidth(2)
    windowline1.setColor('black')
    myCanvas.draw(windowline2)

    # Drawing the door
    door = Rectangle(40, -110, 40, 20)
    door.setColor('grey')
    myCanvas.draw(door)

    # Adding a door knob
    door_noob = Point(55, -130)
    door_noob.setColor('black')
    door_noob.setWidth(4)
    myCanvas.draw(door_noob)

    # Adding windows on the house
    window1 = Rectangle(75, -75, 25, 25)
    window1.setColor('white')
    myCanvas.draw(window1)

    window2 = Rectangle(5, -75, 25, 25)
    window2.setColor('white')
    myCanvas.draw(window2)

    # Adding window lines for the left and right windows
    windowline3 = Line(Point(87, -75), Point(87, -100))
    windowline3.setWidth(2)
    windowline3.setColor('black')
    myCanvas.draw(windowline3)

    windowline4 = Line(Point(75, -88), Point(100, -88)) 
    windowline4.setWidth(2)
    windowline4.setColor('black')
    myCanvas.draw(windowline4)

    windowline5 = Line(Point(18, -75), Point(18, -100))
    windowline5.setWidth(2)
    windowline5.setColor('black')
    myCanvas.draw(windowline5)

    windowline6 = Line(Point(4, -88), Point(30, -88)) 
    windowline6.setWidth(2)
    windowline6.setColor('black')
    myCanvas.draw(windowline6)


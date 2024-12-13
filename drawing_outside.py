from Rectangle import Rectangle
from Circle import Circle
from drawing_house import *
import turtle

# Function to draw outdoor elements on the canvas
def drawing_outside(myCanvas):

    # Drawing the sky
    sky = Rectangle(-300, 250, 600, 600)
    sky.setColor('lightblue')
    myCanvas.draw(sky)

    # Drawing the grass area
    grass = Rectangle(-300, -150, 100, 600)
    grass.setColor('green')
    myCanvas.draw(grass)

    # Drawing the sun
    sun = Circle(-90, 50, 35)
    sun.setColor('yellow')
    myCanvas.draw(sun)

    # Drawing clouds using circles
    cloud1 = Circle(90, 50, 15)
    cloud1.setColor('white')
    myCanvas.draw(cloud1)

    cloud2 = Circle(100, 50, 15)
    cloud2.setColor('white')
    myCanvas.draw(cloud2)

    cloud3 = Circle(120, 50, 15)
    cloud3.setColor('white')
    myCanvas.draw(cloud3)

drawing_outside(myCanvas)

drawing_house()

turtle.done()
import turtle  

class Canvas:
    def __init__(self, w, h):
        self.__visibleObjects = []   
        self.__turtle = turtle.Turtle() 
        self.__screen = turtle.Screen()  
        self.__screen.setup(width=w, height=h)  
        self.__turtle.hideturtle()  

    def drawAll(self):
        self.__turtle.reset()  
        self.__turtle.up()  
        self.__screen.tracer(0)  
        for shape in self.__visibleObjects:  
            shape._draw(self.__turtle)  
        self.__screen.tracer(1)  
        self.__turtle.hideturtle()  

    def addShape(self, shape):
        self.__visibleObjects.append(shape)  

    def draw(self, gObject):
        gObject.setCanvas(self)  
        gObject.setVisible(True)  
        self.__turtle.up()  
        self.__screen.tracer(0)  
        gObject._draw(self.__turtle)  
        self.__screen.tracer(1)  
        self.addShape(gObject)  

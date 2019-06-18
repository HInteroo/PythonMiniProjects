from cs1graphics import *
from time import *
from random import *

class graphics(object):
    def __init__(self,Background,width,length,dx,dy,color):
        self.Background = Background
        self.shape = Rectangle(width,length,Point(dx,dy))
        self.shape.setFillColor(color)
        self.Background.add(self.shape)

    def createRectangles(self,width,length,dx,dy,color):
        m = Rectangle(width,length,Point(dx,dy))
        m.setFillColor(color)
        self.Background.add(m)

    def createCircles(self,radius,dx2,dy2,color):
        y = Circle(radius,Point(dx2,dy2))
        y.setFillColor(color)
        self.Background.add(y)
 
    
if __name__ == '__main__':
    Background = Canvas(600,600,'white','Random Pop-up Shapes.')
    awesome = graphics(Background,40,40,300,300,'blue')
    x = 0
    while x < 500:
        width,length = randint(30,50),randint(30,50)
        dx,dy = randint(0,600),randint(0,600)
        dx2,dy2 = randint(0,600),randint(0,600)
        colors = ['green','purple','white','black','pink','blue','red',\
                  'dark blue','dark red', 'dark green','grey','brown',\
                  'cyan','yellow']
        radius = randint(20,30)
        awesome.createRectangles(width,length,dx,dy,colors[randint(0,13)])
        awesome.createCircles(radius,dx2,dy2,colors[randint(0,13)])
        x=x+1
        sleep(0.01)

        

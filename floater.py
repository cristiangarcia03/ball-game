# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random

def angle_changer(angle):
    change = random.random() + -0.5
    return angle + change

def speed_changer(speed):
    change = random.random() + -0.5
    if speed + change >= 3 and speed + change <= 7:
        return speed + change
    elif speed + change < 3:
        return speed - change
    elif speed + change > 7:
        return speed - change

class Floater(Prey):
    radius = 5 
    def __init__(self, x, y, angle, width=10, height=10, speed=5):
        Prey.__init__(self, x, y, width, height, angle, speed)
        self._x = x 
        self._y = y  
        self._width = width
        self._height = height
        self._color = 'red'
        self._angle = angle
        
    def update(self, model):
        self.move()
        self.wall_bounce()
        
        num = random.randint(1,10)
        if num < 4:
            self._angle = angle_changer(self._angle)
            self._speed = speed_changer(self._speed)
            
    
    def display(self,canvas):
        canvas.create_oval(self._x - Floater.radius, 
                           self._y - Floater.radius, 
                           self._x + Floater.radius, 
                           self._y + Floater.radius, 
                           fill=self._color)


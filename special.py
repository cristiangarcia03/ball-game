from prey import Prey
import math

# Spins in a spiral able to get sucked up by black holes, similar 
# to how planets orbit out into a black hole

class Special(Prey):
    radius = 9
    def __init__(self, x, y, angle, width = 5, height = 5, speed = 1):
        Prey.__init__(self, x, y, width, height, angle, speed)
        self._x = x 
        self._y = y 
        self._width = width 
        self._height = height
        self._angle = angle
        self._speed = speed
    
    def move(self):
        self.change_location(self._speed*math.cos(self._angle),
                             self._speed*math.sin(self._angle))
    
    def update(self, model):
        self.move()
        self._angle += 0.5
        if self._speed < 50:
            self._speed += 0.2
    
    def display(self,canvas):
        canvas.create_oval(self._x - Special.radius, 
                           self._y - Special.radius, 
                           self._x + Special.radius, 
                           self._y + Special.radius,
                           outline = 'grey',
                           fill= 'pink',
                           width=2)
        
        canvas.create_oval(self._x - (Special.radius - 4), 
                           self._y - (Special.radius - 4), 
                           self._x + (Special.radius - 4), 
                           self._y + (Special.radius - 4),
                           outline = 'orange',
                           fill= 'purple',
                           width=2)
    

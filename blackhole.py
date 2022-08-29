# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    radius = 10
    def __init__(self, x, y, width = 20, height = 20):
        Simulton.__init__(self, x, y, width, height)
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = 'black'
        self._radius = self.radius
    
    def contains(self, cords):
        return self.distance(cords) <= 10
    
    def update(self, model):
        eaten = set()
        
        for prey in model.find(lambda x: isinstance(x, Prey)):
            if self.contains(prey.get_location()):
                model.remove(prey)
                eaten.add(prey)

        return eaten
        
    
    def display(self,canvas):
        canvas.create_oval(self._x - self._radius, 
                           self._y - self._radius, 
                           self._x + self._radius, 
                           self._y + self._radius, 
                           fill=self._color)

# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    gaze = 200
    def __init__(self,x,y,angle, speed=5, height=20, width=20):
        Mobile_Simulton.__init__(self, x, y, width, height, angle, speed)
        Pulsator.__init__(self, x, y, height, width)
        self._y = y 
        self._x = x
        self._angle = angle
        self._speed = speed
        self._height = height 
        self._width = width
        self._radius = 10
    
    def update(self, model):
        self.move()
        for prey in model.find(lambda x: isinstance(x, Prey)):
            cords = (prey._x,prey._y)
            if self.distance(cords) <= self.gaze:
                self._angle = atan2(cords[1] - self._y, cords[0] - self._x)
        
        Pulsator.update(self,model)

# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey


class Ball(Prey):
    radius = 5
    def __init__(self, x, y, angle, width = 10, height=10, speed=5):
        Prey.__init__(self, x, y, width, height, angle, speed)
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = 'blue'
    
    def update(self, model):
        self.move()
        self.wall_bounce()
    
    def display(self,canvas):
        canvas.create_oval(self._x - Ball.radius, 
                           self._y - Ball.radius, 
                           self._x + Ball.radius, 
                           self._y + Ball.radius, 
                           fill=self._color)

# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
from prey import Prey


class Pulsator(Black_Hole):
    count = 30
    def __init__(self,x ,y, height = 20, width = 20):
        Black_Hole.__init__(self, x, y, width, height)
        self._height = height 
        self._width = width
        self._count = None
        self._color = 'black'
        self._radius = 10
        self._count = self.count
    
    def update(self, model):
        eaten = set()
        ate = False

        for prey in model.find(lambda x: isinstance(x, Prey)):
            if self.contains(prey.get_location()):
                ate = True
                model.remove(prey)
                eaten.add(prey)
                self._radius += 0.5
                self._height += 1
                self._width += 1
                self._count = 31

                
        if not ate:
            if self._count == 1:
                self._radius -= 0.5
                self._height -= 1
                self._width -= 1
                self._count = 31
                #print('shrink', model.count(), self._radius)
        self._count -= 1
            

        return eaten

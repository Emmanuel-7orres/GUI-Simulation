# This Black_Hole class is derived from Simulton; for updating it finds+removes
#   objects (of any class Prey derived class) whose center is contained inside
#   its radius (returning a set of all eaten simultons), and it displays as a
#   black circle with a radius of 10 (width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
from pickle import TRUE



class Black_Hole(Simulton):  
    radius = 10
    
    def __init__(self, x, y, width = 20, height = 20):
        Simulton.__init__(self, x, y, width, height)
        self.eaten = set()
    
    
    def _contains(self, s):
        if self.distance(s.get_location()) <= self.get_dimension()[0]:
            return True
        else:
            return False


    def update(self, running, model, step=False):
        if running or step:
            self.eaten.clear()
            for s in model.all_simultons:
                if isinstance(s,Prey):
                    if self._contains(s):
                        self.eaten.add(s)
                        model.eaten.add(s)
            return self.eaten
        else:
            self.set_location(self.get_location()[0], self.get_location()[1])
          
            
    def display(self, canvas):
        canvas.create_oval(self.get_location()[0]-self.get_dimension()[0], self.get_location()[1]-self.get_dimension()[1],
                                self.get_location()[0]+self.get_dimension()[0], self.get_location()[1]+self.get_dimension()[1], fill='black')
        

# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 
'''
For every object a Pulsator eats, its dimension (both width and height) grows by 1 and 
its "time between meals" counter is reset; whenever it is goes 30 updates without eating anything, 
its dimension (both width and height) shrinks by 1; and if the dimesions ever shrink to 0, 
the object starves and removes itself from the simulation. 
A non-eating pulsator (starting with radius 10: width and height 20) will shrink to 0 in 600 cycles: 
20 times it shrinks its width and height by 1). The update method should still return the set of simultons eaten. 
Hint: 2 methods (__init__ and update), 1 self variable -for that pulsator's counter-, and 1 class variable for the counter constant of 30).
'''

from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    counter = 30
    
    
    def __init__(self, x, y, width = 20, height = 20):
        Black_Hole.__init__(self, x, y, width, height)
        self.update_counter = 0

    
    def update(self, running, model, step=False):
        
        if running or step:
            self.update_counter += 1
            self.set_location(self.get_location()[0], self.get_location()[1])
            eaten = Black_Hole.update(self, running, model, step)
            if self.update_counter == 30 and len(eaten) == 0:
                #print('shrink')
                self.change_dimension(-1, -1)
                self.set_location(self.get_location()[0], self.get_location()[1])
                dimensions = self.get_dimension()
                #print(dimensions)
                self.update_counter = 0
                if dimensions[0] == 0:
                    #print('dead')
                    model.eaten.add(self)
                    self.eaten.add
                return self.eaten
            else:
                if len(eaten) != 0:
                    #print('grow')
                    self.change_dimension(len(eaten), len(eaten))
                    self.set_location(self.get_location()[0], self.get_location()[1])
                    self.update_counter = 0
        else:
            self.set_location(self.get_location()[0], self.get_location()[1])
            
            
    def display(self, canvas):
        canvas.create_oval(self.get_location()[0]-self.get_dimension()[0], self.get_location()[1]-self.get_dimension()[1],
                            self.get_location()[0]+self.get_dimension()[0], self.get_location()[1]+self.get_dimension()[1], fill='black')


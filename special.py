#This special type is red, avoids all hunters by speeding up and changing angles to outmaneuver hunters.

from prey import Prey
from pulsator import Pulsator
from math import atan2

class Special(Prey): 
    radius = 7.5
    
    
    def __init__(self, x, y, width = 15, height = 15, angle = 0, speed = 5):
        Prey.randomize_angle(self)
        angle = Prey.get_angle(self)
        Prey.__init__(self, x, y, width, height, angle, speed)


    def update(self, running, model, step=False):
        if running or step:
            possible = []
            for p in model.all_simultons:
                if isinstance(p,Prey):
                    pass
                else:
                    if self.distance(p.get_location()) <= 50:
                        possible.append((self.distance(p.get_location()), p))
            possible.sort()
            if possible == []:
                self.set_speed(5)
                self.move()
            else:
                prey_location = possible[0][1].get_location()         
                hunter_location = self.get_location()
                angle = atan2((prey_location[1] - hunter_location[1]),(prey_location[0] - hunter_location[0]))
                self.set_angle(angle)
                self.set_speed(-20)
                self.move()
                self.randomize_angle()
                self.set_speed(8)
                self.move()
                
                #self.move()
        else:
            Prey.set_location(self, Prey.get_location(self)[0], Prey.get_location(self)[1])
        
        
    def display(self, canvas):
        canvas.create_oval(Prey.get_location(self)[0]-Special.radius, Prey.get_location(self)[1]-Special.radius,
                                Prey.get_location(self)[0]+Special.radius, Prey.get_location(self)[1]+Special.radius, fill='red')
        
        
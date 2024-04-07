# The Hunter class is derived from Pulsator first and then Mobile_Simulton.
#   It inherits updating/displaying from Pusator and Mobile_Simulton: it pursues
#   close prey, or moves in a straight line, like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2

'''
Each Hunter behaves and initially looks like a Pulsator, 
except for the following additional behavior. A Hunter always moves at 5 pixels/update, 
and intially is moving at a random angle. 
Use the find method in the model module to locate all objects that are instance of Prey 
(or any of its subclasses no matter how many are added later) 
and whose locations are within a distance of 200 of the Hunter 
(hint: see the methods in the Simulton class); 
if any are seen, find the closest one and set the hunter's angle to point at that simulton: to hunt it. 
Hint: To determine the angle, compute the difference between the y coordinates 
and the difference between the x coordinates of the center of the closest prey simulton minus the center of the Hunter. Instead of dividing them to compute the tangent of the angle between them (and then calling math.atan to compute the angle), just call the math.atan2 function (with these differences as separate arguments) to determine the angle the Hunter should move to head towards the prey. By using math.atan2 and avoiding the division, there will not be a "divide by 0" problem, if the prey is directly over the hunter (have the same x coordinate):
'''

class Hunter(Pulsator, Mobile_Simulton):
    
    
    def __init__(self, x, y, width = 20, height = 20):
        Mobile_Simulton.randomize_angle(self)
        angle = Mobile_Simulton.get_angle(self)
        
        Pulsator.__init__(self, x, y, width, height)
        
        Mobile_Simulton.__init__(self,x,y,width,height,angle,5)


    def update(self, running, model, step=False):
        possible = []
        if running or step:
            Pulsator.update(self, running, model, step)
            for p in model.all_simultons:
                if isinstance(p,Prey):
                    if self.distance(p.get_location()) <= 200:
                        possible.append((self.distance(p.get_location()), p))
            possible.sort()
            if possible == []:
                self.move()
            else:
                prey_location = possible[0][1].get_location()         
                hunter_location = self.get_location()    
                
                angle = atan2((prey_location[1] - hunter_location[1]),(prey_location[0] - hunter_location[0]))
                self.set_angle(angle)
                self.move()
            
            
        else:
            self.set_location(self.get_location()[0], self.get_location()[1])
        
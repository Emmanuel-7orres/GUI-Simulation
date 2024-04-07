# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5
    
    
    def __init__(self, x, y, width = 10, height = 10, angle = 0, speed = 5):
        self.gif = PhotoImage(file = 'ufo.gif')
        Prey.randomize_angle(self)
        
        angle = Prey.get_angle(self)
        
        Prey.__init__(self, x, y, self.gif.width(), self.gif.height(), angle, speed)
        
        
    def update(self, running, model, step=False):
        angle = Prey.get_angle(self)
        speed = Prey.get_speed(self)
        if running or step:
            rand = random() * 100
            if rand > 70:
                Prey.move(self)
            else:
                rand2 = random() * 100
                half_rad = (28.6479 * 3.14159265359) / 180
                if rand2 < 50:
                    angle = angle - half_rad
                    if speed - .5 >= 3:
                        speed = speed - .5
                    else:
                        speed = speed + .5
                else:
                    angle = angle + half_rad
                    if speed + .5 <= 7:
                        speed = speed + .5
                    else:
                        speed = speed - .5
            Prey.set_speed(self, speed)
            Prey.set_angle(self, angle)
            Prey.move(self)
        else:
            Prey.set_location(self, Prey.get_location(self)[0], Prey.get_location(self)[1])
        
        
    def display(self, the_canvas):
        the_canvas.create_image(Prey.get_location(self)[0], Prey.get_location(self)[1], image=self.gif)

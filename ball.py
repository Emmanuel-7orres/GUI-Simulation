# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey


class Ball(Prey): 
    radius = 5
    
    
    def __init__(self, x, y, width = 10, height = 10, angle = 0, speed = 5):
        Prey.randomize_angle(self)
        angle = Prey.get_angle(self)
        Prey.__init__(self, x, y, width, height, angle, speed)


    def update(self, running, model, step=False):
        if running or step:
            Prey.move(self)
        else:
            Prey.set_location(self, Prey.get_location(self)[0], Prey.get_location(self)[1])
        
        
    def display(self, canvas):
        canvas.create_oval(Prey.get_location(self)[0]-Ball.radius, Prey.get_location(self)[1]-Ball.radius,
                                Prey.get_location(self)[0]+Ball.radius, Prey.get_location(self)[1]+Ball.radius, fill='blue')
        
        
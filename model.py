import controller
import model   # Calling update in update_all passes a reference to this model

#Use the reference to this module to pass it to update methods

from ball      import Ball
from blackhole import Black_Hole
from floater   import Floater
from hunter    import Hunter
from pulsator  import Pulsator
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0
all_simultons = set()
eaten       = set()
ball = None


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,all_simultons
    running     = False
    cycle_count = 0
    all_simultons = set()
    
    
#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count,all_simultons
    cycle_count +=  1
    for s in all_simultons:
        s.update(running, model, True)


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global ball
    ball = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global ball,all_simultons
    
    if ball == "Ball":
        add(Ball(x,y))
    elif ball == "Floater":
        add(Floater(x,y))
    elif ball == "Black_Hole":
        add(Black_Hole(x, y))
    elif ball == "Pulsator":
        add(Pulsator(x,y))
    elif ball == "Hunter":
        add(Hunter(x,y))
    elif ball == "Special":
        add(Special(x,y))
    elif ball == "Remove":
        for b in all_simultons:
            if b.contains((x,y)):
                remove(b)
                break

#add simulton s to the simulation
def add(s):
    global all_simultons
    all_simultons.add(s)


# remove simulton s from the simulation    
def remove(s):
    global all_simultons
    all_simultons.remove(s)


#find/return a set of simultons that each satisfy predicate p    
def find(p):
    global all_simultons
    found = set()
    for b in all_simultons:
        if p(b):
            found.add(b)
    return found


#For each simulton in model's simulation, call update on it, passing along model
#This function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton's update do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global all_simultons,running,eaten 
    for b in all_simultons:
        b.update(running, model)
    for dead in eaten:
        all_simultons.remove(dead)
    eaten.clear()
    


        

#Animation: (a) delete all simultons on the canvas; (b) call display on all
#  simultons being simulated, adding back each to the canvas, often in a new
#  location; (c) update the label defined in the controller showing progress 
#This function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    global all_simultons,cycle_count,running
    #(a) delete all simultons on the canvas
    controller.the_canvas.delete("all")
    
    #(b) call display on all simultons being simulated
    #    adding back each to the canvas, often in a new location
    for b in all_simultons:
        b.display(controller.the_canvas)
        
    #(c) update the label defined in the controller showing progress
    sims = len(all_simultons)
    if running:
        cycle_count += 1
    controller.the_progress.config(text=f"{cycle_count} updates/{sims} simultons") 
    

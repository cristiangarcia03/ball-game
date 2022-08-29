import controller
import model   # Calling update in update_all passes a reference to this model
import random, math

#Use the reference to this module to pass it to update methods

from ball       import  Ball
from blackhole  import  Black_Hole
from floater    import  Floater
from hunter     import  Hunter
from pulsator   import  Pulsator
from special    import Special

def random_speed():
    # Magnitude is 5-10
    return random.randint(5,10)

def random_angle():
    # between 0 and 2pi
    return random.random()*math.pi*2
# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

running     = False
cycle_count = 0
balls       = set()
memory = None

def count():
    return cycle_count
#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset():
    global running, cycle_count, balls
    running = False
    cycle_count = 0
    balls = set()


#start running the simulation
def start():
    global running
    running = True

#stop running the simulation (freezing it)
def stop():
    global running
    running = False


#step just one update in the simulation
def step():
    global cycle_count, running
    running = False
    cycle_count += 1
    for b in balls:
        b.update(model)


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global memory
    memory = kind
    


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    #print(x,y)
    
    if memory == 'Remove':
        temp = balls.copy()
        for ball in temp:
            if ball.contains((x,y)):
                remove(ball)
    elif memory == 'Ball':
        add(Ball(x,y, random_angle()))
                
    elif memory == 'Floater':
        balls.add(Floater(x,y, random_angle()))
                
    elif memory == 'Black_Hole':
        add(Black_Hole(x,y))
                
    elif memory == 'Pulsator':
        add(Pulsator(x, y))
            
    elif memory == 'Hunter':
        add(Hunter(x,y,random_angle()))
            
    elif memory == 'Special':
        add(Special(x, y, random_angle()))


#add simulton s to the simulation
def add(s):
    global balls
    balls.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global balls
    balls.remove(s)
        
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    res = set()
    for ball in balls:
        if p(ball):
            res.add(ball)
    return res

#Simulation: for each simulton in the model, call its update, passing it model
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's update do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count += 1
        for b in list(balls):
            b.update(model)

#Animation: clear then canvas; for each simulton in the model, call display
#  (a) delete all simultons on the canvas; (b) call display on all simultons
#  being simulated, adding back each to the canvas, often in a new location;
#  (c) update the label defined in the controller showing progress 
#Loop over a set containing all the simultons; do not use type or isinstance:
#  let each simulton's display do the needed work, without this function knowing
#  what kinds of simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
        
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")











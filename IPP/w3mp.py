#Timers
import simpleguitk as simplegui 

# define global variables
interval = 100

miliseconds = 0
message = ""

stops = 0
points = 4

counter = str(stops) + "/" + str(points)

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global message
    A = t/600
    D = t%10
    C = t/10

    if C > 9:
        C = str(C)[1]

    if t/10 > 9 and t/10 < 59: 
        B = str(t/10)[0]
    else:
        B = 0 

    if A > 9:
        A = 0

    message = str(A) + ":" + str(B) + str(C) + "." + str(D)


format(miliseconds)
     
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global stops, points, counter
    stops = stops + 1; 
    
    p = miliseconds%10 

    st = timer.stop()

    if p == 0:
        points = points + 1

    counter = str(stops) + "/" + str(points)

    if not timer.is_running() and stops != points:
        timer.start()
    else:
        timer.stop()

    
def reset():
    global miliseconds
    miliseconds = 0
    stops = 0

    timer.stop
    
    format(miliseconds)

# define event handler for timer with 0.1 sec interval
def tick():
    global miliseconds, seconds, minutes
    miliseconds = miliseconds + 1
    
    format(miliseconds)

# define draw handler
def draw(canvas):
    canvas.draw_text(message, [80,130], 36, "white")
    canvas.draw_text(counter, [250,40], 25, "green")
    
# create frame
frame = simplegui.create_frame("Cronometer", 300, 200)

# register event handlers
start = frame.add_button("Start", start)
stop = frame.add_button("Stop", stop) 
reset = frame.add_button("Reset", reset) 

frame.set_draw_handler(draw)

timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()

# Please remember to review the grading rubric


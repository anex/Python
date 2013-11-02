#Canvas


#Canvas handler
import simplegui

def draw(canvas):
    canvas.draw_text("Hello", [100, 100], 24, "Red")
    canvas.draw_circle([100, 100], 5, 5, "Yellow")


frame = simplegui.create_frame("test", 300, 200)

frame.set_draw_handler(draw)

frame.start()

#String processing
s = "Carlos Paredes"
print s[6]
print s[-4]
print len(s)
print s[0:7]
print s[:7]

s2 = 475
print str(s2)

def convert(val):
    dollar = int(val)
    cents = int(100 * (val - dollar))
    return str(dollar) + " dollars and " + str(cents) + " cents"

print convert(11.23)

#Interactive Drawing
import simplegui

values = 3.12

def convert(val):
    dollar = int(val)
    cents = int(100 * (val - dollar))
    return str(dollar) + " dollars and " + str(cents) + " cents"

def draw(canvas):
    canvas.draw_text(convert(values),  [60,  110],  24,  "white")

def input_handler(text):
    global values
    values = float(text)

frame = simplegui.create_frame("Converter",  300,  200)

frame.set_draw_handler(draw)

frame.add_input("Enter Value",  input_handler,  50) 

frame.start()

#Timers
import simplegui, random

message = "Carlos" 
position = [50, 50]
w = 500
h = 500
interval = 2000

def update(text):
    global message
    message = text

def tick():
    x = random.randrange(0, w)
    y = random.randrange(0, h)
    position[0] = x
    position[1] = y

def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")

frame = simplegui.create_frame("ScreenSaver",  w,  h)

text = frame.add_input("Message",  update,  50) 

frame.set_draw_handler(draw)

timer = simplegui.create_timer(interval, tick)

frame.start()
timer.start()

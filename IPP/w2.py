#Simplegui and Events handlers

# Structure of program
import simplegtk as simplegui
#Globals
counter = 0
#Helper functions
def increment():
    global counter
    counter += 1
#Event Handler
def tick():
    increment()
    print counter
#Create Frame
frame = simplegui.create_frame("Test",  100,  100)
#Register events
timer = simplegui.create_timer(1000,  tick)
frame.add_button("Start",  tick)
#Start frames and timers
frame.start()
timer.start()

# Buttons
import simplegui

store = 12
operand = 3

def output():
    print "Store =",  store
    print "Operand =",  operand
    print ""

def swap():
    global store,  operand
    store,  operand = operand,  store    

def add():
    global store,  operand
    store = store + operand
    output()

def sub():
    global store,  operand
    store = store - operand
    output()

frame = simplegui.create_frame("Calculadora",  200,  200)
frame.add_button("Print",  output,  100)
frame.add_button("Swap",  swap,  100)
frame.add_button("Add",  add,  100)
frame.add_button("Sub",  sub,  100)

frame.start()

#Inputs
import simplegui

store = 0
operand = 0

def test():
    global store
    store = operand

def s(var):
    global operand
    operand = var
    output()

def output():
    print store,  operand

frame = simplegui.create_frame("Test",  200,  200)
frame.add_button("Test",  test)
frame.add_input("Test",  s,  50)

frame.start()

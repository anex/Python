# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code

num_range = 100
num = 0
num_remain = 0

# helper function to start and restart the game
def new_game():
    global num, num_remain
    num = random.randrange(0, num_range)
    
    num_remain = int(math.ceil(math.log(num_range, 2)))

    print "New game, Range is from 0 to", num_range
    print "Number of remaining guesses is", num_remain, "\n"
    
    frame.start()

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    
    new_game()    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global num_remain
    num_remain = num_remain -1
     
    print "Guess was", guess
    print "Number of remaining guesses is", num_remain
    
    if int(guess) < num:
        print "Higher\n"
    elif int(guess) == num:
        print "Correct\n"
        new_game()
    elif int(guess) > num_range:
        print "Guess out of range\n"
    else:
        print "Lower\n"
        
    if num_remain == 0:
        print "You Lose\n"
        new_game()
        
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game and start frame
new_game()


# always remember to check your completed program against the grading rubric

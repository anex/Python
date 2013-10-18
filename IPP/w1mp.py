#!/usr/bin/env python
import random

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock",  "paper",  "scissors",  "lizard",  "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
# fill in your code below

# convert number to a name using if/elif/else
# don't forget to return the result!
    if number == 0:
        name = "rock"
    elif number == 2:
        name = "paper"
    elif number == 1:
        name = "Spock"
    elif number == 3:
        name = "lizard"
    else:
        name = "scissors"

    return name

def name_to_number(name):
# fill in your code below

# convert name to number using if/elif/else
# don't forget to return the result!
    if name == "rock":
        number = 0
    elif name == "paper":
        number = 2
    elif name == "Spock":
        number = 1
    elif name == "lizard":
        number = 3
    else:
        number = 4

    return number

def rpsls(name): 
# fill in your code below

# convert name to player_number using name_to_number
    player_number = name_to_number(name)
    print "Player chosses "+name

# compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    print "Computer chosses "+number_to_name(comp_number)+"\n"

# compute difference of player_number and comp_number modulo five
    if player_number != comp_number:
        print "Escogieron diferente"

# use if/elif/else to determine winner

# convert comp_number to name using number_to_name
    #results = number_to_name(winner_number)

    #print results+"\n"

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

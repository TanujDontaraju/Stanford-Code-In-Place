# Link to view project: https://codeinplace.stanford.edu/cip5/share/VuwtGhtPMcTfNjtr090Y

from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

# Main function holding all sub functions for Karel to fill all types of worlds properly
def main():
    while front_is_clear():
        place_beeper()
        put_beeper()
        next_row()
    go_to_end()

# Lets Karel place how many ever beepers it can to fill each row
def place_beeper():
    while front_is_clear():
        put_beeper()
        move()

# Moves Karel to next row 
def next_row():
    for i in range (2):
        turn_left()
    while front_is_clear():
        move()
    turn_right()
    if front_is_clear():
        move()
        turn_right()

# Makes Karel go to intended end point
def go_to_end():
    turn_right()
    while front_is_clear():
        move()

# Lets Karel turn right (1x turn_right() = 3x turn_left())
def turn_right():
    for i in range (3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()

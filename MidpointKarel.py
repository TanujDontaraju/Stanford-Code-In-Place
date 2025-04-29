# Link to view project: https://codeinplace.stanford.edu/cip5/share/asbNygp70ywikERDBV5O

from karel.stanfordkarel import *

# Main program to find and stop at the midpoint of 1st Street
def main():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
    turn_around()
    for i in range(11):
        remove_end_beeper()  
    while no_beepers_present():
        move()
    turn_around()
    while not_facing_east():
        turn_left()

# Turns Karel 180 degrees   
def turn_around():
    turn_left()
    turn_left()

# Removes beepers from both ends and moves them toward the center
def remove_end_beeper():
    while no_beepers_present():
        move()
    pick_beeper()
    move()
    if no_beepers_present():
        turn_around()
        move()
        put_beeper()
    while front_is_clear():
        move()
    turn_around()


if __name__ == '__main__':
    main()

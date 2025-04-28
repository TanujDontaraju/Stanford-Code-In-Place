# Link to view project: https://codeinplace.stanford.edu/cip5/share/5r32uOxUI5hcuygkh5BF

from karel.stanfordkarel import *


# Main function that uses sub-functions to handle both Hospital 1 and small cases.
def main():
    for i in range (3):
        while front_is_clear():
            if no_beepers_present():
                move()
            else:
                build_hospital()     
        
# Builds the hospital structure with beepers in the intended shape.
def build_hospital():
    turn_left()
    for i in range (2):
        move()
        put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    for i in range (2):
        move()
        put_beeper()
    turn_left()
    if front_is_clear():
        move()

# Function to turn right 
def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()

# Link to view project: https://codeinplace.stanford.edu/cip5/share/CaOGjFC3WRBRFdPJZG4C

from karel.stanfordkarel import *

# Main function to make Karel work properly
def main():
    make_column()
    to_next_spot()
    make_column()
    to_next_spot()
    make_column()
    to_next_spot()
    make_column()
    to_final_position()

# Replaces intended missing columns with beepers
def make_column():
    turn_left()
    for i in range (4):
        if front_is_clear():
            put_beeper()
            move()
    put_beeper()

# Moves Karel to the next intended column
def to_next_spot():
    turn_right()
    move()
    turn_right()
    for i in range (4):
        move()
    turn_left()
    for i in range (3):
        move()

# Moves Karel to designated end point
def to_final_position():
    turn_right()
    turn_right()
    for i in range (4):
        move()
    turn_left()

# Function to turn right
def turn_right():
    for i in range (3):
        turn_left()

if __name__ == '__main__':
    main()

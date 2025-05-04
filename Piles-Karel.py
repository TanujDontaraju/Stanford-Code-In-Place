# Link to view project: https://codeinplace.stanford.edu/cip5/share/zD6hiRbnpJ68I6VMTbS6

from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()    
    # Code to move Karel to end while picking up all beepers
    pick_up_all_beeper()
    next_beeper()
    pick_up_all_beeper()
    next_beeper()
    pick_up_all_beeper()
    move()

# Function to pick up all 10 beepers each time Karel is on a beeper spot        
def pick_up_all_beepers():
    for i in range(10):
        pick_beeper()

# Function to move Karel to next designated beeper
def next_beeper():
    for i in range(2):
        move()
        

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()

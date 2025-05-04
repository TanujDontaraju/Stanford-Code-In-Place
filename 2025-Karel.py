# Link to view project: https://codeinplace.stanford.edu/cip5/share/YPkuxy9zdlg0MjkVcuLJ

from karel.stanfordkarel import *

def main():
    # First for loop to put the beeer 20 times
    for i in range(20):
        put_beeper()
    # Move action to move Karel to second spot to put 25 other beepers
    move()
    # Second for loop to put the beeper 25 times
    for i in range(25):
        put_beeper()
    # Move action to move Karel to final spot
    move()

if __name__ == '__main__':
    main()

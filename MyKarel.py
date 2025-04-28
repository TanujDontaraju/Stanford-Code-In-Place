#Link to view project: https://codeinplace.stanford.edu/cip5/share/9ZXjaBObI8OgHYW2ImiJ

from karel.stanfordkarel import *

# Main function 
def main():
    for i in range(5):
        move()
    paint_dinasour()

# Function for painting the dinasour
def paint_dinasour():
    first_row()
    turn_right()
    move()
    turn_right()
    second_row()
    for i in range(5):
        move()
    turn_left()
    move()
    turn_left()
    third_row()
    turn_right()
    move()
    turn_right()
    fourth_row()
    turn_left()
    move()
    turn_left()
    fifth_row()
    turn_right()
    move()
    turn_right()
    sixth_row()

# Function to paint first row
def first_row():
    for i in range (7):
        move()
    for i in range(3):
        paint_corner("purple")
        move()
    paint_corner("purple")

# Function to paint second row
def second_row():
    paint_corner("purple")
    move()
    paint_corner("black")
    move()
    for i in range(2):
        paint_corner("purple")
        move()
    move()
    for i in range(5):
        paint_corner("purple")
        move()

# Function to paint third row
def third_row():
    for i in range(5):
        move()
    for i in range(10):
        paint_corner("purple")
        move()
    paint_corner("purple")

# Function to paint fourth row
def fourth_row():
    for i in range(12):
        paint_corner("purple")
        move()
    paint_corner("purple")

# Function to paint fifth row
def fifth_row():
    for i in range(3):
        move()
    for i in range(3):
        paint_corner("purple")
        move()
    move()
    move()
    for i in range(3):
        paint_corner("purple")
        move()

# Function to paint sixth row
def sixth_row():
    move()
    for i in range(3):
        paint_corner("purple")
        move()
    move()
    move()
    for i in range(3):
        paint_corner("purple")
        move()
    
# Function to turn right (1x turn_right() = 3x turn_left())
def turn_right():
    for i in range(3):
        turn_left()


# don't change this code
if __name__ == '__main__':
    main()

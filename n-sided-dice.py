# Link to view project: http://codeinplace.stanford.edu/cip5/share/Rplm5hBHl3DLTSkiiBKH

# Import statement so we can utilize line 9
import random

# Main Function
def main():
    # Lets user input an int value for how many sides dice has. Use "int" to not have any decimals
    dice_sides_value = int(input("How many sides does your dice have? "))
    # Random number selector that decides the roll number from 1 to how ever many sides you inputted
    rand_num = random.randint(1, dice_sides_value)
    # Prints out the value. Use "f" if print statement doesn't work
    print(f"Your roll is {rand_num}")

# No changes from here
if __name__ == '__main__':
    main()

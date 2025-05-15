# Link to view project: https://codeinplace.stanford.edu/cip5/share/CbbE4YY6QTWWNTnAYMRr

# Lets us utilize random function
import random

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

# Main function that prints out 10 random numbers each time without repeating numbers
def main():
    # Gives range of numbers
    numbers = random.sample(range(1, 101), 10)
    # For loop to print the 10 numbers
    for num in numbers:
        print(num)

# No changes from here
if __name__ == '__main__':
    main()

# Link to view project: https://codeinplace.stanford.edu/cip5/share/CwkBqDvKUjvp5FcwwufN

# Main Function 
def main():
    # Sets start variable to 10
    x = 10
    # Prints start variable
    print(x)
    # For loop to make the countdown
    for i in range(9):
        # Substracts x each time so same number doesn't repeat
        x -= 1
        # Prints the new number
        print(x)
    # After for loop is finished, this is printed
    print("Liftoff!")
        
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

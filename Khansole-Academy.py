# Link to view project: https://codeinplace.stanford.edu/cip5/share/CKgrPEhrpY2Y8drJBBzt

# Import statement to let us use random function
import random

# Main Function
def main():
    # Initial print statement
    print("Khansole Academy")
    # Generates first random two-digit number
    first_num = random.randint(10, 99)
    # Generates second random two-digit number
    second_num = random.randint(10, 99)
    # Adds both the random generated numbers
    added_value = first_num + second_num
    # Prints the two random generated numbers to ask in an addition question
    print(f"What is {first_num} + {second_num}?")
    # Lets user print out their answer that they think is right
    answer = int(input("Your answer: "))
    # If statement if the user is correct
    if answer == first_num + second_num:
        # Prints if the answer inputted correct
        print("Correct!")
    # Else statement if the user is incorrect 
    else:
        # Print statement if the answer is incorrect
        print("Incorrect.")
        # Print statement that gives the correct answer
        print(f"The expected answer is {added_value}")
    
# No changes from here
if __name__ == '__main__':
    main()

# Link to veiw project https://codeinplace.stanford.edu/cip5/share/8lVnqJkL2Vx0qukfeNYD

# Main Function
def main():
    # Given print statement
    print("This program multiplies two numbers.")
    # Value for num1. Use int instead of float to not get decimal answers
    num1 = int(input("Enter first number: "))
    # Value for num2. Use int instead of float to not get decimal answers
    num2 = int(input("Enter second number: "))
    # Answer for num1 times num2
    print(num1 * num2)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

# Link to view project: https://codeinplace.stanford.edu/cip5/share/JIMyYGlHOQRvwqYmYCxj

# Main Function
def main():
    # Current value that lets user input a value 
    curr_value = int(input("Enter a number: "))
    # While loop to make sure value doesn't get multiplied again if it's above 100
    while curr_value < 100:
        # Changes current value to the doubled value
       curr_value = curr_value * 2
       # Prints each new current value 
       print(curr_value)
     
    
# No changes from here 
if __name__ == '__main__':
    main()

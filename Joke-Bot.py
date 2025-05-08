# Link to view project: https://codeinplace.stanford.edu/cip5/share/4oOdoUo2IGLXIRlNPGH9

# Prompts already given that need to be used
PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Karel is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Karel returns with 13 liters of milk. The programmer asks why and Karel replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes"

# Main Function
def main():
    # User input that lets user prompt JOKE
    user_input = input(PROMPT)
    # If statement to see if the user inputs JOKE
    if user_input == "Joke":
        # If user inputs JOKE, the JOKE gets printed out
        print(JOKE)
    # Else statement to see if user doesn't input JOKE
    else:
        # Prints SORRY if JOKE isn't inputted
        print(SORRY)

# No changes from here
if __name__ == "__main__":
    main()

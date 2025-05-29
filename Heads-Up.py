# Link to view project: https://codeinplace.stanford.edu/cip5/share/npbJuEjxTHPYNTnc3moH

import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'

def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    lines = []
    with open(FILE_NAME) as f:
        for line in f:
            # removes whitespace characters (\n) from the start and end of the line
            line = line.strip() 
            # if the line was only whitespace characters, skip it 
            if line != "":
                lines.append(line)
                
    return lines


def main():
    # Milestone #1: Load words from file
    words = get_words_from_file()
    
    # Check if words were loaded
    if not words:
        print("No words found in the file.")
        return

    print("Welcome to Heads Up!")
    print("When it's your turn, close your eyes.")
    print("Press Enter to get a new word.")
    print("Type 'quit' and press Enter to end the game.\n")

    # Milestone #2 and #3: Show a random word and repeat on Enter
    while True:
        user_input = input("Press Enter to get a word (or type 'quit' to quit): ").strip().lower()

        # If the user typed 'quit', exit the game
        if user_input == 'quit':
            print("Exiting the game. Goodbye!")
            break
        
        # Choose a random word from the list
        word = random.choice(words)

        # Display the word
        print(f"\n👉 Your word is: **{word}**")
        print("(The rest of the group should describe this word without using it!)\n")

# This ensures the program only runs when executed directly
if __name__ == '__main__':
    main()

# Link to view project: https://codeinplace.stanford.edu/cip5/share/8pwn0wWjiF3UI4aDh4Rq

# Imports the gpt (AI) function to utilize in line 13
from ai import call_gpt

# Main Function
def main():
    # Lets user input their name
    your_name = input("Enter your name: ")
    # Lets user input a topic for haiku
    topic = input("Enter a topic: ")
    # General print statement for generating haiku
    print("Creating your haiku...")
    # Using gpt (AI) to create a haiku from the name and topic that has been inputted. Use "f" if call_gpt doesn't work properly
    response = call_gpt(f" Use {your_name}, and {topic} and create a haiku from it. When you create the haiku, just put the haiku no other words from you")
    # Empty print line to give blank line for spacing 
    print()
    # Print line to print the response
    print(response)

# No changes from here
if __name__ == "__main__":
    main()

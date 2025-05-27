# Link to view project: https://codeinplace.stanford.edu/cip5/share/zXbILJEscmOhIi8sSBiL

def main():
    # Dictionary with English-Spanish translations
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    correct = 0  # Track correct answers

    for english_word in translations:
        # Prompt for user input (do NOT add a space after the question mark)
        user_input = input(f"What is the Spanish translation for {english_word}?")

        # Check correctness and respond
        if user_input == translations[english_word]:
            print("That is correct!")
            correct += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {translations[english_word]}.")

        # One blank line between questions (as per expected output)
        print()

    # Final result message
    total = len(translations)
    print(f"You got {correct}/{total} words correct, come study again soon!")

# No changes from here
if __name__ == '__main__':
    main()

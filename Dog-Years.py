# Link to veiw project: https://codeinplace.stanford.edu/cip5/share/jUPiwZ5dYELc3NXUW1ZZ

# Value saying 1 human year = 7.18 dog years
DOG_YEARS_MULTIPLIER = 7.18  

# Main Function 
def main():
    # Input for human age. Float used so the value entered is usable without being considered a string 
    human_age = float(input("Enter an age in calendar years: "))
    # Multiplies the input for human age by the dog years multiplier
    dog_years = human_age * DOG_YEARS_MULTIPLIER
    # Use "f" if print statement doesn't work properly 
    print(f"That's {dog_years} in dog years!")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()

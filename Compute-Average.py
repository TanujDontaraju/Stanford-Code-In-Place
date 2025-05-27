# Link to view project: https://codeinplace.stanford.edu/cip5/share/vwLnjlAB7qrBKfQriFSA

def main():
    # Load a list of numbers from the file "numbers.txt"
    number_list = load_numbers_from_file("numbers.txt")
    
    # Check if the list is not empty to avoid division by zero
    if len(number_list) > 0:
        # Calculate the average: sum of numbers divided by count
        average = sum(number_list) / len(number_list)
        # Print the result to the user
        print("Average:", average)
    else:
        # Handle the case where the file is empty or contains no valid numbers
        print("The list is empty. No average to compute.")

def load_numbers_from_file(filepath):
    numbers = []  
    
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()  
            if cleaned_line != '':  
                numbers.append(float(cleaned_line)) 
    
    return numbers  

# No changes from here 
if __name__ == '__main__':
    main()

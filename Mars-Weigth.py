# Link to view project: https://codeinplace.stanford.edu/cip5/share/nPuPVIzKIzpG9pYBJQgF

# Main Function 
def main():
    # Input Earth weight
   earth_weight = float(input("Enter a weight on Earth: "))
   # Conversion from earth to mars weight by multiplication 
   mars_weight = earth_weight * 0.378
   # Print statement that displays conversion
   print(f"The equivalent weight on Mars: {mars_weight}")

if __name__ == "__main__":
    main()

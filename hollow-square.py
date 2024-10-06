# Program: Create a Hollow Square Pattern
# Features: Takes the side length of a square as input and prints a hollow square pattern using a function.
# Procedure:
# 1. Define a function to create and display a square pattern of the given length.
# 2. Define a function to take and validate user input for the side length.
# 3. Use loops and conditions to generate the pattern.
# 4. Handle invalid inputs until a valid number is provided.

def create_square(length):
    """Create and display a hollow square pattern of a given length.

    Args:
        length (int): The side length of the square.
    """
    for i in range(length):
        if i == 0 or i == length - 1:
            print("*" * length)
        else:
            print("*" + " " * (length - 2) + "*")

def get_square_length():
    """Get and validate the side length of the square from user input.

    Returns:
        int: The valid side length of the square.
    """
    while True:
        try:
            length = int(input("Enter the side length of the square: "))
            return length
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

# Start of the program
side_length = get_square_length()
create_square(side_length)

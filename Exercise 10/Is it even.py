# Function to determine if a number is even or odd
def check_even_or_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."
# Main function
def main():
    # Ask the user for a number
    try:
        user_input = int(input("Enter a number: "))
        # Pass the number to the function and get the result
        result = check_even_or_odd(user_input)
        # Print the result
        print(result)
    except ValueError:
        print("Invalid input. Please enter an integer.")
# Check if the script is run directly
if __name__ == "__main__":
    main()
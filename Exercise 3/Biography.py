# Get user input for name,hometown,and age
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
# Validate the age input to ensure that it is an integer
while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)  
        break  
    except ValueError:
        print("Please enter a valid number for age.")
# Store the information in a dictionary
user_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}
# Print the values on separate lines using a single print() statement
print(f"Name: {user_info['name']}\nHometown: {user_info['hometown']}\nAge: {user_info['age']}")
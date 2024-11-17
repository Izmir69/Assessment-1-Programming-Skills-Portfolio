# Define the correct password
correct_password = "12345"
# Set the maximum number of attempts
max_attempts = 5
attempts = 0
# Use a while loop to ask for the password with a limit on attempts
while attempts < max_attempts:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Access granted.")
        break  # Exit the loop if the password is correct
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Incorrect password. No attempts left. Authorities have been alerted.")
# If maximum attempts are reached, execute additional action (if needed)
if attempts == max_attempts:
    print("System locked due to multiple failed attempts.")

# A dictionary with country-capital pairs
quiz_data = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Switzerland": "Bern",
    "Austria": "Vienna",
    "Sweden": "Stockholm"
}
# Initialize the score
score = 0
# Loop through each of the question
for country, capital in quiz_data.items():
    user_answer = input(f"What is the capital of {country}? ").strip().lower()
    # Compare answers which ignore the case
    if user_answer == capital.lower():
        print(f"Correct! The capital of {country} is {capital}.")
        score += 1
    else:
        print(f"Wrong! The correct answer is {capital}.")
# Show final score
print(f"\nQuiz Over! You scored {score}/{len(quiz_data)}.")
# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
# Ask the user for the search term
search_term = input("Enter the name to search for: ").strip()
# Search for the term in the list
if search_term in names:
    print(f"{search_term} found in the list!")
else:
    print(f"{search_term} not found in the list.")
# Create a dictionary with a person's name and contact info for a small company, take the input from a user to search for a user using their name, return the number (example user will search for 'Ram' and if user exists, their phone number is returned)

person_info = {
    "Suman":"9840399956",
    "Sujan":"9840433327",
    "Samip":"9841675987",
    "Ram":"9801234567"
}

search_name = input("Enter the name to search:")
if search_name in person_info:
    print(f"{search_name}'s phone number is: {person_info[search_name]}")
else:
    print(f"{search_name} not found in the contact list")
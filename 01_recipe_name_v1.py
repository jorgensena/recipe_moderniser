""" Get the recipe name from the user, check that input doesn't contain
numbers or is not left blank
Created by Amy Jorgensen
Version 1 : 09/06/21
"""

# Ask user for recipe name
recipe_name = input("What is the recipe name? ")

# Error message - in the event that the name contains numbers or is blank
error = "Your recipe name is blank or contains numbers!"

# Check each character is the recipe name for any numbers
contains_number = False
for letter in recipe_name:
    if letter.isdigit():
        contains_number = True

# Print error message if recipe_name is blank or contains numbers
if not recipe_name or contains_number:
    print(error)

else:
    print("That's a good name.")

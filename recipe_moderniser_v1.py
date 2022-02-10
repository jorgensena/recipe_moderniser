""" Recipe moderniser - full working program
Gets recipe name and recipe source (components 1 & 2)
Version 1 - includes 'To Do' list
Created by Amy Jorgensen
5/07/21
"""

# Modules to be used
import csv


# FUNCTIONS
def not_blank(question, error_msg, allow_num):
    error = error_msg
    valid = False
    while not valid:
        number = False  # Initial assumption that name doesn't contain digits
        response = input(question)

        if not allow_num:
            for letter in response:  # Check for digits in recipe_name
                if letter.isdigit():
                    number = True

        if not response or number == True:  # print error for blank name or digits
            print(error)

        else:
            return response

# MAIN ROUTINE

# Set up dictionaries

# Set up list to hold 'modernised' ingredients

# Get recipe name and check it is not blank and contains no numbers
# Customisable error message eg. to include mention of numbers
recipe_name = not_blank("What is the recipe name? ",
                        "The recipe name cannot be blank or contain numbers!",
                        False)  # Doesn't allow digits
print("Today we are making {}, yum!".format(recipe_name))

# Get recipe source and check it's not blank - numbers OK
# Customisable error message eg. to include mention of numbers
source = not_blank("Where is the recipe from? ",
                   "The recipe source can't be blank!",
                   True)  # Allows digits
print("\nThis recipe is from {}".format(source))

# Get serving sizes and desired number of servings

# Get ingredients
# Loop for each ingredient
# Get ingredient amount
# Scale amount using scale factor
# Get ingredient name and check it's not blank and doesn't contain numbers
# Get unit
# Convert to mLs
# Converts from mLs to grams
# Add updated ingredient to list

# Output modernised recipe

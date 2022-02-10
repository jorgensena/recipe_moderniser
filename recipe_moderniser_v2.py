""" Recipe moderniser - full working program
Incorporates scale factor - (component 3)
Version 2 - includes 'To Do' list
Created by Amy Jorgensen
7/07/21
"""

# Modules to be used
import csv
import re


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


# number checking function
# Gets the scale factor - which must be a number
def num_check(question):
    valid = False
    error = "Please enter a number, higher than 0"
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


def get_scale_factor():
    keep_scale = False
    while not keep_scale:

        # Get serving size and check it's a number
        serving_size = num_check("What is the recipe serving size? ")
        # Get desired number of servings and check it's a number
        desired_size = num_check("How many servings would you like: ")
        # Calculate scale factor
        scale_factor = desired_size / serving_size

        # Warn the user if the scale factor is less than 0.25 or more than 4
        if scale_factor < 0.25:
            print("Scale Factor: {}".format(scale_factor))
            print("Warning! This scale factor is very small and you might "
                  "\nstruggle to accurately weigh the ingredients."
                  "\nPlease consider having more servings and freezing the "
                  "left overs.")
            change_scale = input("Press <enter> to keep this scale, "
                                 "or <any key> and <enter> to change it: ")
            if not change_scale:
                keep_scale = True

        elif scale_factor > 4:
            print("Scale Factor: {}".format(scale_factor))
            print("Warning! This scale factor is quite large and you might "
                  "\nstruggle to fit everything in the bowl. "
                  "\nPlease consider having less servings and making more "
                  "than one batch.")
            change_scale = input("Press <enter> to keep this scale, "
                                 "or <any key> and <enter> to change it: ")
            if not change_scale:
                keep_scale = True

        else:
            keep_scale = True

    return scale_factor


# MAIN ROUTINE

# Set up dictionaries

# Set up list to hold 'modernised' ingredients

# Get recipe name and check it is not blank and contains no numbers
# Customisable error message eg. to include mention of numbers
recipe_name = not_blank("What is the recipe name? ",
                        "The recipe name cannot be blank or contain numbers!",
                        False)  # Doesn't allow digits

# Get recipe source and check it's not blank - numbers OK
# Customisable error message eg. to include mention of numbers
source = not_blank("Where is the recipe from? ",
                   "The recipe source can't be blank!",
                   True)  # Allows digits

# Get serving sizes and desired number of servings
# Calculate scale factor
scale_factor = get_scale_factor()
print(scale_factor)

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

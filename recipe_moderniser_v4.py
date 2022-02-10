""" Recipe moderniser - full working program
Incorporates ingredient list splitter - (component 9)
Version 4
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


# Function to get (and check) amount, unit, and ingredient
def get_all_ingredients():
    ingredient_list = []  # Set up ingredient lst
    valid_list = False

    print("\nEnter an ingredient - quantity, unit, then name (or 'X' to "
          "exit): \n")

    line_number = 1 # To make sure entering the ingredients easy to follow
    while not valid_list:
        ingredient_name = not_blank("{}. ".format(line_number),
                                    "The ingredient cannot be blank",
                                    True).title()
        # Check for exit code: 'X'
        if ingredient_name != 'X':
            # If exit code not entered, add ingredient to list
            ingredient_list.append(ingredient_name)
            line_number += 1
        else:
            if len(ingredient_list) < 2:  # Check that list contains at lease 2 items
                print("Please enter at lease two ingredients")
            else:
                valid_list = True  # If contains at least two items, break loop
                return ingredient_list  # Output list


# MAIN ROUTINE

# Set up dictionaries

# Set up list to hold 'modernised' ingredients
modernised_recipe = []

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

# Get ingredients
full_recipe = get_all_ingredients()

# Split each line of the recipe into amount, unit and ingredient
# The regex format below is expecting: number <space> number
# Need to have the r before the docstring to make it a raw string rather than
# a string literal (to pass PEP8 tests)
mixed_regex = r"\d{1,3}\s\d{1,3}\/\d{1,3}"
# \d for a digit, \d{1,3} allows 1-3 digits, \s for space, / for divide

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()
    # Get amount
    if re.match(mixed_regex, recipe_line):
        # Get mixed number by matching the regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()
        # group returns the part of the string where there was a match

        # replace the space in the mixed number with '+' sign
        amount = mixed_num.replace(" ", "+")

        # changes the string into a float using python's evaluation method
        amount = eval(amount) * scale_factor  # Scales the quantity as required


        # Get unit and ingredient
        compile_regex = re.compile(mixed_regex)
        # compiles the regex into a string object - so we can search for patterns

        unit_ingredient = re.split(compile_regex, recipe_line)
        # produces the recipe line unit and amount as a list

        unit_ingredient = (unit_ingredient [1]).strip()
        # removes the extra white space before and after the unit,
        # 2nd element in list, converting it into a string
    else:
        # splits the line of the first space
        get_amount = recipe_line.split(" ", 1)

        try:
            amount = eval(get_amount[0])  # Convert the amount to float if possible
            amount = amount * scale_factor

        except NameError:  # NameError rather than ValueError
            amount = get_amount[0]

        unit_ingredient = get_amount[1]

    # Get init and ingredient
    # splits the string into a list containing just the unit and ingredient
    get_unit = unit_ingredient.split(" ", 1)

    # Count the number of spaces in the recipe line
    num_spaces = recipe_line.count(" ")
    if num_spaces > 1:  # Item has both unit and ingredient
        unit = get_unit[0]  # Making the 1st item in the list 'unit'
        ingredient = get_unit[1]  # Making the 2nd item in the list 'ingredient'
        # All 3 elements of the original recipe line are now broken into the 3 required variables
        modernised_recipe.append("{} {} {}".format(amount, unit, ingredient))

    # to cope with ingredients not requiring a unit value e.g. '3 eggs'
    else:
        ingredient = get_unit[0]
        modernised_recipe.append("{} {}".format(amount, ingredient))


# Convert to mLs
# Converts from mLs to grams
# Add updated ingredient to list

# Output modernised recipe
for item in modernised_recipe:
    print(item)

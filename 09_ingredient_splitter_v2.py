""" Further version of an ingredient splitter which splits the ingredients
from one list of input into quantity, unit and ingredient
Version 2
Created by Amy Jorgensen
06/07/21
"""

import re  # This is the regular expression module

# Ingredient has mixed fraction followed by unit and ingredient
recipe_line = "1 1/2 ml flour"  # Change to input statement in due course

# The regex format below is expecting: number <space> number
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"
# \d for a digit, \d{1,3} allows 1-3 digits, \s for space, / for divide

# Testing to see if the recipe line matches the regular expression
if re.match(mixed_regex, recipe_line):
    print("True")
    # Get mixed number by matching the regex
    pre_mixed_num = re.match(mixed_regex, recipe_line)
    mixed_num = pre_mixed_num.group()
    # group returns the part of the string where there was a match

    # replace the space in the mixed number with '+' sign
    amount = mixed_num.replace(" ", "+")

    # changes the string into a float using python's evaluation method
    amount = eval(amount)
    print(amount)

    # Get unit and ingredient
    compile_regex = re.compile(mixed_regex)
    # compiles the regex into a string object - so we can search for patterns
    print(compile_regex)

    unit_ingredient = re.split(compile_regex, recipe_line)
    # produces the recipe line unit and amount as a list
    print(unit_ingredient)

    unit_ingredient = (unit_ingredient [1]).strip()
    # removes the extra white space before and after the unit,
    # 2nd element in list, converting it into a string
    print(unit_ingredient)


get_unit = unit_ingredient.split(" ", 1)
# splits the string into a list containing just the unit and ingredient
print(get_unit)

unit = get_unit[0]  # making the 1st item in the list 'unit'
ingredient = get_unit[1]  # making the 2nd item in the list 'ingredient'

# All 3 elements of the original recipe line are now broken into the 3 required variables
print(amount)
print(unit)
print(ingredient)

""" Initial version of an ingredient splitter which splits the ingredients
from one list of input into quantity, unit and ingredient
Version 1
Created by Amy Jorgensen
06/07/21
"""

import re  # This is the regular expression module

# Ingredient has mixed fraction followed by unit and ingredient
recipe_line = "1 1/2 ml flour"  # Change to input statement in due course

# The regex format below is expecting: number <space> number
mixed_recipe = "\d{1,3}\s\d{1,3}\/\d{1,3}"
# \d for a digit, \d{1,3} allows 1-3 digits, \s for space, / for divide

# Testing to see if the recipe line matches the regular expression
if re.match(mixed_recipe, recipe_line):
    print("True")
else:
    print("False")

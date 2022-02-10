""" Further version of an ingredient splitter which splits the ingredients
from one list of input into quantity, unit and ingredient
Version 3 - testing on full recipe
Created by Amy Jorgensen
06/07/21
"""

import re  # This is the regular expression module

# Reading from a full list of ingredients
# Ingredient has mixed fraction followed by unit and ingredient
full_recipe = [
    "1 1/2 ml flour",
    "3/4 cup milk",
    "1 cup flour",
    "2 tablespoons white sugar",
    "1 3/4 cups flour",
    "1.5 tsp baking powder",
    "pinch of cinnamon"
]

# The regex format below is expecting: number <space> number
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
        amount = eval(amount)

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
        except NameError:  # NameError rather than ValueError
            amount = get_amount[0]

        unit_ingredient = get_amount[1]

    # Get init and ingredient
    # splits the string into a list containing just the unit and ingredient
    get_unit = unit_ingredient.split(" ", 1)

    unit = get_unit[0]  # making the 1st item in the list 'unit'
    ingredient = get_unit[1]  # making the 2nd item in the list 'ingredient'

    # All 3 elements of the original recipe line are now broken into the 3 required variables
    print("{} {} {}".format(amount, unit, ingredient))

""" Recipe moderniser - full working program
Adding instructions and information at the start
Allowing fractional amounts for serving sizes
Alerting user to potential errors in their input e.g. "1/"
Version 8
Created by Amy Jorgensen
13/07/21
"""

# Modules to be used
import csv
import re


# FUNCTIONS
def round_amount(amount_to_round):
    # Finds whole numbers
    if amount_to_round % 1 == 0:
        # Converts to integer
        amount_to_round = int(amount_to_round)
    # Finds numbers with 1dp e.g. 0.5
    elif amount_to_round * 10 % 1 == 0:
        # Round to 1dp
        amount_to_round = "{:.1f}".format(amount_to_round)
    # Everything else is rounded to 2dp
    else:
        amount_to_round = "{:.2f}".format(amount_to_round)

    return amount_to_round

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

        if not response or number == True:  # print error for blank name or
            # digits
            print(error)

        else:
            return response


# number checking function
# Gets the scale factor - which must be a number
def num_check(question):
    valid = False
    error = "Please enter a number, higher than 0"
    while not valid:
        response = input(question)
        try:
            response = eval(response)
            response = float(response)
            if response <= 0:
                print(error)
            else:
                return response
        # allow inappropriate value to be entered
        except ValueError:
            print(error)
        # allow unrecognisable variable name
        except NameError:
            print(error)
        # show error rather than crashing if data type wrong
        except SyntaxError:
            print(error)


def get_scale_factor():
    keep_scale = False
    # Get serving size and check it's a number
    serving_size = num_check("\nWhat is the recipe serving size? ")
    # Get desired number of servings and check it's a number
    desired_size = num_check("How many servings would you like: ")
    # Calculate scale factor
    scale_factor = desired_size / serving_size

    while not keep_scale:
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

    line_number = 1  # To make sure entering the ingredients easy to follow
    while not valid_list:
        ingredient_name = not_blank("{}. ".format(line_number),
                                    "The ingredient cannot be blank",
                                    True).lower()
        # Check for exit code: 'X'
        if ingredient_name != 'x':
            # If exit code not entered, add ingredient to list
            ingredient_list.append(ingredient_name)
            line_number += 1
        else:
            if len(ingredient_list) < 2:  # Check that list contains at lease
                # 2 items
                print("Please enter at lease two ingredients")
            else:
                valid_list = True  # If contains at least two items, break loop
                return ingredient_list  # Output list


def general_converter(amount, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        factor = dictionary.get(lookup)
        amount *= float(factor) / conversion_factor
        converted = True
    else:
        converted = False
    return [amount, converted]


# Checks input for common abbreviations so that the correct conversion factor
# can be applied from the list in the unit_dict
def unit_checker(raw_unit):
    # Ask user for unit
    unit_to_check = raw_unit

    # abbreviation list
    teaspoon = ["tsp", "teaspoon", "t", "teaspoons"]
    tablespoon = ["tbs", "tbsp", "tablespoon", "T", "tablespoons"]
    cup = ["c", "cup", "cups"]
    ounce = ["oz", "fluid ounce", "fl oz", "ounce", "ounces", "oz."]
    pint = ["p", "pt", "fl pt", "pint", "pints", "pt."]
    quart = ["q", "qt", "fl qt", "quart", "quarts"]
    pound = ["lb", "lbs" "#", "pound", "pounds", "lb.", "lbs."]
    ml = ["millilitre", "milliliter", "cc", "mL", "millilitres", "milliliters",
          "mls"]
    litre = ["litre", "liter", "L", "litres", "liters"]
    decilitre = ["decilitre", "deciliter", "dL", "decilitres", "deciliters"]
    grams = ["g", "gram", "grams", "gm", "gms"]

    if not unit_to_check:  # if left blank
        # no need to print but still need to return it
        return unit_to_check
    elif unit_to_check in grams:
        return "gram"
    elif unit_to_check in teaspoon:
        return "teaspoon"
    elif unit_to_check in tablespoon:
        return "tablespoon"
    elif unit_to_check in cup:
        return "cup"
    elif unit_to_check in ounce:
        return "ounce"
    elif unit_to_check in pint:
        return "pint"
    elif unit_to_check in quart:
        return "quart"
    elif unit_to_check in pound:
        return "pound"
    elif unit_to_check in ml:
        return "mL"
    elif unit_to_check in litre:
        return "litre"
    elif unit_to_check in decilitre:
        return "decilitre"
    else:
        return unit_to_check  # If the unit to check is not in any list


def instructions():
    print()
    print("---------------- INSTRUCTIONS ----------------")
    print()
    print("This program converts recipe ingredients to mls / grams and also "
          "\nallows users to up size or down-size ingredients.")
    print()
    print("The program will ask for the source of the recipe - we recommend"
          "\ntyping in the URL where you found the recipe or the book where "
          "\nit is from so that you can refer back to the original if "
          "necessary.")
    print()
    print("The program also asks for the number of servings. If you are not "
          "\nsure, type '1'. Then when it asks for servings needed, you can "
          "\nincrease or decrease the amount (eg 2 or 1/2) and the program "
          "\nwill scale the ingredient amounts for you")
    print()
    print("Note that you can use fractions if needed. For example, write "
          "\none half as 1/2 and one and three quarters as 1 3/4")
    print()
    print("Please only type in ONE ingredient per line, if a recipe says"
          "\n'butter or margarine', choose ONE ingredient, either butter or"
          "\nmargarine")
    print()
    print("Lastly, all lines should start with a number / fraction unless"
          "\nthere is no number given e.g. a pinch of salt")
    print()
    print("-------------------------------------------------------")
    print()


# MAIN ROUTINE

# Set up dictionaries
unit_dict = {
    "teaspoon": 5,
    "tablespoon": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000,
    "decilitre": 100,
    "ml": 1,
    "gram": 1
}

# To check for errors in numeric entry of quantity
problem = False

# set up dictionary of conversion factors for ingredients
# Open file using appropriately named variable
groceries = open("01_ingredients_ml_to_g.csv")

# Read data from above into a list
csv_groceries = csv.reader(groceries)

# Create a dictionary to hold the data
food_dictionary = {}

# Add the data from the list into the dictionary
# (First item in row is key, and next is definition)
for row in csv_groceries:
    food_dictionary[row[0]] = row[1]
# Set up list to hold 'modernised' ingredients
modernised_recipe = []

# Providing option for new user to get instructions
print("-------- Welcome to the Great Recipe Moderniser --------")
print()

get_instructions = input("Press <enter> to get instructions, or any other key "
                         "+ <enter> "
                         "\nif you have used this program before: ")

if not get_instructions:
    instructions()
else:
    print()

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
        # compiles the regex into a string object - so we can search for
        # patterns

        unit_ingredient = re.split(compile_regex, recipe_line)
        # produces the recipe line unit and amount as a list

        unit_ingredient = (unit_ingredient[1]).strip()
        # removes the extra white space before and after the unit,
        # 2nd element in list, converting it into a string
    else:
        # splits the line of the first space
        get_amount = recipe_line.split(" ", 1)

        try:
            # Convert the amount to float if possible
            amount = eval(get_amount[0])
            amount = amount * scale_factor

        except NameError:  # NameError rather than ValueError
            amount = get_amount[0]
            modernised_recipe.append(recipe_line)
        except SyntaxError:  # if amount unrecognised e.g. 1/ instead of 1/2
            problem = True
            modernised_recipe.append(recipe_line)
            continue

        unit_ingredient = get_amount[1]

    # Get init and ingredient
    # splits the string into a list containing just the unit and ingredient
    get_unit = unit_ingredient.split(" ", 1)

    # Count the number of spaces in the recipe line
    num_spaces = recipe_line.count(" ")
    if num_spaces > 1:  # Item has both unit and ingredient
        unit = get_unit[0]  # Making the 1st item in the list 'unit'
        ingredient = get_unit[1]  # Make the 2nd item in the list 'ingredient'
        unit = unit_checker(unit)

        # If unit is already in grams, add to list
        if unit == "gram":
            modernised_recipe.append("{:.0f} grams {}".format(amount,
                                                            ingredient))
            continue

        # Convert to mls if possible: unit_dict gives amount in ml so
        # conversion factor is 1
        amount = general_converter(amount, unit, unit_dict, 1)

        # If converted to mls is 'True', try convert to grams
        if amount[1]:  # food_dictionary gives gms per 250 ml so conversion
            # factor is 250
            amount_2 = general_converter(amount[0], ingredient,
                                         food_dictionary, 250)

            # If 'true' the ingredient is in food_dictionary, so converts it
            # to grams
            if amount_2[1]:
                modernised_recipe.append("{:.0f} grams {}".format(amount_2[0], ingredient))
                # If only 2 elements (no unit) then just 2 variables needed

            # If the ingredient is not in the food_dictionary, leave as ml
            else:
                modernised_recipe.append("{:.0f} ml {}".format(amount[0], ingredient))

        # If the unit is not in mls, leave the line unchanged
        else:
            amount[0] = round_amount(amount[0])
            modernised_recipe.append("{} {} {}".format(amount[0], unit,
                                                       ingredient))

    # to cope with ingredients not requiring a unit value e.g. '3 eggs'
    else:
        amount = round_amount(amount)
        ingredient = get_unit[0]
        modernised_recipe.append("{} {}".format(amount, ingredient))


# Output details of recipe
print("\n-------------------- {} --------------------".format(recipe_name))
print("Source:", source)
print("\n---- Ingredients: scaled by a factor of {} ----".format(scale_factor))

# In the event of a problem with numeric entry of quantity
if problem:
    print()
    print("********* WARNING *********")
    print("Some of the entries below might be incorrect as there were "
          "\nproblems processing some of your input. "
          "\nIt's possible that you typed a fraction incompletely :(")
    print()

# Output modernised recipe
for item in modernised_recipe:
    print(item)

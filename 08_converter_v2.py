""" Second version of a combined converter using a function
Converts amount to mls and (if possible) converts to grams
Version 2
Created by Amy Jorgensen
1/07/21
"""
import csv

def general_converter(amount, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        factor = dictionary.get(lookup)
        amount *= float(factor) / conversion_factor
        converted = "yes"
    else:
        converted = "no"
    return [amount, converted]


# Checks input for common abbreviations so that the correct conversion factor
# can be applied from the list in the unit_dict
def unit_checker():
    # Ask user for unit
    unit_to_check = input("Enter the unit: ")

    # abbreviation list
    teaspoon = ["tsp", "teaspoon", "t", "teaspoons"]
    tablespoon = ["tbs", "tbsp", "tablespoon", "T", "tablespoons"]
    cup = ["c", "cup", "cups"]
    ounce = ["oz", "fluid ounce", "fl oz", "ounce", "ounces"]
    pint = ["p", "pt", "fl pt", "pint", "pints"]
    quart = ["q", "qt", "fl qt", "quart", "quarts"]
    pound = ["lb", "lbs" "#", "pound", "pounds"]
    ml = ["millilitre", "milliliter", "cc", "mL", "millilitres", "milliliters",
          "mls"]
    litre = ["litre", "liter", "L", "litres", "liters"]
    decilitre = ["decilitre", "deciliter", "dL", "decilitres", "deciliters"]

    if not unit_to_check:  # if left blank
        # no need to print but still need to return it
        return unit_to_check
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


# Main routine
# Set up dictionary
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
    "ml": 1
}

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

# Get items
complete_list = False
while not complete_list:

    # Ask user for amount
    amount = eval(input("Enter the amount: "))

    # Set unit and change it to match dictionary
    unit = unit_checker()

    # Get ingredient and change it to match dictionary
    ingredient = input("Ingredient: ").lower()

    # Convert to mls if possible
    amount = general_converter(amount, unit, unit_dict, 1)

   # If converted to mls, try to convert to grams
    if amount[1] == "yes":
        amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

        # If the ingredient is in the list, convert to grams
        if amount_2[1] == "yes":
            print(round(amount_2[0], 1), "grams")

        # If the ingredient is not in the conversion dictionary, leave as is
        else:
            print(round(amount_2[0], 1), "mls (Ingredient not in conversion dictionary")
    else:
        print(round(amount[0], 1), unit, "(Unable to convert to grams)")

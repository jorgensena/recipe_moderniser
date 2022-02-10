"""Initial version of a combined converter using a function
Converts amount to mLs but doesn't yet include conversion of mLs to grams
Version 1
Created by Amy Jorgensen
1/07/21
"""


def general_converter(amount, lookup, dictionary, conversion_factor):
    if lookup in dictionary:
        factor = dictionary.get(lookup)
        amount *= factor * conversion_factor

    return amount


# Checks input for common abbreviations so that the correct conversion factor
# can be applied from the list in the unit_dict
def unit_checker():
    # Ask user for unit
    unit_to_check = input("Enter the unit: ")

    # abbreviation list
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tbsp", "tablespoon", "T"]
    cup = ["c"]
    ounce = ["oz", "fluid ounce", "fl oz"]
    pint = ["p", "pt", "fl pt"]
    quart = ["q", "qt", "fl qt"]
    pound = ["lb", "lbs" "#"]
    ml = ["millilitre", "milliliter", "cc", "mL"]
    litre = ["litre", "liter", "L"]
    decilitre = ["decilitre", "deciliter", "dL"]

    if not unit_to_check:  # if left blank
        print("You have no unit")
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
}

complete_list = False
while not complete_list:

    # Ask user for amount
    amount = eval(input("Enter the amount: "))

    # Set unit and change it to match dictionary
    unit = unit_checker()

    # Check if the unit is in the dictionary
    # if unit is in dictionary, convert to mL
    # if not unit given or unit is unknown, leave as is
    amount = general_converter(amount, unit, unit_dict, 1)
    print(amount)

    # To end the loop of items to check
    another_item = input("\nPress <enter> to add another item"
                         "\nor any key + <enter> to end:"
                         "\n")
    if not another_item:
        continue
    else:
        complete_list = True

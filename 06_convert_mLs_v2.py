"""Get amount and unit from user then check if unit is in dictionary of units,
if it is, convert to mL's, otherwise leave as is.
Version 2 - adds loop for testing purposes
Created by Amy Jorgensen
29/06/21
"""


# Set up dictionary
unit_dict = {
    "tsp": 5,
    "tbsp": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454
}

complete_list = False
while not complete_list:

    # Ask user for amount
    amount = eval(input("Enter the amount: "))

    # Ask user for unit
    unit = input("Enter the unit: ")

    # Check if the unit is in the dictionary
    # if unit is in dictionary, convert to mL
    # if not unit given or unit is unknown, leave as is
    if unit in unit_dict:
        factor = unit_dict.get(unit)
        amount *= factor
        print("The amount in ml {}".format(amount))
    else:
        print("{} in unchanged".format(amount))

    # To end the loop of items to check
    another_item = input("\nPress <enter> to add another item"
                         "\nor any key + <enter> to end:"
                         "\n")
    if not another_item:
        continue
    else:
        complete_list = True


"""Get the ingredients required in the recipe, adding them to a list
and then printing the list at the end
Created by Amy Jorgensen
23/06/21
"""

# Ask user for ingredient name
# Check that response has been entered
def not_blank(question):
    error = "Please enter an ingredient name (cannot be blank)"
    valid = False
    while not valid:
        response = input(question)

        if not response:  # If no response, generate error message
            print(error)

        else:
            return response


# Main routine
# Set up ingredient list
ingredient_list = []

valid_list = False
while not valid_list:
    ingredient_name = not_blank("Enter an ingredient from the recipe "
                                "(or 'X' to exit): ").title()
    # Check for exit code: 'X'
    if ingredient_name != 'X':
        # If exit code not entered, add ingredient to list
        ingredient_list.append(ingredient_name)
    else:
        if len(ingredient_list) < 2:  # Check that list contains at lease 2 items
            print("Please enter at lease two ingredients")
        else:
            valid_list = True  # If contains at least two items, break loop
            print("Here are your ingredients:"  # Print list
                  "\n{}".format(ingredient_list))


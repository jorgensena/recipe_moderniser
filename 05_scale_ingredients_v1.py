"""Get the scale factor, then the ingredients and amount required for each
Then add the ingredients with their scaled amounts into a list to be printed
at the end
Created by Amy Jorgensen
27/06/21
"""

# number checking function
def num_check(response):
    valid = False
    error = "Please enter a number, higher than 0"
    while not valid:
        try:
            if response <= 0:
                response = float(input("Please enter a number more than 0: "))
            else:
                return response
        except ValueError:
            print(error)

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

# Replace line below with component 3 (number checker function) eventually
scale_factor = float(input("Scale Factor = "))

ingredient_list = []  # Set up ingredient list
valid_list = False

while not valid_list:
    amount = input("Enter amount (or 'X' to exit): ")
    if amount.upper() != 'X':
        if not amount or not amount.upper():  # Don't allow blank or strings
            print("Please enter a valid amount")
        else:
            amount = float(amount)  # Convert string to float
            scaled = num_check(amount) * scale_factor
            ingredient_name = not_blank("Enter an ingredient from the recipe: "
                                        ).title()
                # Calls the not_blank function and provides the question
            ingredient_list.append("{} units {}".format(scaled, ingredient_name))
                # Puts both elements on the same line
    elif len(ingredient_list) > 1:
        valid_list = True
            # If list contains at lease two items break out of loop
        print("Here are your ingredients:")
        for i in ingredient_list:
            print(i)  # Output list

    else:
        print("Please enter at lease two ingredients")


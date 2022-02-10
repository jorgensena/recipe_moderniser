"""Evaluates fractions for scale factor, rounds scaled amounts, and prevents
entry of digits in ingredient name
Version 2
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

    valid = False
    while not valid:
        response = input(question)

        if not response:  # checks if the response is blank
            print("Please enter an ingredient name (cannot be blank)")
            # if it is, generates error message
        elif not response.isalpha():  # checks to ensure the ingredient name
            # contains no digits
            print("The ingredient name can't contain digits")
        else:
            return response


# Main routine

# Replace line below with component 3 (number checker function) eventually
scale_factor = eval(input("Scale Factor = "))  # eval allows the scale factor
# to be entered as a fraction e.g. 1/3

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

            # Remove decimal point for whole numbers
            if scaled % 1 == 0:
                scaled = int(scaled)
            elif scaled * 10 % 1 == 0:
                scaled = "{:.1f}".format(scaled)  # 1dp (removes 2nd dp
                # when it's 0 e.g. 0.50)
            else:
                scaled = "{:.2f}".format(scaled)  # 2dp

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
